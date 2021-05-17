from bs4 import BeautifulSoup
from requests_html import HTMLSession

metrics_url = "https://spymetrics.ru/ru/website/"


def parse_site(domain="amazon.com"):
    try:
        session = HTMLSession()
        r = session.get(metrics_url + domain)
        r.html.render()
        soup = BeautifulSoup(r.html.html, "lxml")

        visits, avg_time_onsite, pages_per_visit = parse_main_stats(soup)
        sources = parse_sources(soup)
        geo = parse_geo(soup)
        ratings = parse_ratings(soup)
        return {"status": True, "data": {"visits": visits, "avg_time_onsite": avg_time_onsite, "pages_per_visit": pages_per_visit,
                "sources": sources, "best_geo": geo, "ratings": ratings}}
    except Exception as D:
        return {"status": False, "data": {}}


def parse_main_stats(soup: BeautifulSoup):
    td_list = soup.find_all("td", class_="text-right")

    return td_list[0].text, td_list[1].text, td_list[2].text


def parse_sources(soup: BeautifulSoup):
    chart = soup.find_all("g", class_="highcharts-data-labels highcharts-series-0"
                                             " highcharts-column-series highcharts-color-undefined highcharts-tracker")[0]
    source_users = chart.find_all("tspan", class_="highcharts-text-outline")

    sources = {"direct": source_users[0].text, "referrals": source_users[1].text, "search": source_users[2].text,
               "social": source_users[3].text, "mails": source_users[4].text, "banners": source_users[5].text}
    return sources


def parse_geo(soup: BeautifulSoup):
    table_geo = soup.find("table", id="countriesBreakdownTable").find_all("tr")
    countries = {}
    for i in table_geo:
        a_name = i.find("a", class_="country-name")
        span_name = i.find("span", class_="country-name")
        if a_name is not None:
            countries[a_name.text] = i.find("div", class_="shareValue").text
        else:
            countries[span_name.text] = i.find("div", class_="shareValue").text
    return countries


def parse_ratings(soup: BeautifulSoup):
    spans = soup.find_all("span", "text-right col-xs-12")
    names = soup.find_all("div", class_="ranking-subtext")
    ratings = {}
    for i in range(3):
        ratings[names[i].find("a").text.strip()] = spans[i].text.strip()
    return ratings

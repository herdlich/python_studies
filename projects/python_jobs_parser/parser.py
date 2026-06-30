import csv
import argparse
import requests
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin
from bs4 import BeautifulSoup as BS

BASE_URL = "https://www.python.org/jobs/"

Path("data").mkdir(exist_ok=True)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--output", default="data/jobs.csv")

    return parser.parse_args()


def save_csv(csv_file, data):
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["title", "company", "location", "category", "date", "link", "parsed_at"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def download_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return response.text

        else:
            print(f"Page was not downloaded: {url}, status code: {response.status_code}")
            return False

    except requests.RequestException as error:
        print(f"Request error: {error}")
        return False


def get_text_or_empty(element):
    if not element:
        return ""

    return element.get_text(strip=True)


def parse_page(html_text):
    if not html_text:
        print("HTML not found")
        return []

    soup = BS(html_text, "html.parser")
    vacancies = soup.select("ol.list-recent-jobs > li")

    job_list = []

    for vacancy in vacancies:
        title_element = vacancy.find("a", href=True)
        if not title_element:
            continue

        title = get_text_or_empty(title_element)

        link = title_element["href"]
        link = urljoin(BASE_URL, link)

        company_block = vacancy.find(class_="listing-company-name")
        company_name = ""
        if company_block and company_block.contents:
            company_name = company_block.contents[-1].strip()

        location_element = vacancy.find(class_="listing-location")
        location = get_text_or_empty(location_element)

        category_element = vacancy.find(class_="listing-company-category")
        category = get_text_or_empty(category_element)

        date_element = vacancy.find("time")
        date = get_text_or_empty(date_element)

        parsed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        vacancy_dict = {
            "title": title,
            "company": company_name,
            "location": location,
            "category": category,
            "date": date,
            "link": link,
            "parsed_at": parsed_at
        }

        job_list.append(vacancy_dict)

    return job_list


def parse_all_pages(csv_output):
    all_vacancies = []

    page_number = 1
    while True:
        page_url = BASE_URL + f"?page={page_number}"

        html_text = download_html(page_url)
        if not html_text:
            break

        page_vacancies = parse_page(html_text)

        if not page_vacancies:
            break

        all_vacancies.extend(page_vacancies)

        page_number += 1

    save_csv(csv_output, all_vacancies)

    return all_vacancies


def main():
    args = get_args()

    jobs = parse_all_pages(args.output)

    print(f"Saved jobs: {len(jobs)}")
    print(f"Output file: {args.output}")


if __name__ == "__main__":
    main()

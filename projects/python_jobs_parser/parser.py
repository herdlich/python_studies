import csv
import time
import logging
import argparse
import requests
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin
from bs4 import BeautifulSoup as BS

BASE_URL = "https://www.python.org/jobs/"

Path("logs").mkdir(exist_ok=True)

time_format = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(filename="logs/parser.log", level=logging.INFO, encoding="utf-8",
                    format="[%(asctime)s] - %(levelname)s: %(message)s", datefmt=time_format)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--output", default="data/jobs.csv")

    return parser.parse_args()


def save_csv(csv_file, data):
    Path(csv_file).parent.mkdir(parents=True, exist_ok=True)
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["title", "company", "location", "category", "description", "date", "link", "parsed_at"]

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
            logging.warning(f"Page was not downloaded: {url}, status code: {response.status_code}")

            return False

    except requests.RequestException as error:
        print(f"Request error: {error}")
        logging.error(f"Request error: {error}")

        return False


def parse_vacancies_links(html_text):
    if not html_text:
        print("HTML not found")
        logging.warning("HTML not found")

        return []

    soup = BS(html_text, "html.parser")
    vacancies = soup.select("ol.list-recent-jobs > li")

    links_list = []

    for vacancy in vacancies:
        link_element = vacancy.find("a", href=True)
        if not link_element:
            continue

        link = link_element["href"]
        link = urljoin(BASE_URL, link)

        link_dict = {
            "link": link
        }

        links_list.append(link_dict)

    return links_list


def parse_all_pages():
    all_links = []

    page_number = 1
    while True:
        page_url = BASE_URL + f"?page={page_number}"

        html_text = download_html(page_url)
        if not html_text:
            break

        page_vacancies = parse_vacancies_links(html_text)

        if not page_vacancies:
            break

        all_links.extend(page_vacancies)
        logging.info(f"Parsed page: {page_url}")

        page_number += 1

    logging.info(f"Found links: {len(all_links)}")

    return all_links


def parse_vacancy_detail(html_text, vacancy_link):
    soup = BS(html_text, "html.parser")

    company_name_tag = soup.find("span", class_="company-name")

    title = ""
    company = ""
    if company_name_tag:
        parts = [part.strip() for part in company_name_tag.get_text(separator="|").split("|") if part.strip()]
        title = parts[0] if len(parts) > 0 else ""
        company = parts[-1] if len(parts) > 1 else ""

    location_tag = soup.find("span", class_="listing-location")
    location = location_tag.get_text(strip=True) if location_tag else ""

    desc_tag = soup.find("div", class_="job-description")
    description = ""
    if desc_tag:
        start_h2 = desc_tag.find("h2", string="Job Description")

        if start_h2:
            description_blocks = []

            for sibling in start_h2.find_next_siblings():
                if sibling.name == "h2":
                    break
                if sibling.name == "p":
                    description_blocks.append(sibling.get_text(strip=True))

            description = "\n\n".join(description_blocks)

    time_tag = soup.find("time")
    date = time_tag.get_text(strip=True) if time_tag else ""

    category_tag = soup.find("span", class_="listing-company-category")
    category = category_tag.get_text(strip=True) if category_tag else ""

    parsed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    vacancy_dict = {
        "title": title,
        "company": company,
        "location": location,
        "category": category,
        "description": description,
        "date": date,
        "link": vacancy_link,
        "parsed_at": parsed_at
    }

    return vacancy_dict


def parse_vacancies_by_link():
    all_links = parse_all_pages()

    all_vacancies = []

    if not all_links:
        return []

    for link in all_links:
        vacancy_link = link["link"]
        if not vacancy_link:
            continue

        html_text = download_html(vacancy_link)
        if not html_text:
            continue

        vacancy_dict = parse_vacancy_detail(html_text, vacancy_link)

        all_vacancies.append(vacancy_dict)

        logging.info(f"Parsed vacancy: {vacancy_link}")

        time.sleep(0.5)

    return all_vacancies


def main():
    args = get_args()

    all_vacancies = parse_vacancies_by_link()

    if not all_vacancies:
        logging.warning("No vacancies found")

        return

    save_csv(args.output, all_vacancies)

    logging.info(f"Saved vacancies: {len(all_vacancies)}")
    logging.info(f"Output file: {args.output}")

    print(f"Saved vacancies: {len(all_vacancies)}")
    print(f"Output file: {args.output}")


if __name__ == "__main__":
    main()

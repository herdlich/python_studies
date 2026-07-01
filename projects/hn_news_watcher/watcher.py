import csv
import requests
import logging
import sqlite3
import argparse
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin
from bs4 import BeautifulSoup as BS

BASE_URL = "https://news.ycombinator.com/newest"
HN_BASE_URL = "https://news.ycombinator.com/"

Path("logs").mkdir(exist_ok=True)
time_format = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(filename="logs/watcher.log", level=logging.INFO, encoding="utf-8",
                    format="[%(asctime)s] - %(levelname)s: %(message)s", datefmt=time_format)

path_csv = Path("data/news.csv")
path_csv.parent.mkdir(exist_ok=True)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--db", default="data/news.db")
    parser.add_argument("--pages", type=int, default=3)

    return parser.parse_args()


def save_csv(csv_file, data):
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["title", "link", "age", "author", "points", "comments", "item_id", "parsed_at"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def db_init(db_file):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        title TEXT,
        link TEXT,
        age TEXT,
        author TEXT,
        points TEXT,
        comments TEXT,
        item_id INTEGER PRIMARY KEY,
        parsed_at TEXT
        )
        """)

    connection.commit()
    connection.close()


def download_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return response.text
        else:
            print(f"Page was not downloaded {url}, status code: {response.status_code}")
            return False

    except requests.RequestException as error:
        print(f"Request error: {error}")
        return False


def get_text_or_empty(element):
    if not element:
        return ""

    return element.get_text(strip=True)


def get_next_page_url(html_text):
    soup = BS(html_text, "html.parser")
    more_link = soup.select_one("a.morelink")
    if not more_link:
        return None

    link = more_link.get("href") if more_link else False
    link = urljoin(BASE_URL, link)

    return link


def parse_items(html_text):
    soup = BS(html_text, "html.parser")
    items = soup.select("tr.athing.submission")

    all_news_page = []

    for item in items:
        title_tag = item.select_one("span.titleline > a")
        if not title_tag:
            continue

        title = get_text_or_empty(title_tag)

        link = title_tag["href"]
        link = urljoin(HN_BASE_URL, link)

        item_id = item.get("id")

        subtext = item.find_next_sibling("tr")
        if not subtext:
            continue

        score_tag = subtext.select_one(".score")
        score = get_text_or_empty(score_tag)

        author_tag = subtext.select_one(".hnuser")
        author = get_text_or_empty(author_tag)

        age_tag = subtext.select_one(".age")
        age = get_text_or_empty(age_tag)

        comment_links = subtext.select("a[href^='item?id=']")
        comments = get_text_or_empty(comment_links[-1]) if comment_links else ""
        comments = comments.replace(" ", " ")

        parsed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_dict = {
            "title": title,
            "link": link,
            "age": age,
            "author": author,
            "points": score,
            "comments": comments,
            "item_id": item_id,
            "parsed_at": parsed_at
        }

        all_news_page.append(new_dict)

    return all_news_page


def parse_pages(start_url, pages):
    all_items = []
    html_text = download_html(start_url)
    if not html_text:
        return []

    for page in range(pages):
        all_news_page = parse_items(html_text)

        all_items.extend(all_news_page)

        next_link = get_next_page_url(html_text)
        if not next_link:
            break

        html_text = download_html(next_link)
        if not html_text:
            break

    return all_items


def item_exists(db_file, item_id):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute("""
    SELECT item_id FROM news
    WHERE item_id = ?
    """, (item_id,))

    result = cursor.fetchone()

    connection.close()

    return result is not None


def save_item_to_db(db_file, item):
    Path(db_file).parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO news (title, link, age, author, points, comments, item_id, parsed_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        item["title"],
        item["link"],
        item["age"],
        item["author"],
        item["points"],
        item["comments"],
        item["item_id"],
        item["parsed_at"]
    ))

    connection.commit()
    connection.close()


def find_new_items(db_file, items):
    new_items = []

    for item in items:
        item_id = item["item_id"]

        if not item_exists(db_file, item_id):
            save_item_to_db(db_file, item)
            new_items.append(item)

    return new_items


def main():
    args = get_args()

    db_init(args.db)

    all_pages = parse_pages(BASE_URL, args.pages)

    new_items = find_new_items(args.db, all_pages)

    save_csv(path_csv, all_pages)
    save_csv("data/new_items.csv", new_items)

    print(f"Found news: {len(all_pages)}")
    print(f"New news: {len(new_items)}")
    print(f"Output file: {path_csv}")

    logging.info(f"Found news: {len(all_pages)}")
    logging.info(f"Output file: {path_csv}")


if __name__ == "__main__":
    main()
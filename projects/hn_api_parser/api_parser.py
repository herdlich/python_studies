import csv
import requests
import argparse
import sqlite3
import logging
from pathlib import Path

API_URL = "https://hn.algolia.com/api/v1/search"

Path("logs").mkdir(exist_ok=True)
time_format = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(filename="logs/api_parser.log", level=logging.INFO, encoding="utf-8",
                    format="[%(asctime)s] - %(levelname)s: %(message)s", datefmt=time_format)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--output", default="data/news.csv")
    parser.add_argument("--db", default="data/news.db")
    parser.add_argument("--query", default="python")
    parser.add_argument("--pages", type=int, default=1)

    return parser.parse_args()


def fetch_data(query, page=0):
    params = {
        "query": query,
        "tags": "story",
        "page": page
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")
        logging.error(f"Request error: {error}")
        return None


def transform_items(data):
    news_list = []

    if data and "hits" in data:
        for hit in data["hits"]:
            title = hit.get("title") or ""
            author = hit.get("author") or ""
            created_at = hit.get("created_at") or ""
            updated_at = hit.get("updated_at") or ""
            if len(created_at) > 9:
                created_at = created_at[:10]
            if len(updated_at) > 9:
                updated_at = updated_at[:10]

            object_id = hit.get("objectID", "")
            link = hit.get("url") or f"https://news.ycombinator.com/item?id={object_id}"

            comments_count = hit.get("num_comments", "")
            points = hit.get("points", "")

            news_dict = {
                "object_id": object_id,
                "title": title,
                "link": link,
                "author": author,
                "points": points,
                "comments_count": comments_count,
                "created_at": created_at,
                "updated_at": updated_at
            }

            news_list.append(news_dict)

    return news_list


def save_csv(csv_file, data_to_csv):
    Path(csv_file).parent.mkdir(parents=True, exist_ok=True)

    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["object_id", "title", "link", "author", "points", "comments_count", "created_at", "updated_at"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data_to_csv)


def db_init(db_file):
    Path(db_file).parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        object_id TEXT PRIMARY KEY,
        title TEXT,
        link TEXT,
        author TEXT,
        points INTEGER,
        comments_count INTEGER,
        created_at TEXT,
        updated_at TEXT
        )
        """)

    connection.commit()
    connection.close()


def save_to_db(db_file, items):
    Path(db_file).parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.executemany("""
    INSERT OR IGNORE INTO news (object_id, title, link, author, points, comments_count, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, [
        (
            item["object_id"],
            item["title"],
            item["link"],
            item["author"],
            item["points"],
            item["comments_count"],
            item["created_at"],
            item["updated_at"]
        )
        for item in items
    ])

    connection.commit()
    connection.close()


def main():
    args = get_args()

    db_init(args.db)

    all_news = []

    for page_num in range(args.pages):
        raw_items = fetch_data(args.query, page=page_num)
        if not raw_items or not raw_items.get("hits"):
            print("No more data or error encountered")
            logging.warning("No more data or error encountered")
            break

        clean_items = transform_items(raw_items)

        all_news.extend(clean_items)

    if not all_news:
        print("No items found")
        logging.warning("No items found")
        return

    save_csv(args.output, all_news)
    save_to_db(args.db, all_news)

    print(f"News saved: {len(all_news)}")
    print(f"Output: {args.output}")

    logging.info(f"News saved: {len(all_news)}")
    logging.info(f"Output: {args.output}")


if __name__ == "__main__":
    main()

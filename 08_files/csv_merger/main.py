import csv
from pathlib import Path

path_products = Path("products")
path_merger = Path("merge.csv")

def load_csv(file):
    with open(file, "r", encoding="utf-8", newline="") as csvfile:
        reader = list(csv.DictReader(csvfile))

        return reader


def save_csv(file, data):
    with open(file, "w", encoding="utf-8", newline="") as csvfile:
        fieldnames = ["id", "title", "category", "price", "stock"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def csv_merger():
    all_rows = []

    processed_files = 0

    for file in path_products.glob("*.csv"):
        rows = load_csv(file)
        all_rows.extend(rows)

        processed_files += 1

    if processed_files == 0:
        print("No CSV files found")
        return

    if not all_rows:
        print("No rows found")
        return

    save_csv(path_merger, all_rows)

    print(f"Processed {processed_files} files")
    print(f"Saved {len(all_rows)} rows")


csv_merger()


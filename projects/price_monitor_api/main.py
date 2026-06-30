from fastapi import FastAPI
import monitor

app = FastAPI(title="Price Monitor API")


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/categories")
def categories():
    html_text = monitor.download_html(monitor.BASE_URL)

    if not html_text:
        return {
            "status": "error",
            "message": "HTML not found"
        }

    categories = monitor.parse_categories(html_text)

    if not categories:
        return {
            "status": "error",
            "message": "no categories found"
        }

    category_names = []

    for category in categories:
        category_name = category["name"]

        category_names.append(category_name)

    return {
        "categories": category_names,
        "count": len(category_names)
    }


@app.post("/monitor/{category}")
def monitor_category(category: str):
    result = monitor.run_monitor(category, "products.db", "price_changes.csv")

    return result


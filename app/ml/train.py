from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = BASE_DIR / "data/raw/bestsellers_with_categories.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data/processed/bestsellers_cleaned.csv"

print("Reading raw data from:", RAW_DATA_PATH)

df = pd.read_csv(RAW_DATA_PATH)

df = df.rename(columns={
    "Name": "title",
    "Author": "author",
    "User Rating": "rating",
    "Reviews": "review_count",
    "Price": "price",
    "Year": "year",
    "Genre": "genre"
})

df = df.drop_duplicates(subset=["title", "author", "year"])
df = df.dropna()

# Generate stable book_id
df["book_id"] = (
    df["title"].str.lower().str.replace(r"[^a-z0-9]+", "_", regex=True)
    + "_"
    + df["author"].str.lower().str.replace(r"[^a-z0-9]+", "_", regex=True)
    + "_"
    + df["year"].astype(str)
)

df.to_csv(PROCESSED_DATA_PATH, index=False)

print(f"Cleaned dataset saved to {PROCESSED_DATA_PATH}")
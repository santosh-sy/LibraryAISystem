from pymongo import MongoClient
import pandas as pd
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data/processed/bestsellers_cleaned.csv"

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI not found in .env")

client = MongoClient(MONGO_URI)
db = client["library_db"]

df = pd.read_csv(DATA_PATH)

print(f"Inserting {len(df)} records into MongoDB...")

db.books.delete_many({})
result = db.books.insert_many(df.to_dict(orient="records"))

print(f"Inserted {len(result.inserted_ids)} books into MongoDB")

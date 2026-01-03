# Library AI System

A Python-based backend application that demonstrates **machine learning in production** using FastAPI and MongoDB.  
The system provides **book recommendations** and **demand prediction** through REST APIs.

---

## Features

- Book catalog API backed by MongoDB
- Content-based book recommendation (TF-IDF + cosine similarity)
- Demand prediction using supervised machine learning (linear regression)
- Proper data preprocessing and train/test split
- API-driven model training and inference

---

## Tech Stack

- Python
- FastAPI
- MongoDB Atlas
- pandas, scikit-learn
- Kaggle dataset (Amazon Best Sellers: https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019)

---

## Machine Learning Overview

- **Recommendation System**:  
  Unsupervised, content-based filtering using book title, author, and genre.

- **Demand Prediction**:  
  Supervised regression model predicting book popularity using genre, year, price, and rating, with log-transformed targets and evaluation metrics (MAE, MSE).

---

## How to Run

```bash
pip install -r requirements.txt
python app/ml/train.py
python app/db/init_db.py
uvicorn app.main:app --reload
```
**Open Swagger UI at:**
http://127.0.0.1:8000/docs

---

## API Endpoints

- `GET /books`
- `GET /books/{book_id}`
- `GET /recommend/{book_id}`
- `POST /demand/train`
- `GET /demand/{book_id}`

---

## Purpose
This project was built to demonstrate backend engineering and applied machine learning concepts in a realistic system.
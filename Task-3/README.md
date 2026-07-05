# Task-3: AI Recommendation Logic

## 📌 Project Overview

This project is a simple **Content-Based Recommendation System** developed as part of the **DecodeLabs Artificial Intelligence Industrial Training Program (Batch 2026)**.

The system recommends courses based on the user's interests by comparing their input with course descriptions using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 🚀 Features

- Accepts user interests as input
- Uses TF-IDF to convert text into numerical vectors
- Computes similarity using Cosine Similarity
- Displays the top recommended courses
- Easy to understand and beginner-friendly

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Scikit-learn

---

## 📂 Project Structure

```
Task-3/
│── app.py
│── courses.csv
│── requirements.txt
└── README.md
```

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/sahilsri-07/decodelabstasks.git
```

Go to the project folder

```bash
cd decodelabstasks/Task-3
```

Install the required libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 💻 Example

### Input

```
Enter your interests:
python ai
```

### Output

```
Recommended Courses

AI Fundamentals           Similarity Score: 0.86
Python for Beginners      Similarity Score: 0.71
Data Science              Similarity Score: 0.54
Cloud Computing           Similarity Score: 0.00
Java DSA                  Similarity Score: 0.00
```

---

## ⚙️ How It Works

1. Load the dataset containing course names and tags.
2. Convert course tags into TF-IDF vectors.
3. Take the user's interests as input.
4. Transform the input into a TF-IDF vector.
5. Calculate Cosine Similarity between the user vector and all course vectors.
6. Sort the similarity scores.
7. Display the top matching recommendations.

---

## 📚 Concepts Used

- Content-Based Recommendation System
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Text Feature Extraction

---

## 🎯 Learning Outcomes

- Understand recommendation systems
- Learn TF-IDF vectorization
- Learn cosine similarity
- Work with textual datasets
- Build a basic AI recommendation engine

---

## 👨‍💻 Author

**Sahil Srivastava**

B.Tech CSE (AI & ML)

DecodeLabs Artificial Intelligence Internship – Task 3

---

## 📄 License

This project is created for educational purposes as part of the DecodeLabs AI Industrial Training Program.
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
courses = pd.read_csv("courses.csv")

# Convert tags into TF-IDF vectors
vectorizer = TfidfVectorizer()

course_vectors = vectorizer.fit_transform(courses["tags"])

# User Input
user_interest = input("Enter your interests: ")

# Convert user input to vector
user_vector = vectorizer.transform([user_interest])

# Calculate similarity
similarity = cosine_similarity(user_vector, course_vectors)

scores = similarity.flatten()

courses["Score"] = scores

recommendations = courses.sort_values(
    by="Score",
    ascending=False
)

print("\nRecommended Courses\n")

for index, row in recommendations.head(5).iterrows():
    print(
        f"{row['course']}  -> Similarity Score: {row['Score']:.2f}"
    )
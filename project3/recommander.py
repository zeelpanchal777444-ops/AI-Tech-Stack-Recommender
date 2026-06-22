import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("raw_skills.csv")

# User input
user_skills = input(
    "Enter skills separated by commas: "
)

# Combine dataset skills
documents = data["Skills"].tolist()

# Add user skills
documents.append(user_skills)

# TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# User vector
user_vector = tfidf_matrix[-1]

# Job vectors
job_vectors = tfidf_matrix[:-1]

# Cosine similarity
scores = cosine_similarity(
    user_vector,
    job_vectors
)

# Add score column
data["Score"] = scores[0]

# Sort results
recommendations = data.sort_values(
    by="Score",
    ascending=False
)

print("\n____________Top Recommendations:______________\n")

for index, row in recommendations.head(3).iterrows():
    print(
        f"{row['Role']} --> {round(row['Score']*100,2)}%"
    )
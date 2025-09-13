import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import re

# Load dataset
data = pd.read_csv('../data/students_data.csv')

# Training sample queries
training_queries = [
    "Score of Alice", "Grade of Bob",
    "Score of Student1", "Grade of Student200",
    "What is the score of Student45?", "Tell me the grade of Student99"
]

training_labels = [
    "score", "grade",
    "score", "grade",
    "score", "grade"
]

# Vectorize text
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_queries)

# Train simple classifier
clf = LogisticRegression()
clf.fit(X_train, training_labels)

print("Welcome to AI/ML Chatbot with NLP!")
print("You can ask for a student's Score or Grade by Name or ID.")
print("Type 'exit' to quit.\n")

while True:
    query = input("Your query: ").strip()
    if query.lower() == "exit":
        print("Goodbye!")
        break

    # Predict intent
    X_test = vectorizer.transform([query])
    intent = clf.predict(X_test)[0]

    # Extract Name or ID using regex
    id_match = re.search(r'\b\d+\b', query)
    name_match = re.search(r'Student\d+|[A-Z][a-z]+', query)

    if id_match:
        student_id = int(id_match.group())
        student_data = data[data['StudentID'] == student_id]
    elif name_match:
        student_name = name_match.group()
        student_data = data[data['Name'] == student_name]
    else:
        student_data = pd.DataFrame()

    if student_data.empty:
        print("Student not found.")
    else:
        if intent == "score":
            print(f"{student_data['Name'].values[0]}'s Score: {student_data['Score'].values[0]}")
        elif intent == "grade":
            print(f"{student_data['Name'].values[0]}'s Grade: {student_data['Grade'].values[0]}")
        else:
            print("Sorry, I can only provide Score or Grade.")

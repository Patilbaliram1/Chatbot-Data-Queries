import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import re

# Load dataset
data = pd.read_csv("students_data.csv")
data['Name'] = data['Name'].str.lower()

# Training data (INTENTS)
training_queries = [
    "score of student1",
    "grade of student2",
    "average score",
    "maximum score",
    "minimum score",
    "how many students",
    "top five students",
    "bottom five students"
]

training_labels = [
    "score",
    "grade",
    "average",
    "max",
    "min",
    "count",
    "top5",
    "bottom5"
]

# Vectorizer & Model
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_queries)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, training_labels)

print("📊 Advanced Student Analytics Chatbot")
print("Ask about scores, grades, averages, top students, etc.")
print("Type 'exit' to quit.\n")

while True:
    query = input("Your query: ").strip().lower()
    if query == "exit":
        print("Goodbye!")
        break

    intent = clf.predict(vectorizer.transform([query]))[0]

    # Student-specific queries
    name_match = re.search(r'student\d+', query)

    # ---- INDIVIDUAL QUERIES ----
    if intent in ["score", "grade"]:
        if name_match:
            student_name = name_match.group()
            student_data = data[data['Name'] == student_name]

            if student_data.empty:
                print("Student not found.")
            else:
                if intent == "score":
                    print(f"{student_name.upper()} Score: {student_data['Score'].values[0]}")
                else:
                    print(f"{student_name.upper()} Grade: {student_data['Grade'].values[0]}")
        else:
            print("Please specify a student (e.g., student1).")

    # ---- DATA ANALYTICS QUERIES ----
    elif intent == "average":
        print(f"📈 Average Score: {data['Score'].mean():.2f}")

    elif intent == "max":
        top = data.loc[data['Score'].idxmax()]
        print(f"🏆 Highest Score: {top['Name'].upper()} → {top['Score']}")

    elif intent == "min":
        low = data.loc[data['Score'].idxmin()]
        print(f"⬇️ Lowest Score: {low['Name'].upper()} → {low['Score']}")

    elif intent == "count":
        print(f"👥 Total Students: {len(data)}")

    elif intent == "top5":
        print("🏅 Top 5 Students:")
        print(data.nlargest(5, 'Score')[['Name', 'Score']])

    elif intent == "bottom5":
        print("🔻 Bottom 5 Students:")
        print(data.nsmallest(5, 'Score')[['Name', 'Score']])

    else:
        print("Sorry, I didn’t understand that.")

import pandas as pd

# Load the dataset
data = pd.read_csv('../data/students_data.csv')

print("Welcome to the AI/ML Data Query Chatbot!")
print("You can ask for a student's Score or Grade by Name or ID.")
print("Examples: 'Score of Student23', 'Grade of ID 45'")
print("Type 'exit' to quit.\n")

while True:
    query = input("Your query: ").strip().lower()
    
    if query == 'exit':
        print("Goodbye!")
        break

    # Search by Name
    if 'score of' in query:
        if 'id' in query:
            # By ID
            try:
                student_id = int(query.split('id')[-1].strip())
                result = data[data['StudentID'] == student_id]['Score']
                if not result.empty:
                    print(f"Score of Student ID {student_id}: {result.values[0]}")
                else:
                    print("Student ID not found.")
            except:
                print("Invalid ID format.")
        else:
            # By Name
            name = query.split('score of')[-1].strip().capitalize()
            result = data[data['Name'] == name]['Score']
            if not result.empty:
                print(f"Score of {name}: {result.values[0]}")
            else:
                print("Student Name not found.")

    elif 'grade of' in query:
        if 'id' in query:
            # By ID
            try:
                student_id = int(query.split('id')[-1].strip())
                result = data[data['StudentID'] == student_id]['Grade']
                if not result.empty:
                    print(f"Grade of Student ID {student_id}: {result.values[0]}")
                else:
                    print("Student ID not found.")
            except:
                print("Invalid ID format.")
        else:
            # By Name
            name = query.split('grade of')[-1].strip().capitalize()
            result = data[data['Name'] == name]['Grade']
            if not result.empty:
                print(f"Grade of {name}: {result.values[0]}")
            else:
                print("Student Name not found.")

    else:
        print("I can only provide Score or Grade. Try again.")

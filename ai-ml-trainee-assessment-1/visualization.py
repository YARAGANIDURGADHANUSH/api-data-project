import matplotlib.pyplot as plt

# Sample student data (simulate API response)
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 90},
    {"name": "David", "score": 65},
    {"name": "Eva", "score": 88}
]

# Extract names and scores
names = [student["name"] for student in students]
scores = [student["score"] for student in students]

# Calculate average
average_score = sum(scores) / len(scores)
print("Average Score:", average_score)

# Create bar chart
plt.bar(names, scores)
plt.title("Student Test Scores")
plt.xlabel("Students")
plt.ylabel("Scores")

plt.show()

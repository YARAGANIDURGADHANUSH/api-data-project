import matplotlib.pyplot as plt

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 90},
    {"name": "David", "score": 65},
    {"name": "Eva", "score": 88}
]

names = [student["name"] for student in students]
scores = [student["score"] for student in students]

average_score = sum(scores) / len(scores)
print("Average Score:", average_score)

plt.bar(names, scores)
plt.title("Student Test Scores")
plt.xlabel("Students")
plt.ylabel("Scores")

plt.show()

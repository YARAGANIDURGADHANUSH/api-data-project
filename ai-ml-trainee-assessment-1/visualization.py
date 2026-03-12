import matplotlib.pyplot as plt

# Sample student data (simulating API response)
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 90},
    {"name": "David", "score": 65},
    {"name": "Eva", "score": 88}
]


# Extract names and scores
def extract_data(data):
    names = [student["name"] for student in data]
    scores = [student["score"] for student in data]
    return names, scores


# Calculate average score
def calculate_average(scores):
    return sum(scores) / len(scores)


# Plot bar chart
def plot_scores(names, scores, avg_score):
    plt.figure(figsize=(8, 5))
    plt.bar(names, scores)

    plt.title("Student Test Scores")
    plt.xlabel("Students")
    plt.ylabel("Scores")

    # Display average line
    plt.axhline(avg_score, linestyle="--", label=f"Average Score: {avg_score:.2f}")

    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    names, scores = extract_data(students)

    avg_score = calculate_average(scores)
    print("Average Score:", avg_score)

    plot_scores(names, scores, avg_score)


if __name__ == "__main__":
    main()

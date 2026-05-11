# Student Grade Calculator
# A simple Python program to calculate and analyze student grades

def get_grade_letter(average):
    """Return the letter grade based on the average score."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_remarks(average):
    """Return remarks based on the average score."""
    if average >= 90:
        return "Excellent! Outstanding performance."
    elif average >= 80:
        return "Good job! Above average performance."
    elif average >= 70:
        return "Fair. Average performance."
    elif average >= 60:
        return "Needs improvement. Below average."
    else:
        return "Failing. Please seek help immediately."


def calculate_average(scores):
    """Calculate the average of a list of scores."""
    if not scores:
        return 0
    return sum(scores) / len(scores)


def get_student_scores():
    """Prompt the user to enter student name and scores."""
    print("\n" + "=" * 45)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 45)

    name = input("\nEnter student name: ").strip()
    if not name:
        name = "Unknown Student"

    subjects = []
    scores = []

    print(f"\nEnter subject names and scores for {name}.")
    print("Type 'done' when finished.\n")

    while True:
        subject = input("Subject name (or 'done' to finish): ").strip()
        if subject.lower() == "done":
            if len(scores) == 0:
                print("Please enter at least one subject.")
                continue
            break

        try:
            score = float(input(f"Score for {subject} (0-100): "))
            if score < 0 or score > 100:
                print("Score must be between 0 and 100. Try again.")
                continue
            subjects.append(subject)
            scores.append(score)
        except ValueError:
            print("Invalid score. Please enter a number.")

    return name, subjects, scores


def display_report(name, subjects, scores):
    """Display a formatted report card for the student."""
    average = calculate_average(scores)
    grade = get_grade_letter(average)
    remarks = get_remarks(average)

    print("\n" + "=" * 45)
    print("              REPORT CARD")
    print("=" * 45)
    print(f"  Student Name : {name}")
    print("-" * 45)
    print(f"  {'Subject':<20} {'Score':>10}")
    print("-" * 45)

    for subject, score in zip(subjects, scores):
        print(f"  {subject:<20} {score:>10.2f}")

    print("-" * 45)
    print(f"  {'Average Score':<20} {average:>10.2f}")
    print(f"  {'Grade':<20} {grade:>10}")
    print(f"  {'Highest Score':<20} {max(scores):>10.2f}")
    print(f"  {'Lowest Score':<20} {min(scores):>10.2f}")
    print("-" * 45)
    print(f"  Remarks: {remarks}")
    print("=" * 45)


def run_calculator():
    """Main loop to run the grade calculator."""
    print("\nWelcome to the Student Grade Calculator!")

    while True:
        name, subjects, scores = get_student_scores()
        display_report(name, subjects, scores)

        again = input("\nCalculate grades for another student? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThank you for using the Student Grade Calculator. Goodbye!\n")
            break


if __name__ == "__main__":
    run_calculator()

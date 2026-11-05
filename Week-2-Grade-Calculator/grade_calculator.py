"""Week 2: Validate marks and calculate a student's grade."""

def calculate_grade(marks):
    """Return the grade and an encouraging message for valid marks."""
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")

    if marks >= 90:
        return "A", "Excellent work! Keep it up."
    elif marks >= 80:
        return "B", "Very good! You are doing well."
    elif marks >= 70:
        return "C", "Good effort. Keep practising."
    elif marks >= 60:
        return "D", "You passed. Keep improving."
    else:
        return "F", "Do not give up. Review the topics and try again."


def main():
    while True:
        raw_marks = input("Enter marks (0-100): ").strip()
        try:
            marks = float(raw_marks)
            grade, message = calculate_grade(marks)
            print(f"Grade: {grade}")
            print(message)
            break
        except ValueError as error:
            print(f"Invalid input: {error}")
            print("Please enter a number from 0 to 100.")


if __name__ == "__main__":
    main()

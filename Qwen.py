"""Student grade calculator."""


def calculate_grade(score: int) -> str:
    """Return ``Pass`` or ``Fail`` for an integer score from 0 through 100."""
    if isinstance(score, bool) or not isinstance(score, int):
        raise ValueError("score must be an integer")
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")

    return "Pass" if score >= 60 else "Fail"


def main() -> None:
    """Read and grade multiple scores until the user chooses to quit."""
    print("Enter scores one by one. Type 'q' to quit.")

    while True:
        user_input = input("Enter the student's score (0-100): ").strip()

        if user_input.lower() in {"q", "quit"}:
            print("Goodbye!")
            break

        try:
            result = calculate_grade(int(user_input))
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    main()

def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 2:
                question, answer = parts
                questions.append((question.strip(), answer.strip()))
    return questions


def run_quiz(questions):
    score = 0
    total = len(questions)

    print("\n===== QUIZ START =====\n")

    for i, (question, correct_answer) in enumerate(questions, start=1):
        print(f"Q{i}: {question}")
        
        user_answer = input("Your Answer: ").strip().lower()
        correct_answer = correct_answer.strip().lower().replace('"', '')

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! Correct Answer: {correct_answer}\n")

    return score, total


def show_result(score, total):
    print("\n===== RESULT =====")
    print(f"Total Questions: {total}")
    print(f"Correct Answers: {score}")
    print(f"Wrong Answers: {total - score}")
    print(f"Score: {(score / total) * 100:.2f}%")

    if score == total:
        print("Excellent!")
    elif score >= total / 2:
        print("Good Job!")
    else:
        print("Need Improvement!")


def main():
    filename = "questions.txt"

    try:
        questions = load_questions(filename)
        if not questions:
            print("No questions found!")
            return

        score, total = run_quiz(questions)
        show_result(score, total)

    except FileNotFoundError:
        print("Question file not found!")


if __name__ == "__main__":
    main()
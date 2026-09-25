def calculate_final_score(quiz_score: float, exam_score: float, bonus_score: float):
    return ((quiz_score + exam_score) / 2) + bonus_score

def print_course_result(quiz_score: float, exam_score: float, bonus_score: float):
    final_score = calculate_final_score(quiz_score, exam_score, bonus_score)
    print(f"Final score: {final_score:.2f}")

    if final_score >= 50.0:
        print("Result: Pass")
    else:
        print("Result: Fail")

print_course_result(78.0, 86.0, 4.0)
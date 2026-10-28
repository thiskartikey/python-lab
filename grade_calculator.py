def calculate_scores(*args, **kwargs):
    score_list = list(args)

    if not score_list:
        return 0, 0, 0, {}

    min_score = min(score_list)
    max_score = max(score_list)
    avg_score = sum(score_list) / len(score_list)

    grade_breakdown = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for score in score_list:
        if score >= 90:
            grade_breakdown["A"] += 1
        elif score >= 80:
            grade_breakdown["B"] += 1
        elif score >= 70:
            grade_breakdown["C"] += 1
        elif score >= 60:
            grade_breakdown["D"] += 1
        else:
            grade_breakdown["F"] += 1

    print("Assessment Details:", kwargs)
    return min_score, max_score, avg_score, grade_breakdown

user_scores = tuple(map(int, input("Enter grades separated by spaces: ").split()))

min_val, max_val, avg_val, breakdown = calculate_scores(
    *user_scores, subject="Python", class_name="BCA"
)

print("Minimum Grade:", min_val)
print("Maximum Grade:", max_val)
print("Average Grade:", round(avg_val, 2))
print("Letter Grade Distribution:", breakdown)

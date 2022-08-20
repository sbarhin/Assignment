raw_scores = input("Record your scores and the required operation(C,D,+): ").split(",")
# raw_scores = ["5", "2", "C", "D", "+"]
scores = []
for raw_score in raw_scores:
    if raw_score.upper() == "C":
        del scores[-1]
    elif raw_score.upper() == "D":
        scores.append(scores[-1] * 2)
    elif raw_score.upper() == "+":
        scores.append(sum(scores[-2:]))
    else:
        scores.append(int(raw_score))
result = sum(scores)
print(result)
# def appending():
#     b = []
#     first_item = list_of_strings[0]
#     for index, item in enumerate(list_of_strings):
#         b.append(first_item)

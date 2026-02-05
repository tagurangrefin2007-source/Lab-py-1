scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hScore = scores[0]  
lScore = scores[0]  


print("All scores:", end=" ")
for score in scores:
    print(score, end=" ")
print()


for score in scores:
    if score > hScore:
        hScore = score
    if score < lScore:
        lScore = score


average = sum(scores) / len(scores)


print("Highest score =", hScore)
print("Lowest score =", lScore)
print("Average score =", average)


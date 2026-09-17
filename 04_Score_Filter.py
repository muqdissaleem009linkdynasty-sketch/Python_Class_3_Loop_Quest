scores = [42, 78, 91, 33, 67, 85, 49, 73, 58, 88]

count = 0

for score in scores:
    if score >= 70:
        print(score)
        count += 1

print("Number of scores 70 or above:", count)
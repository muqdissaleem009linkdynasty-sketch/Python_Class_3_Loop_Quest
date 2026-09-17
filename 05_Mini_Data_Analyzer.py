temperatures = [31, 34, 29, 36, 33, 27, 38, 35, 30, 32]

total = 0
days_35_or_above = 0
days_below_30 = 0

print("All temperatures:")
for temperature in temperatures:
    print(temperature)
    total += temperature

print("35 or above:")
for temperature in temperatures:
    if temperature >= 35:
        print(temperature)
        days_35_or_above += 1

for temperature in temperatures:
    if temperature < 30:
        days_below_30 += 1

average = total / len(temperatures)

print("Days at 35+:", days_35_or_above)
print("Days below 30:", days_below_30)
print("Total temperature:", total)
print("Average temperature:", average)
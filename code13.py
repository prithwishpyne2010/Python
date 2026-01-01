marks = [80, 75, 90, 85, 70]
total = sum(marks)
average = total / len(marks)

print("Total Marks:",total)
print("Average Marks:", average)

if average >=40:
    print("Conclusion: Student has passed.")
else:
    print("Conclusion: Student has failed.")

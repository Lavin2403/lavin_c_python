"""Write a program to accept a student’s name and scores in three subjects. Display the total, average,
and class secured based on the following criteria:
• 1st Class: Average score of 60 and above.
• 2nd Class: Average score of 50 and above.
• Pass Class: Average score of 35 and above.
• Fail: Average score less than 35."""

name=input("Enter your name: ")
sub1=int(input("Enter score in subject1: "))
sub2=int(input("Enter score in subject2: "))
sub3=int(input("Enter score in subject3: "))
total=sub1+sub2+sub3
print("Total marks is: ",total)
average=total/3
print("Average marks is: ",average  )
if average>=60:
    print("First class")
elif average>=50:
    print("Second class")
elif average>=35:
    print("Pass class")
elif average<35:
    print("Fail")
else:
    print("Invalid input")
    
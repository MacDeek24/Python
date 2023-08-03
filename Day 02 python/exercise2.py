# create a program using maths and f-string that tell
# us how many day,month and week we have left if we live until 90 years old 
a = int(input("Enter Your Current Age : "))

yearremainig= 90-a
dayremainig= yearremainig*365
weekremainig= yearremainig*52
monthremainig= yearremainig*12

print(f"You have {dayremainig} days , {weekremainig} weeks , {monthremainig} month")

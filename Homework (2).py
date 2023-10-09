

# HOMEWORK(GROUP_HOMEWORK) E(i)
def seconds_to_minutes(x):
    minutes = x / 60
    print(f"{x}seconds is the same as {minutes}minutes")

def minutes_to_seconds(x):
    seconds = x * 60
    print(f"{x}minutes is the same as {seconds}seconds.")



a = "minutes"
b = "seconds"

answer = input(f"Do you want your inputted number to be converted to {a} or {b}? ")

if answer == a:
    x = eval(input("Enter your number: "))
    seconds_to_minutes(x)

elif answer == b:
    x = eval(input("Enter your number: "))
    minutes_to_seconds(x)

else:
    print("ERROR!")








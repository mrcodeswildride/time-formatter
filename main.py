def format(number):
  if len(number) == 0:
    return "00"
  if len(number) == 1:
    return f"0{number}"
  else:
    return number

print()

hour = format(input("Enter the hour: "))
minute = format(input("Enter the minute: "))
second = format(input("Enter the second: "))

print(f"\nThe time is {hour}:{minute}:{second}")

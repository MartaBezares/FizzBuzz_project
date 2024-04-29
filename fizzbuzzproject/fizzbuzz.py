def fizz_buzz(max_num):
  for number in range(1, max_num + 1):
    if number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz")
    elif number % 3 == 0:
      print("Fizz")
    elif number % 5 == 0:
      print("Buzz")
    else:
      print(number)

fizz_buzz(100)

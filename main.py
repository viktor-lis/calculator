print("Калькулятор")


def calculation(number1, number2, action):
    match action:
        case "+":
          result = (number1 + number2)
        case "-":
          result = (number1 - number2)
        case "*":
          result = (number1 * number2)
        case "/":
          result = (number1 / number2)
        case "**":
          result = (number1 ** number2)
    return result
    # if action == "+":
    #     result = (number1 + number2)
    # if action == "-":
    #     result = (number1 - number2)
    # if action == "*":
    #     result = (number1 * number2)
    # if action == "/":
    #     result = (number1 / number2)
    # if action == "**":
    #     result = (number1 ** number2)
    # return resulta


while True:
      action = input("Выбирете действие."
                     "\nприбавить: +"
                     "\nотнять: -"
                     "\nумножить: *"
                     "\nразделить: /"
                     "\nстепень: **"
                     "\n Выход q\n")

      if action == "q":
          print("Досвидания")
          break
      elif action =="+" or action =="-" or action =="*" or action =="/" or action =="**":
            number1 = int(input("Ввведите первое число:\n\n"))
            number2 = int(input("Ввведите второе число:\n\n"))
            if action == "/" and number2 == 0:
                  print("На ноль елить нельзя!!!\n\n")
                  continue
      else:
          print("\nТаког действия нет.\n")
          continue
      res_cal = calculation(number1, number2, action)
      print("\n", res_cal, "\n")



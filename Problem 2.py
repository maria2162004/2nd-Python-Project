# Maria Atef Edward , 


def binary_num(num_str):  #this function ensures that the input is a binary numbers
    for number in num_str:
        if number != '0' and number != '1':
            return False
    return True


def menu1():  #menu1 used for inputing and validating the user's choice whether its A or B only
    while True:
        # menu 1
        print("Binary calculator")
        print("Please choose A or B: ")
        choice1 = input("A- Insert a number\nB- Exit")

        if choice1.upper() == "A":
            num1 = input("Enter a binary number: ")

            if not binary_num(num1):
             print ("enter a valid binary number")
            else:
                menu2(choice1,num1)

        elif choice1.upper() == "B":
            exit()

        else:
            print("Please select a valid choice (A/B)")
    return False, num1


def o_comp(binary_num):  #this function calculates one's complement
    if binary_num[0] == '0':
        return binary_num
    ones_complement = ''
    for bit in binary_num:
     ones_complement += '0' \
     if bit == '1' \
      else '1'
    return ones_complement


def t_comp(binary_num):   #this function calculates two's complement
    if binary_num[0] == '0':
        return binary_num
    ones_complement = o_comp(binary_num)
    result = ''
    carry = 1
    for bit in reversed(ones_complement):
            if bit == '0' and carry == 1:
                result = '1' + result
                carry = 0
            elif bit == '1' and carry == 1:
                result = '0' + result
            else:
                result = bit + result
    return result


def enforce_same_length(list1, list2):  #this function ensures that both binary inputs have the same length in addition and subtraction
    if len(list1) != len(list2):
        print("Binary numbers must be of the same length")
        return False
    else:
        return list1, list2


def add_binary(a, b):  #this function performs addition on 2 binary numbers
    x = enforce_same_length(a, b)
    if not x:
        return False
    carry = 0
    result = ''
    for i in range(len(a) - 1, -1, -1):
        sum_digit = carry
        if a[i] == '1':
            sum_digit += 1
        if b[i] == '1':
            sum_digit += 1

        if sum_digit % 2 == 1:
            result = '1' + result
        else:
            result = '0' + result

        carry = sum_digit // 2

    if carry > 0:
        result = '1' + result

    return result


def sub_binary(a, b):  #this function performs subtraction on 2 binary numbers
    x = enforce_same_length(a, b)
    if not x:
        return False
    carry = 0
    result = ''

    for i in range(len(a) - 1, -1, -1):
        diff_digit = carry + (1 if b[i] == '1' else 0) - (1 if a[i] == '1' else 0)

        if diff_digit < 0:
            diff_digit += 2
            carry = 1
        else:
            carry = 0

        result = str(diff_digit % 2) + result

    if carry > 0:
        result = '1' + result

    return result


def menu2(choice1,num1):  #menu2 is used to calculate 4 operations which I custom made a function for each one before
  while True:
        # menu 2
        print("Please select the operation you want to perform ")
        choice2 = input("A) Compute one's complement\nB) Compute two's complement\nC) Addition\nD) Subtraction\n")

        if choice2.upper() == "A":
            num1 = o_comp(num1)
            print(num1)
            menu1()

        elif choice2.upper() == "B":
            num1 = t_comp(num1)
            print(num1)
            menu1()

        elif choice2.upper() == "C":
            num2 = input("Please insert the second number: ")
            if not binary_num(num2):
                print("Please enter a valid binary number")
            else:
                sum_result = add_binary(num1, num2)
                print(str(num1) + " + " + str(num2) + " = " + str(sum_result))
                menu1()

        elif choice2.upper() == "D":
            num2 = input("Please insert the second number: ")
            if not binary_num(num2):
                print("Please insert a valid binary number")
            else:
                diff_result = sub_binary(num2, num1)
                print(str(num2) + " - " + str(num1) + " = " + str(diff_result))
                menu1()

        if choice1.upper() == "B":
            print("Exit the program")


num1 = ''
menu1()

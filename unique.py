def lab_3():
    numero = input("Enter a set of numbers: ")
    numbers = input("Enter another set of numbers: ")
    numero_list = numero.split(' ')
    numbers_list = numbers.split(' ')
    for num in numero_list:
        if num in numbers_list: 
            numbers_list.remove(num)

    print (numero_list + numbers_list)

lab_3()

# 1. Create input
# 2. Create list and use split
# 3. Use loop to check for duplicate number (blank.remove(num))
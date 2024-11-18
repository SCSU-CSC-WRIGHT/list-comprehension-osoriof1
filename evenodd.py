def lab_2():
    nums = input("Enter more than one number: ")
    nums_list = nums.split(' ')
    nums = 0
    for num in nums_list:
        if (int(num)%2==0):
            print("Even")
        else:
            print("Odd")    
            
        # if (num%2==1):
        #     print("Odd")

lab_2()

def lab_1():
    num = int(input("Enter # of scores: "))
    scores = []
    for i in range (num):
        score = float(input("Enter the score: "))
        scores.append(score)
    avg=sum(scores)/len(scores)
    if avg>90:
        print("A")
    elif avg>=80 and avg<90:
        print("B")
    elif avg>=70 and avg<80:
        print("C")
    elif avg>=60 and avg<70:
        print("D") 
    elif avg>=0 and avg<60:
        print("F")           

lab_1()        



    
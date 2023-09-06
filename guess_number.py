import random
minnumber = input("請輸入最小值")
maxnumber = input("請輸入最大值")
r = random.randint((int(minnumber)),(int(maxnumber)))
time=0
while True:
    anw = int(input("請輸入你猜的數字:"))
    if anw == r:
        if time == 0:
            print(f"太厲害了,{time + 1}次就猜中了")
            break
        else:
            print(f"終於猜對了,總共猜了{time+1}次")
            break
    elif anw > r:
        print(f"你猜的數字比答案大,你已經猜了{time+1}次")
    else:
        print(f"你猜的數字比答案小,你已經猜了{time+1}次")
    time += 1
print("這是你猜的第3次")
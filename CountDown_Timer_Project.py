import time 
start=int(input("Enter the number to start the countdown from: "))
print("\n---countdown start---")
while start >0:
    print(start)
    time.sleep(1)
    start -= 1
print("countdown completed")
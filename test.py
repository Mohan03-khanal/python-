import time
cH = time.strftime('%H:%M:%S')
print(cH)
cH = int(time.strftime('%H'))
a=input("Enter your name: ")
if cH < 12 :
    print("GM ",a)
elif 12 <= cH < 18:
    print("GA ",a)
else:
    print("GE ",a)
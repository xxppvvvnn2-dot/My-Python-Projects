import datetime
import math
import random
print("مبرحبا بك")
year = int(input("ادخل سنة ميلادك هنا"))
month = int(input("ادخل الشهر هنا"))
day = int(input("ادخل اليوم هنا"))
birth_date = datetime.date(year, month, day)
print("تم تسجيل تاريخ ميلادك بنجاح")
print(birth_date)
power = int(input("ادخل قوتك هنا من فضلك"))
print(math.sqrt(power))
print(random.randint(1, 100))
n = []
for i in range(3):
    number = int(input("ادخل رقم من فضلك"))
    n.append(number)
print(max(n))
print(sum(n))


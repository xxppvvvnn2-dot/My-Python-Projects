print('ادخل نقاط الطلاب ')
n = []
for i in range(5):
    score = float(input(f'ادخلها هنا :{i + 1}'))
    n.append(score)
print('اعلى درجة',max(n))
print('اقل درجة ',min(n))
print('مجموع الدرجات', sum(n))
def u():
    print("ادخل درجة للحصول على تقدير الطالب")
    for i in range(5):
        o = float(input('ادخله هنا:'))
        if o > 100 or o < 0:
            print("القيمة خاطئة")
        elif o >= 90:
            print('التقدير العام ممتاز')
        elif o >= 80:
            print('التقدير العام جيد جدا')
        elif o >= 65:
            print("التقدير العام جيد")
        elif o >= 55:
            print("التقدير العام مقبول")
        elif o >= 50:
            print("التقدير العام ناج بالكاد")
        else:
            print("التقدير العام راسب")
u()


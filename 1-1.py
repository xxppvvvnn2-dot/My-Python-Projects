

print("مرحبا بكم في برنامج قياس قوة الصياد")
try:
    name = str(input('ادخل اسم الصياد هنا:'))
    energy = float(input("قم بادخال مستوى الطاقة من 1 الى 100 هنا:"))
    iq = float(input("قم بادخال مستوى الذكاء من 1 الى 100 هنا:"))
    if (energy > 100 or energy < 0) or (iq > 100 or iq < 0):
        print("الرقم الذي ادخلته خاطئ")
        print("حاول مرة اخرى")
    else:
        value = (energy + iq) / 2
        print("مرحبا بك يا",name)
        print("هاذا هو معدل قوتك:",value)
        print("شكرا لاستخدامك نظام حساب القوة")
except ValueError:
    print("حدث خطا حاول مرة اخرى مع التركيز على الارقام والاحرف وشكرا لك")


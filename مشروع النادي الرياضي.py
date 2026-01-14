print("--اهلا بك في نظام النادي الرياضي--")
age = int(input("ادخل عمرك هنا من فضلك:"))
x = int(input("ادخل وزنك هنا من فضلك:"))
pro = input("هل انت محترف نعم/لا")
if age < 12 and pro == "لا":
    print("قسم الاشبال")
elif (age >= 12 and age < 18) and x < 60 and pro == "لا":
    print("فئة الناشئين - وزن خفيف")
elif (age >= 18 and pro == "نعم") and x > 70:
    print("قسم المحترفين - فريق المنافسات")
else:
    print("فريق الهواة")


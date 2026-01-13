print("مرحبا في برنامج التحقق من كلمة المرور")
user = str(input("ادخل اسم المستخدم هنا"))
password = str(input("ادخل كلمة المرور هنا"))
if user == password:
    print("خطر عالي للتعرض للهندسة الاجتماعية")
elif len(password) < 8:
    print("كلمة مرور ضعيفة جدا")
elif len(password) == 8:
    print("كلمة مرور عادية")
elif ("@" in password or "#" in password) and len(password) > 8:
    print("كلمة مرور قوية جدا")
else:
    print("كلمة مرور جيدة ولكن يفضل استخدام الرموز مثل @ و #")
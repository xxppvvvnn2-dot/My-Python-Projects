print("مرحبا بك في نظام معرفة المدرسين")
names = {"احمد":"علوم","هاني":"رياضيات","منصور":"لغتي"}
name = str(input("من فضلك ادخل الاسم هنا"))
if name in names:
    print(names[name])
else :
    print("الاسم خاطئة")
    print("حاول مرة اخرى")
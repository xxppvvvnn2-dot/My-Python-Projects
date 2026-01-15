print("----اهلا وسهلا بك----")
print('---------------------------------------')
try:
   name = str(input('ادخل اسمك هنا:'))
   if name == 'ملك الظلال' or name == 'shadow':
            print("اهلا وسهلا بك لقد تخطيت جميع البرتوكولات تفضل بالدخول")
   else:
    power = int(input("ادخل قوتك هنا:"))
    if power >= 10000:
      print( "الرتبة = s+")
    elif power >= 7000:
       print("الرتبة = s")
    elif power >= 5000:
       print("الرتبة = A")
    elif power >= 3000:
       print("الرتبة = B")
    elif power >= 1000:
        print("الرتبة = C")
    elif power >= 500:
        print("الرتبة = D")
    elif power >= 100:
        print("الرتبة = E")
    else:
        print("لم تستفق بعد!")
except ValueError:
    print("حدث خطا حاول مرة اخرى وتاكد من كتباة الارقام في خانتها والاحرف كذلك")

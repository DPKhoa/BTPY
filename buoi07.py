#Viết chương trình giải phương trình bậc hai với các hệ số được nhập từ bàn phím và hiển thị kết quả ra màn hình.Bài 19
import math
try:
    print("Nhập số a,b,c")
    a,b,c = map(float,input().split())
    if a ==0 :
        if b ==0:
            if  c == 0:
                print("Phương trinh vô số nghiệm !")
            else:         
             print("Phương có vô nghiệm ")
        else:
         print("Phương trình có nghiệm duy nhất \n x={}".format(-c/b))
    else:
     delta = b*b+2*a*c
    if delta > 0:
        x1 = float((-b + math.sqrt(delta)) / (2 * a))
        x2= float((-b - math.sqrt(delta)) / (2 *a ))
        print("Phương trình có 2 nghiệm phân biệt \nx1={} \nx2={}".format(x1,x2))
    elif delta == 0 :
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép \nx1=x2={}".format(x1,x2))
    else:
        print("Phương trình vô nghiệm")
except:
    print("Dữ liệu đầu vào sai ")
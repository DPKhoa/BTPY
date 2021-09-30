#bài 12
'''with open('inputN.inp','r',encoding='utf8') as fileInp:
        data = fileInp.readlines()
        print(data)
        stringJoined = ' '.join(data).replace('\n',' ')
        print(stringJoined)
fileOut = open('output.out','wb')
fileOut.write(stringJoined.encode('utf8'))'''
#bài 13
'''try:
    with open('inputN.inp','r',encoding='utf8') as fileInp:
        data=fileInp.readlines()
        print(data)
        stringJoined = ' '.join(data).replace('\n',' ')
        print(stringJoined)
        fileOut=open('output.out','wb')
        fileOut.write(stringJoined.encode('utf8'))
except:
    print('Định dạng không hộp lệ!!!')'''
#bài 14 +15
'''print("Tên bạn 1 và chiều cao")
yourFirstname,yourFirstHeight = input().split()
print("Tên bạn 2 và chiều cao ")
yourSecondname,yourSecondtHeight = input().split()
try:
   

    yourFirstHeight = int(yourFirstHeight)
    yourSecondtHeight = int(yourSecondtHeight)
    if yourFirstHeight <= 0 or yourSecondtHeight <= 0:
        print("CHieu cao phai lon hon 0")
    if yourFirstHeight > yourSecondtHeight:
        print(str(yourFirstHeight) + " is taller than " +str(yourSecondtHeight))
    elif yourFirstHeight == yourSecondtHeight:
         print(str(yourFirstHeight) + " same " +str(yourSecondtHeight))

    else:
        print(str(yourSecondtHeight) + " is taller than " +str(yourFirstHeight))
except:
    print("ban nhap sai ten roi!!!")'''
#bài 16 +17
'''print("nhap các cạnh a ,b ,c ")
try:
    a,b,c = map(float,input().split())    
    if a < 0 or b < 0 or c < 0:
        print("Các cạnh phải lớn hơn 0")
    if a + b > c or c + b >a:
        print("{} , {} , {} là 3 cạnh của 1 tam giác".format(a,b,c))
    else:
        print("không phải là tam giác")
except:
    print("Định dạng không hợp lệ")'''
#bài 18
print("nhập sô thứ nhất phép tính và số thứ 2")
sothunhat,sothu2,pheptinh = input().split()
sothunhat=float(sothunhat)
sothu2=float(sothu2)

ketqua = None
if pheptinh == '+':
    ketqua = sothunhat + sothu2
elif pheptinh == '-':
    ketqua = sothunhat - sothu2
elif pheptinh == '*':
    ketqua = sothunhat * sothu2
elif pheptinh == ':':
    if sothu2 == 0:
        print("Số bị chia phải lớn hơn 0")
    else:
        ketqua = sothunhat / sothu2
if ketqua != None:
    print("{} {} {} = {}".format(sothunhat,pheptinh,sothu2,ketqua))
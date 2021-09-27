'''bài 5
try:
    print("Nhap so thap phan")
    sothapphan = int(input())
    print("so thap phan %d trong he bat phan %o" %(sothapphan,sothapphan))

except: 
    print("moi ban nhap lại!!!!!!!")
'''
# bài 6
'''print("Nhap so thap nhan a")
sothapphana = float(input())
print("Số muốn làm tròn b")
sothapphanb = int(input())
print("Dùng format {0:.{1}f}".format(sothapphana,sothapphanb))

formatRound = round(sothapphana,sothapphanb)
print("Dùng round", formatRound)'''

# bài 7
'''try:
    soa = float(input())
    sob = int(input())
    print("{0:.{1}f}".format(soa,sob))
except:
    print("moi ban nhap lai ")''' 

# bài 8 
'''print("nhap vao day so")
daySo = input()
danhSachgiatri = daySo.split()
print(danhSachgiatri)
# map dùng để ép kiểu về int 
danhSachso = map(int,danhSachgiatri)
print(danhSachso)
tongDayso = sum(danhSachso)
print('Tổng dãy số là :',tongDayso)'''

# bài 9
'''print("nhập dãy số")
daySo = input()
danhSachgiatri = daySo.split()
try:
   
   
    danhSachso = map(int,danhSachgiatri)
    
    tongDayso = sum(danhSachso)
    print("Tổng dãy số là :",tongDayso)
except:
    print("bạn đã nhập sai ")'''

#bài 10 input ouput +11
try:
    with open('input.inp','r', encoding='utf8') as fileInp:
        ten = fileInp.readline().rstrip('\n')#bỏ các kí tự xuống dòng
        tuoi = int(fileInp.readline())
    with open('output.out','wb') as fielOut:
        stringTosave = ('20 năm nũa tuổi của {} sẽ là {} '.format(ten,tuoi+20))
        fielOut.write(stringTosave.encode('utf8'))
except FileExistsError:
    print("Không tim thấy file")
except FileNotFoundError:
    print("filenotfound")
except:
    print('Dinh dang k hop le!')
import random
list_option = ['keo', 'bua', 'bao']
print("Tro cho keo bua bao")
print("1: bua\n2: bao\n3: keo")

# khoi tao lua chon cua may
machine_option = random.choice(list_option)

# yeu cau nhap lua chon cua nguoi
people_option = int(input("Nhap 1 so tu 1 den 3 de dua ra lua chon: "))

#kiem tra nguoi dung nhap gi
# if people_option == 1:
#     people_option = 'bua'
# elif people_option == 2:
#     people_option = 'bao'
# else:
#     people_option = 'keo'
# #lua chon
# print("lua chon cua may ",machine_option)   
# print("lua chon cua nguoi ",people_option)

# #so sanh voi lua chon may
# if people_option == machine_option:
#     print("hoa")
# else:
#     if people_option == 'bua':
#         if machine_option == 'keo':
#             print("nguoi thang")
#         else:
#             print("may thang")
#     elif people_option == 'bao':
#         if machine_option == 'bua':
#             print("nguoi thang")
#         else:
#             print("may thang")
#     if people_option == 'keo':
#         if machine_option == 'bao':
#             print("nguoi thang")
#         else:
#             print("may thang")
if people_option == 1:
    people_option1 = 'bua'
elif people_option == 2:
    people_option1 = 'bao'
else:
    people_option1 = 'keo'
if machine_option == 'bua':
    machine_option1 = 1
elif machine_option == 'bao':
    machine_option1 = 2
else:
    machine_option1 = 3
#lua chon
print("lua chon cua may ",machine_option)   
print("lua chon cua nguoi ",people_option1)        
if machine_option1==people_option:
    print("hoa")
elif machine_option1 > people_option:
    print("may thang")
else:
    print("nguoi thang")  
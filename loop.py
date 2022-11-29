import time
# number=0
# while number <=20:
#     print(number)
#     number+=5



# number=[0,1,2,3,4,5,6,7,8,9]
# for a in number:
#     print(a)




# number=int(input('enter a number'))
# for a in range(1, number*4):
#    print(f'{a}')

# a=0
# while a<10:
#    print(a) 
#    a+=1

# a=5
# for x in range(a):
#    print(x) 

# x=int(input('enter a number'))
# for a in range(1,x):
#    print(x*1,x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9,x*10,x*11,x*12)


# number=int(input('enter any number '))
# print('the multiplication table of',number)
# for value in range(1,21):
#    print(number ,'x', value ,'=',number*value)

# number=str(input('enter the number to be reversed:'))
# print('reverse of the number is:')
# print(number[::-1])
# for tough in number[::-1]:
#    print(tough)


# for i in range(-10,0,1):
#    print(i)
# else:
#    print('done')   

number=str(input('enter pin\n'))
if number == '*141#':
   mtn = str(input('1.my offer\n2.daily bundle\n3.borrow airtime or data\n'))
   if mtn== '1':
      mtn_A = str(input('1.1GB for N200\n2.2.5GB for N500\n3.back\n'))
      if mtn_A == '1':
         print('please wait...')
         time.sleep(2)
         print('you have been credited with 1GB for 7 days')
      elif mtn_A == '2':
       print('you have been credited with 2.5GB for 14 days')
      else:
         print(mtn)
   elif mtn == '2':
      mtn_B = str(input('1.daily bundle\n2.mega bundle\n3.recharge from bank\n'))
      if mtn_B == '1':
         mtnb=str(input('1.N50 for 40MB\n2.N200 for 200MB\n3.N500 for 2GB for all socials\n'))
         if mtnb == '1':
            print('you have been credited with 40MB which will expire in 2 days')
         elif mtnb == '2':
            print('you have been credited with 200MB which will expire in 6 days')
         elif mtnb == '3':
            print('you have been credited with 2GB for all socials  including instagram and tiktok for 1month')
      elif mtn_B == '2':
         mtnb2 = str(input('1.N2000 for 6GB  in 3 months\n2.N3500 for 10GB in 5 months\n3.N5000 for 20GB in 7 months'))
         if mtnb2 == '1':
            print('you have been credited with 6GB in 3 months for all socials')
         elif mtnb2 == '2':
            print('you have been credited with 10GB in 5 months for all socials')
         elif mtnb2 =='3':
            print('you have been credited with 20GB in 7 months for all socials')
      elif mtn_B == '3':
         print('enter the bank name\n, the account number\n and the amount\n')
   elif mtn == '3':
      mtn_C = str(input('1.borrow airtime\n2.borrow data\n3.back\n'))
      if mtn_C == '1':
         mtnc = str(input('1.N100\n2.N200\n3.N500\n'))
         if mtnc== '1':
            print('you have just borrowed N100 to make calls')
         elif mtnc == '2':
            print('you have just borrowed N200 to make calls')
         elif mtnc == '3':
            print('you have just borrowed N500 to make calls')
      elif mtn_C == '2':
         mtnc2 = str(input('1.100MB for N100\n2.200MB for N200\n3.500MB for N500'))
         if mtnc2  == '1':
            print('you have just been credited with 100MB')
         elif mtnc2 == '2':
            print('you have just been credited with 200MB')
         elif mtnc2 == '3':
            print('you have just been credited with 500MB')
      elif mtn_C == '3':
         print(mtn)
   else:
      print('invalid activation code')
   
   



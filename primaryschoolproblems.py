print()
print('**************well come to my mathschool************')
print()
print('*****Here we have to learn lot of problems for primary school/children*****')
print()   
name=str(input('Can u please enter your good name:')).lower()
if name.isalpha(): 
     print()
     print('THANK your entering your name :',name)
     print()
else:
     print('please write the name only latter s')
     exit()
print()

ids = int(input("can u please Enter your  school ID: "))
 
if ids==12345:
     print('login successfull')
     print()
     while True:
               print()
               print(1,'even/odd or range of even number')
               print(2,'prime/range of prime_numbers/nth prime number')
               print(3,'multiplications tables /add/sub/multiply/division')
               print(4,'factrizations/divisers/sum of numbers and digits')
               print(5,'strong number/ amstrong number')
               print(0,'exit')
               print()
               n=int(input('choose the option above the blanks:'))
               if n==1:
                    print()
                    print('****** wellcone to even numbers world ******')
                    def even(a):
                         if a%2==0:
                              print('even number')        
                         else:
                              print('odd number')
                    def rangeofeven(n):
                         for i in range(n+1):
                              if i%2==0:
                                   print(i,'= even number/',end='  ')
                              else:
                                   print(i,'= odd number')
                    print()
                    while True:
                         print()
                         print(1,'even/odd number ')
                         print(2,'range of even/odd number')
                         print(3,'exit')
                         print()
                         k=int(input('choose the option wt u check :'))
                         if k==1:
                              u=int(input('can u please enter a number wt u want to checks:'))
                              even(u)
                         elif k==2:
                              n=int(input('can u plzz enter a number and it will range of even :'))
                              rangeofeven(n)
                         elif k==3:
                              break
                         else:
                              print('plzz choose the correct option 1/2/3')
                              s=input('if u want to check again press yes/no')
                              if s=='no':
                                   break     
               elif n==2:
                    print()
                    print('***** well come to the prime world *****')
                    def prime(n):
                         i=1
                         cnt=0
                         while i<=n:
                              if n%i==0:
                                   cnt=cnt+1
                              i=i+1
                         if cnt==2:
                              print('prime')
                         else:
                              print('not a prime')  
                    def rangeofprime(n):
                         i=1
                         while i<=n:
                              j=1
                              cnt=0
                              while j<=i:
                                   if i%j==0:
                                        cnt=cnt+1
                                   j=j+1
                              if cnt==2:
                                   print(i)
                              i=i+1
                    def nthprime(a):
                         i=1
                         count=0
                         while True:
                              j=1
                              cnt=0
                              while j<=i:
                                   if i%j==0:
                                        cnt=cnt+1
                                   j=j+1
                              if cnt==2:
                                   count=count+1
                                   print(i,end=' ')
                                   if count==a:
                                        print(i,'is the nth prime number')
                                        break
                              i=i+1
                    def primefactor(b):
                         i=1
                         while i<=b:
                              j=1
                              cnt=0
                              while j<=i:
                                   if i%j==0:
                                        cnt=cnt+1
                                   j=j+1
                              if cnt==2:
                                   while b%i==0:
                                        print(i)
                                        b=b//i
                              i=i+1      
                    print()
                    while True:
                         print()
                         print('if u want to check plzz choose the options if u want to exits press option 5')
                         print()
                         print(1,'prime or not')
                         print(2,'range of the prime number')
                         print(3,'nth prime numbers')
                         print(4,'prime factors')
                         print(5,'back')
                         print()
                         c=int(input('can u please choose the option s above blanks:'))
                         if c==1:
                              n=int(input('Can enter a number to check is it prime or not:'))
                              print()
                              prime(n)
                         elif c==2:
                              m=int(input('please enter a number to check the range of prime number:'))
                              rangeofprime(m)
                         elif c==3:
                              y=int(input('please enter a number nth prime number:'))
                              nthprime(y)
                         elif c==5:
                              break
                         elif c==4:
                              z=int(input('enter a prime factor number wt u want:'))
                              primefactor(z)
                         else:
                              print('plzz choose the currect options 1/2/3/4')
                              h=input('if u want to check again press yes/no')
                              if h=='no':
                                   print('thank you for choosing ')
                                   break

                 
               elif n==0:
                         break
 
               
               elif n==3:
                    print()
                    print('****** wellcome to the tables world *******')
                    print()
                    def tables(a):
                         i=1
                         while i<=10:
                              print(a,'*',i,'=',a*i)
                              i=i+1
                    def multiply(a,b):
                         c=a*b
                         j=a+b
                         k=a-b
                         return c ,'= is the multily of two number and : (',j,')= is the addition of the numbers and :(',k,')= is the substraction of the numbers ',a,b
                    def divisions(a,b):
                         c=a%b
                         d=a/b
                         e=a//b
                         return c,',= module division of two number and : (',d,')= is the float division and :(',e,')= is the division of the two number',a,b
                    print()
                    print('At a time we calculates like tables and (*,+,-,%,/) ')
                    n=int(input('please enter a tables number'))
                    tables(n)
                    print()
                    print('can u plzz enter a two number in two inputs ex: 1 * 2(+,-,,) etc')
                    a=int(input('enter a first number:'))
                    b=int(input('enter a second number:'))
                    print()
                    y=multiply(a,b)
                    print(y)
                    print()
                    f=divisions(a,b)
                    print(f)
               elif n==4:
                    print()
                    print('******* welcome to the factorial of numbers *******')
                    print()
                    def factrial(n):
                         f=1
                         while n>1:
                              f=f*n
                              n=n-1
                         print(f)
                    def diviser(n):
                         i=1
                         cnt=0
                         s=0
                         while i<=n:
                              if n%i==0:
                                   print(i)
                                   cnt=cnt+1
                                   s=s+i
                              i=i+1
                         print(cnt,'there are diviser of :',n)
                         print(s,'the sum if the diviser of :',n)
                    def sumofnumbers(n):
                         i=1
                         s=0
                         while i<=n:
                              s=s+i
                              i=i+1
                         print(s)
                    def sumofdigits(b):
                         s=0
                         while b>0:
                              d=b%10
                              s=s+d
                              b=b//10
                         print(s,'= is the sum of the digits of values =',p) 
                    while True:
                         
                         print()
                         print(1,'factrizations')
                         print(2,'diviser')
                         print(3,'sum of the range of number')
                         print(4,'sum of the digits')
                         print(5,'back')
                         print()
                         x=int(input('choose the option wt u calculate:'))
                         if x==1:
                              n=int(input('can u plzz enter a number to check factors:'))
                              factrial(n)
                         elif x==2:   
                              m=int(input('plzz enter a number to check diviser:'))
                              diviser(m)
                         elif x==3:                         
                              s=int(input('can u plzz enter a number to check sum ranges:'))
                              sumofnumbers(s)
                         elif x==4:                                
                              p=int(input('enter a sum of digits vise:'))
                              sumofdigits(p)
                         elif x==5:
                              break
                         else:
                              print('can u please choos the option s like 1/2/3/5 or 5:')
                              h=input('if u want to press again choose the option yes/no').lower()
                              if h=='no':
                                   print('thank you for using have a nice day')
                                   break
               elif n==5:
                    print()
                    print('******** welcome to big numbers stronge/amstrong ********')
                    print()
                    def stronge(a):#153
                         s=0
                         while a>0:#15
                              d=a%10#3 5
                              f=1
                              while d>=1:#3 2 1 t
                                   f=f*d#f=1*3=3 *2=6 5
                                   d=d-1#d=3-1=2
                              s=s+f#24+120+1
                              a=a//10#15
                         if s==n:
                              return 'strong number'
                         else:
                              return 'not a strong number'
                    def rangeofstronge(k):
                         i=1
                         while i<=k:
                              n=i
                              s=0
                              while n>0:
                                   d=n%10
                                   f=1
                                   while d>=1:
                                        f=f*d
                                        d=d-1
                                   s=s+f
                                   n=n//10
                              if s==i:
                                   print(i)
                              i=i+1
                    def amstronge(a):
                         cnt=len(str(a))
                         s=0
                         while a>0:
                              d=a%10
                              s=s+d**cnt
                              a=a//10
                         if s==q:
                              print('amstrong')
                         else:
                              print('not a amstrong')
                    def rangeofamstronge(k):
                         i=1
                         while i<=k:
                              a=i
                              cnt=len(str(a))
                              s=0
                              while a>0:
                                   d=a%10
                                   s=s+d**cnt
                                   a=a//10
                              if s==i:
                                   print(i)
                              i=i+1
                    n=int(input('enter a number'))
                    k=stronge(n)
                    print(k)
                    p=int(input('enter a numbers'))
                    rangeofstronge(p)
                    q=int(input('enter a amstrong number'))
                    amstronge(q)
                    r=int(input('enter a rangeof amstrong'))
                    rangeofamstronge(r)
else:
     print('invalid id number :')
     exit()
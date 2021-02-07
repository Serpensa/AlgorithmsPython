#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.


l1=input('Enter letter1=')
l2=input('Enter letter2=')
n1=ord(l1)-96
n2=ord(l2)-96
if n1>n2:
    n3=n1-(n2+1)
else:    
    n3=n2-(n1+1)
print('number of letter1=',n1,';number of letter2=',n2, ';letters between= ', n3)
password=input('Введите пароль:')
digits='1234567890'
upper_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letters='abcdefghijklmnopqrstuvwxyz'
symbols='!@#$%^&*()-+'
message="Слабый пароль.Рекомендации:"
acceptable=upper_letters+lower_letters+symbols
cond1=(len(password))>11
cond2=all(char in password for char in symbols)
cond3=all(char in password for char in upper_letters)
cond4=all(char in password for char in digits)
cond5=all(char in set(password) for char in set(acceptable))
rules=[cond1,cond2,cond3,cond4,сond5]
p=set(password)
a=set(acceptable)
result=[]

for x in p:
    result.append(x in a)
if all(result) is False:
    print('Ошибка. Запрещенный спецсимвол')
elif all(result) is True:
    if cond1 is False:
        message+=' увеличить число символов -'+" "+str(12-len(password))+','      
    if cond2 is False:
        message+=' '+'добавить 1 спецсимвол,'
    if cond3 is False:
        message+=' '+'добавить 1 заглавную букву,'
    if cond4 is False:
        message+=' '+'добавить 1 цифру,'
        print(message[:(len(message)-1)])
else:
    if all(rules) is True:
        print('Сильный пароль')
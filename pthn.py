def is_valid(n):
    if 1 <= n <= 100:  
        return True
    else:
        return False

from random import randint  

def game():  
    print("Добро пожаловать в числовую угадайку")
    num1 = 0
    print("Введите число - конец диапазона")
    n = int(input())
    num = randint(1, n+1) 
    count = 0
    while num1 != num:
        count += 1
        print("Напишите число")
        num1 = int(input())
        if is_valid(num1):
            if num1 < num:
                print("Ваше число меньше загаданного, попробуйте еще разок") 
            elif num1 > num:  
                print("Ваше число больше загаданного, попробуйте еще разок")
            
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")
    print(f'Победа!!! Вы угадали ответ за {count} попыток, поздравляем!')

while True:
    game()
    print("Вы хотели бы продолжить? (yes)")
    s = input().lower()
    if s != "yes":  
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
        break



#attempts counter
# n = int(input())
# count = 0
# while n >1:
#     if n %2 == 0:
#         n +=1
#     n/=2 
#     count+=1
# if count == 0:
#     print(n)
# else:    
#     print(count)


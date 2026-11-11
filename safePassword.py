from random import *

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation= "!#$%&*+-=?@^_."
ambiguous = "il1Lo0O"
chars = ''

print("Количество паролей для генерации: ")
total_passwords = int(input())
print("Длинa одного пароля: ")
password_len = int(input())
print("Включать ли цифры 0123456789?")
answer = input().lower()
if answer == "да":
    chars += digits 
print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?")
answer1 = input().lower()
if answer1 == "да":
    chars += lowercase_letters
print("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?")
answer2 = input().lower()
if answer2 == "да":
    chars += uppercase_letters
print("Включать ли символы !#$%&*+-=?@^_?")
answer3 = input().lower()
if answer3 == "да":
    chars += punctuation 
print("Исключать ли неоднозначные символы il1Lo0O?")
answer4 = input().lower()
if input().lower() == "да":
    chars = "".join(c for c in chars if c not in ambiguous)

if not chars:
    print("Не выбрано ни одного символа для генерации паролей!")
else:
    def generate_password(length, chars):
        password = ""
        for _ in range(length):
            password += choice(chars)
        return password

    for _ in range(total_passwords):
        print(generate_password(password_len, chars))

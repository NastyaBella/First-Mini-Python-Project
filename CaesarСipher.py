s=list("Блажен, кто верует, тепло ему на свете!")
result = []

const_upper_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
const_lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

for c in s:
    if c.isalpha():
        if c in const_upper_ru:
            index = (const_upper_ru.find(c)+10)%32
            result.append(const_upper_ru[index])
        elif c in const_lower_ru:
            index = (const_lower_ru.find(c)+10)%32
            result.append(const_lower_ru[index])
    else:
        result.append(c)

for i in result:
    print(i, end="")
    
#Russian reverse
s2=list("Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.")
result2 = []


for c in s2:
    if c.isalpha():
        if c in const_upper_ru:
            index = (const_upper_ru.find(c)-7)%32
            result2.append(const_upper_ru[index])
        elif c in const_lower_ru:
            index = (const_lower_ru.find(c)-7)%32
            result2.append(const_lower_ru[index])
    else:
        result2.append(c)

for i in result2:
    print(i, end="")
print()

#English
s1 = list("Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.")
result1 = []

const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const_lower_en = 'abcdefghijklmnopqrstuvwxyz' 

for c in s1:
    if c.isalpha():
        if c in const_upper_en:
            index = (const_upper_en.find(c)-25)%26
            result1.append(const_upper_en[index])
        elif c in const_lower_en:
            index = (const_lower_en.find(c)-25)%26
            result1.append(const_lower_en[index])
    else:
        result1.append(c)

for i in result1:
    print(i, end="")

print()

#English
s3 = list("To be, or not to be, that is the question!")
result3 = []

for c in s3:
    if c.isalpha():
        if c in const_upper_en:
            index = (const_upper_en.find(c)+17)%26
            result3.append(const_upper_en[index])
        elif c in const_lower_en:
            index = (const_lower_en.find(c)+17)%26
            result3.append(const_lower_en[index])
    else:
        result3.append(c)

for i in result3:
    print(i, end="")

print()

#find shift
s4 = list("Hawnj pk swhg xabkna ukq nqj.")

n = const_lower_en.find("p") - const_lower_en.find("t")
result4 = []

for c in s4:
    if c.isalpha():
        if c in const_upper_en:
            index = (const_upper_en.find(c)-n)%26
            result4.append(const_upper_en[index])
        elif c in const_lower_en:
            index = (const_lower_en.find(c)-n)%26
            result4.append(const_lower_en[index])
    else:
        result4.append(c)

for i in result4:
    print(i, end="")


#Ave, Caesar! (count shift by word length) 
s5 = input().split()
result5 = []

const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const_lower_en = 'abcdefghijklmnopqrstuvwxyz'

for word in s5:
    encrypted_word = [] 
    
    word_length = sum(1 for char in word if char.isalpha()) 

    
    for char in word: 
        if char.isalpha():
            if char in const_upper_en:
                index = (const_upper_en.find(char) + word_length) % 26
                encrypted_word.append(const_upper_en[index])
            elif char in const_lower_en:  
                index = (const_lower_en.find(char) + word_length) % 26
                encrypted_word.append(const_lower_en[index])
        else:
            encrypted_word.append(char)  
    
    result5.append("".join(encrypted_word)) 


print(" ".join(result5))  

#8*n + 8 = 3*n + 2 + 2*n + 2 + 1*n + 6 + 1*n + 7
# 8n-3n-2n-n-n = -8+2+2+6+7
#n=9


bin_num1 = bin(10) #2  0b
print(bin_num1[2:])  #we cut str to remove 0b
print(oct(10)) #8  0o
print(hex(10)) #16  0x

num = int(input())

bin_num = bin(num)  
oct_num = oct(num)  
hex_num = hex(num).upper()  

print(bin_num[2:])  
print(oct_num[2:])  
print(hex_num[2:])  



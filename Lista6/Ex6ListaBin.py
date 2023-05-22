num = int(input("informe o número decimal: "))

hexa = ""
while num > 0:
    resto = num % 16
    if resto <= 9:
        hexa = str(resto) + hexa
    elif resto == 10:
        hexa = "A" + hexa
    elif resto == 11:
        hexa = "B" + hexa        
    elif resto == 12:
        hexa = "C" + hexa        
    elif resto == 13:
        hexa = "D" + hexa        
    elif resto == 14:
        hexa = "E" + hexa        
    else:
        hexa = "F" + hexa                                        

    num = num // 16

print(hexa)
import unicodedata

def checkA(string):
    cnt = 0
    
    for i in string:
        if unicodedata.normalize('NFD', i)[0] == 'a':
            cnt += 1
    
    return cnt


print("Escreva uma frase: ")
string = input()

print("A letra 'a' aparece", checkA(string), "vezes na frase")
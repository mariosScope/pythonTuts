
def stringTransformer(s) :
    words = s.split()

    reversedWords = words[::-1]

    reversedString = ' '.join(reversedWords)
    
    return reversedString

# Order numbers?
# Find missing numbers in sequence
def findMissingNumbers(unsortedNumbers) :
    #order numbers
    #find missing in sequence
    # return array with 2 missing numbers? 
    # return text with 2 missing numbers?
    N = len(unsortedNumbers)+2
    suma = (N*(N+1))/2
    for i in unsortedNumbers :
     suma -= i
    average = suma/2
    sumAverage = (average*(average+1))/2
    x = 0
    for i in unsortedNumbers :
     if i <= average :
      x += i
    num1 = int(sumAverage-x)
    num2 = int(suma-num1)
    result = [num1,num2]
    return result

print(findMissingNumbers([1,2,5,7,6]))
print(stringTransformer("Este Texto debe salir Pero alrevés"))



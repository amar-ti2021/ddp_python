import math
a = 1
b = 8
c = 12

def countSq(a, b, c):
    hasil = math.sqrt((math.pow(b, 2) - 4 * a * c))
    while hasil % 1 != 0.0:
       hasil = simpSq([hasil])
    hasil = [hasil]
    return hasil


def simpSq(lst):
    hasil = lst
    primeNum = [2, 3, 5, 7, 11,
                13, 17, 19, 23, 29,
                31, 37, 41, 43, 47,
                53, 59, 61, 67, 71,
                73, 79, 83, 89, 97]
    num2 = [1]
    sqr = math.sqrt(hasil[0])
    while sqr % 1 != 0.0:
        num = hasil.pop(0)
        for x in primeNum:
            if num % x == 0:
                y = num / x
                if x in hasil:
                    num2.append(hasil.pop(hasil.index(x)))
                else:
                    hasil.insert(0, x)
                sqr = math.sqrt(y)
                break
    for x in num2:
        sqr = sqr * x
    hasil.insert(0, sqr)
    return hasil

bo = []
print(bo.pop(0))

# x1 = ((b * -1) + countSq(a, b, c).pop(0))/ (2*a)
# x2 = ((b * -1) - countSq(a, b, c).pop(0))/ (2*a)


# print(x1)
# print(x2)

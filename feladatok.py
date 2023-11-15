import math
import random

"""
Írj eljárást, mely a paraméterben kap két egész számot ezen két szám közötti páros számok összegét számolja ki az eljárás
"""

def paros(min:int, max:int):
    i: int= min
    osszeadas: int = 0
    while i <= max:
        if i % 2 == 0:
            print(i)
            osszeadas += i
        i += 1
    ## visszatérési érték
    return osszeadas
    ## print(f"A páros számok összege: {osszeadas}")


def paros2(min:int, max:int):
    # i: int= min
    osszeadas: int = 0
    # while i <= b:
    for i in range(min, max, 1):
        if i % 2 == 0:
            print(i)
            osszeadas += i
        # i += 1
    ## visszatérési érték
    return osszeadas
    ## print(f"A páros számok összege: {osszeadas}")

"""
Írj függvényt, amely generál 20 db véletlen számot -10 és 10 között
Számold meg hány negatív szám van közötte
A visszatérési érték a negatív számok száma
"""

def negativ():
    i: int= 0
    negativok: int= 0
    while i < 20:
        szam: int= math.floor(random.random()* (10 + 1 -(-10)) + (-10))
        print(szam, end = ", ")
        if szam < 0:
            negativok += 1
        i += 1
    return negativok


def negativ2():
    # i: int= 0
    negativok: int= 0
    # while i < 20:
    for i in range(0, 20, 1):
        szam: int= math.floor(random.random()*21-10)
        print(szam, end = ", ")
        if szam < 0:
            negativok += 1
        # i += 1
    return negativok


"""
Írj függvényt, amely generál 10db véletlen számot,
[12, 33] között, és visszatér ezek összegével
"""

def osszeg():
    osszeadas: int= 0
    for i in range(0, 10, 1):
        szam: int= math.floor(random.random()*22+12)
        print(szam)
        osszeadas += szam
    return osszeadas


"""
Írj függvényt, amely generál 8db véletlen számot,
[20, 50) között, és visszatér ezek közül a legnagyobb számmal
"""

def osszeg2():
    max: int= 0
    for i in range(0, 8, 1):
        szam: int= math.floor(random.random()*30+20)
        print(szam)
        if szam > max:
            max = szam
    return max


"""
Kérjünk be 3 db egész számot a felhasználótól 
Mekkora a számok átlaga?
"""

def atlag():
    osszeg: int= 0
    for i in range(0, 3, 1):
        szam: int= int(input(f"Kérem az {i+1}. egész számot: "))
        print(szam)
        osszeg += szam
    return osszeg/3


"""
Kérjünk be egész számokat a felhasználótól, amíg 0-át nem ad!
Írjuk ki a számok átlagát!
"""

def atlag2():
    i: int= 0
    osszeg: int= 0
    db: int= 1
    szam: int= int(input(f"Kérem a(z) {i+1}. számot: "))
    while szam != 0:
        osszeg += szam
        szam: int= int(input(f"Kérem a(z) {i+1}. számot: "))
        db += 1
        i += 1
    return osszeg/(db-1)
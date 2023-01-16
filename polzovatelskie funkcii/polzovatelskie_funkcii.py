from math import *
from datetime import *
def arithmetic(a1:float, a2:float, sym:str):
    """Lihtne kalkulaator
    + liitmine, - lahutamine, * korrutamine, / jagamine
    :param float a1: Esimene arv
    :param float a2: Teine arv
    :param str sym: Tehe
    :rtype var: Maaramata tuup
    """
    if sym in ["+","-","*","/"]:
        if sym =="/" and a2==0:
            vas="Div/0"
        else:
            vas=eval(str(a1)+sym+str(a2))
    else:
        vas="tundmatu arv"
    return vas

def is_year_leap(b:int)->bool:
    """Opredelenie visokosnogo goda
    :param int b: aasta number
    :rtype: bool Funktsioni vastus loogilises formaadis
    """
    if b%4==0:
        t=True
        print("True")
    else:
        t=False
        print("False")
    return t

def square(a:float)->float:
    """Ruudu suuruste leidmine
    :param float a: ruudu kulg
    :rtype float P: ruudu umbermoot
    :rtype float S: ruudu pindala
    :rtype float d: ruudu diaameter
    """
    if a>=0:
        P=4*a
        S=a**2
        d=a*sqrt(2)
        return P, S, d
    else:
        print("Tq chto-to pereputal")
    return P, S, d

def season(s:int)->str:
    """Mis aastaaeg on
    :param int s: kuu number
    :rtype str: aastaaeg
    """
    if s in [12,1,2]:
        aeg='Talv'
    elif s in [3,4,5]:
        aeg='Kevad'
    elif s in [6,7,8]:
        aeg='Suvi'
    elif s in [9,10,11]:
        aeg='Sugis'
    else:
        print("Pole sellist kuud")
    return aeg

def bank(a:float,years:int)->float:
    """Tulu leidmine
    :param float a: summa vklada
    :param int years: vremja vklada
    :rtype float: summa vqvoda
    """
    while a>0 or years>0: 
        try:
            if a<0 and years<0:
                S=a*(1+0.1)**years
                
            else:
                print ("oshibka v dannqh")
                break
        except:
            ValueError


    
def is_prime(n:int)->bool:
    """Kas arv on lihtne?
    :param int n: arv mida on vaja kontrollida
    """
     
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_valid_date(day:int, month:int, year:int)->bool:
    """
    :param int day: paev
    :param int month: kuu
    :param int year: aasta
    """
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False
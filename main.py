#import random
# import time
#
# print("----------------------------")
# start_time = time.time()
# count = 0
# for i in range(10000000):
#     while True: #0,1666666666666667
#         dice = random.randint(1,6)
#         count +=1
#         # print(dice)
#         if dice == 6:
#             break
# print(f'meciau {count} kartu, kol iskrito 1000000 6tu. tikimybe yra {10000000 / count}')
# end_time = time.time()
# print(f'paskaiciavimams prireikė {(end_time - start_time)  } sekundžių')
import numbers
import random
import numpy as np
from dataclasses import replace
from ipaddress import v4_int_to_packed
from multiprocessing.resource_sharer import stop

print("-----------------pirmas-----------------")
labas = "labas"

# for z in enumerate(labas):
#     print(labas)

count = 1
while True:
    print(count, labas)
    count += 1
    if count == 11:
        break
print("------------------------antras---------------------------")

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in num:
    print(n)

print("-----------------------------trecias----------------------")

augalai = ['Ąžuolas', 'Beržas', 'Pušis', 'Klevas', 'Obelis', 'Rožė', 'Tulpė', 'Saulėgrąža', 'Ramunė', 'Papartis']
print(augalai)
print("--------------------------------ketvirtas----------------------------")
for a in augalai:
    print(a)

print("--------------------------------penktas----------------------------")
augalai.reverse()
for a in augalai:
    print(a)

print("-----------------------------------sestas-----------------------------")


for r in range(10,51):
    if r % 2 == 0:
        print(r)

print("------------------------------septintas---------------------------------")

for r in range(10,51):
    if r % 2 == 1 or r % 10 == 0:
        continue
    print(r)

print("-----------------------------astuntas-------------------------------------")
count = 0
for r in range(0,20):
    if r % 2 == 0:
        count += 1
        print(f"kelintas kartas:{count} skaiciai:{r}")

print("--------------------------------devintas----------------------------------")

augalai = ['Ąžuolas', 'Beržas', 'Pušis', 'Klevas', 'Obelis', 'Rožė', 'Tulpė', 'Saulėgrąža', 'Ramunė', 'Papartis']
count = 0
for a in augalai:
    if len(a) < 5:
        count += 1
        print(count, a)
print("maziau nei 5 ^^")
print("daugiau negu 7 ")
count = 0
for a in augalai:
    if len(a) > 7:
        count += 1
        print(count, a)

print("-------------------------------------desimtas-----------------------------")
augalai = ['Ąžuolas', 'Beržas', 'Pušis', 'Klevas', 'Obelis', 'Rožė', 'Tulpė', 'Saulėgrąža', 'Ramunė', 'Papartis']
count = 0
for a in augalai:
    if len(a) > 5 and len(a) <= 10:
        count += 1
        print(count, a, len(a))

print("------------------------------pirmas sunkesnis--------------------------------------")
#
# count150 = 0
# countnum = 0
#
# while True:
#     num = random.randint(0, 300)
#     print(num)
#     countnum += 1
#     if num > 150:
#         count150 += 1
#     if num > 275:
#         print(f"[{num}]")
#     if countnum == 300:
#         break
# print(num)
# print(f"zemiau 150 [{count150}]")
print("============================")


# count = 0
# count150 = 0
#
# while True:
#     num = random.randint(0, 300)
#     print(num)
#     count += 1
#     for nu in num:
#         if count == 300:
#             break
#         if nu > 150:
#             count150 += 1
#             print(nu)
#             if nu > 275:
#                     print(f"[{n}]")

count = 0
count150 = 0
while True:
    num = random.randint(0, 300)
    if num > 275:
        print(f"[{num}]",end = ' ')
    else:
        print(num, end = " ")
    if num > 150:
        count150 += 1
    count +=1
    if count == 300:
        break
print()


print("---------------------------------------antras sunkesnis-----------------------------------")

result = ""

for n in range(1, 3000):
    if n % 77 == 0:
        result += str(n) + ","

print(result.rstrip(","))

# result = ""
#
# for n in range(1, 3000):
#     if n % 77 == 0:
#         result += str(n) + ","
#
# print(result.rstrip(","))

print("--------------------------------trecias sunkesnis--------------------------------")


# count = 0
# zvaigzde = "*************************"

# while True:
#     count += 1
#     if range(1,25):
#         print(zvaigzde)
#         if count == 25:
#             break

# zvaigzde = "*"
#
#
# for c in range(0,26):
#     # print(zvaigzde, end= "")
#     print()
#     for v in range(0,26):
#         print(zvaigzde, end= "")
# print()

count = 0
z = "*"
for s in range(0,26):
    # print(z, end= " ")
    print()
    for v in range(0, 26):
        print(z, end="  ")

print()


print("------------------------------------ketvirta sunkesne---------------------------------")



print("---------------------------------------penkta sunkesne---------------------------------")
print("----------------a----------------------")
counth = 0
count = 0
counts = 0
while True:
    coin = random.randint(0, 2)
    if coin == 0:
        print("h")
        break
    else:
        print("s")
print("---------------b------------")
counth = 0
count = 0
counts = 0
while True:
    coin = random.randint(0, 2)
    if counth >= 3:
        break
    if coin == 0:
        counth += 1
        print("h")
    if coin == 1:
        print("s")
        counts += 1
    count += 1
print(f"herbu {counth}")
print(f"skaiciu {counts}")
print("------------------c---------------------")

count = 0

while True:
    coin = random.randint(0, 2)
    if count >= 3:
        break
    if coin == 0:
        count += 1
        print("h")
        if count >= 3:
            break
    if coin == 1:
        print("s")
        count = 0

print("--------------------------------------------sestas sunkesnis-------------------------------------")

petras = random.randint(10,20)
kazys = random.randint(5,25)
ptaskai = int()
ktaskai = int()
ptaskai1 = ""
print(f"petro taskai {petras}")
print(f"kazyio taskai {kazys}")
count = 0

while True:
   for i in range(0,100):
       petras = random.randint(10, 20)
       kazys = random.randint(5, 25)
       count += 1
       temp = petras
       temk = kazys
       if ptaskai >= 222 or ktaskai >= 222:
           break
       if ptaskai < 222:
           ptaskai = ptaskai + temp
       if ktaskai < 222:
           ktaskai = ktaskai + temk
           if ptaskai >= 222:
                print("Partiją laimėjo:Petas")
           elif ktaskai >= 222:
               print("Partija laimejo:Kazys")
       print(f"petro taskai {ptaskai}")
       print(f"kazyio taskai {ktaskai}")
   break

print("------------------------astuntas sunkesnis--------------------------------------")
print("------------a-------------------")

vi = 850
hitt = random.randint(5, 20)
count = 0
ikalti_vinis = 0
for c in range(0,60):
    ikalti_vinis +=1
    for v in range(0,1000):
        count += 1
        hitt = random.randint(5, 20)
        vi -= hitt
        if vi <= 0:
            break
    if ikalti_vinis == 6:
        break
    print(f"tikek smugiu {count} kad ikalt vini {ikalti_vinis} ")
print("--------------b--------------------------")


vi = 850
hitt = random.randint(20, 30)
hittchanse = random.randint(0, 1)
count = 0
ikalti_vinis = 0
countmiss = 0
for c in range(0,60):
    ikalti_vinis += 1
    for v in range(0,1000):
        count += 1
        hitt = random.randint(20, 30)
        hittchanse = random.randint(0, 1)
        if hittchanse == 1:
            vi -= hitt
        if hittchanse == 0:
            countmiss += 1
            continue
        if vi <= 0:
            break
    if ikalti_vinis == 6:
        break
    print(f"tikek smugiu {count} kad ikalt vini {ikalti_vinis} ir nepataikiau smugiu {countmiss} ")

print("-------------------------------devintas sunkesnis-------------------------------------------")

print("----------------------------MASIVAI----------------------------------------------------------")
print("------------------------------pirmas----------------------------------------------------------")

for d in range(0,30):
    b = random.randint(5, 25)
    print(d, b)

print("---------------------------------------antras----------------------------------------------")
print("-----------a-------------")
count = 0
for d in range(0,30):
    b = random.randint(5, 25)
    print(d, b)
    if b >= 10:
        count += 1
print(f"daugiu negu 10 yra {count}")

print("--------------b------------")
count = 0
result = ""
for d in range(0,30):
    b = random.randint(5, 25)
    result += str(b)
sorted = "".join(sorted(result))
print(sorted)
print("----------------c---------------")
print("---------------------------------------trecias---------------------------------------------")
counta = 0
countb = 0
countc = 0
countd = 0
a = random.randint(0, 3)
for v in range(0,200):
    a = random.randint(0, 3)
    if a == 0:
        print("a")
        counta += 1
    elif a == 1:
        print("b")
        countb += 1
    elif a == 2:
        print("c")
        countc += 1
    elif a == 3:
        print("d")
        countd += 1
print(f"a = {counta}, b = {countb}, c = {countc}, d = {countd}")
print("---------------------------ketvirtas---------------------------------------")

result = ""
a = random.randint(0, 3)
for _ in range(0,200):
    a = random.randint(0, 3)
    if a == 0:
        result += "a"
    elif a == 1:
        result+= "b"
    elif a == 2:
        result += "c"
    elif a == 3:
       result += "d"
sorted_result = "".join(sorted(result))
print(sorted_result)


print("-----------------------penktas-----------------------------------")


git config --global user.name "taucas2"
git config --global user.email "dovydastaucas123@gmail.com"
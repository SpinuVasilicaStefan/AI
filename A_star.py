import random
import time

def date_problema():
    m = input("Nr. de misionari: ")
    c = input("Nr. de  canibali: ")
    cb = input("Capacitatea barcii: ")
    return (m,c,cb)

def stare_initiala():
    pb = 1
    cb = int(date[2])
    m1 = int(date[0])
    m2 = 0
    c1 = int(date[1])
    c2 = 0
    return (pb,cb,m1,c1,m2,c2)

def stare_initiala_cu_parametrii(m, c, b):
    pb = 1
    cb = b
    m1 = m
    m2 = 0
    c1 = c
    c2 = 0
    return (pb,cb,m1,c1,m2,c2)

def verificare_stare_initiala(stare):
    if stare[3] > stare[2] or stare[1] <=0:
        return False
    else:
        return True

def stare_finala():
    pb = 2
    cb = int(date[2])
    m1 = 0
    m2 = int(date[0])
    c1 = 0
    c2 = int(date[1])
    return (pb, cb, m1, c1, m2, c2)

def stare_finala_cu_parametrii(m, c, b):
    pb = 2
    cb = b
    m1 = 0
    m2 = m
    c1 = 0
    c2 = c
    return (pb, cb, m1, c1, m2, c2)

def tranzitie(stare,m,c):
    return (3-stare[0],stare[1],stare[2]+m,stare[3]+c,stare[4]-m,stare[5]-c)

#daca m si c sunt negative mut de pe malul 1 pe 2, daca m si c - pozitive de pe 2 pe 1, in rest => invalid
def validare_tranzitie(stare,m,c):
    if stare[0] == 1:
        pb = 2
    else:
        pb = 1
    cb = stare[1]
    m1 = stare[2]+m
    c1 = stare[3]+c
    m2 = stare[4]-m
    c2 = stare[5]-c
    if c1 > m1 and m1 > 0:
        return False
    elif c2 > m2 and m2 > 0:
        return False
    elif abs(m) + abs(c) > cb:
        return False
    elif m==0 and c==0:
        return False
    elif (m+c)>0 and m >= 0 and c >= 0 and pb == 2:
        return False
    elif (m+c) < 0 and m <= 0 and c <= 0 and pb == 1:
        return False
    elif m1<0 or c1<0 or c2<0 or m2<0:
        return False
    elif m*c<0:
        return False
    else:
        return True



def strategia_random(stare):
    stari_anterioare = []
    stari_anterioare.append(stare)
    x = stare[1]
    m = stare[2]
    c = stare[3]
    contor = 0
    while stare != stare_finala_cu_parametrii(m, c, x):
        if contor == 1000:
            stare = stare_initiala_cu_parametrii(m, c, x)
            stari_anterioare = []
            contor = 0
        contor += 1
        m = random.randint((-1)*x,x)
        c = random.randint((-1)*x,x)
        if validare_tranzitie(stare,m,c) and (tranzitie(stare,m,c) not in stari_anterioare):
            stare = tranzitie(stare,m,c)
            stari_anterioare.append(stare)
    return stari_anterioare;

#strategia_random(stare_initiala())


def strategia_backtracking(stare):
    drumuri = []
    stare_precedenta = stare
    ok = 1
    flag = 0
    m1 = stare[2]
    c1 = stare[3]
    cb1 = stare[1]
    #print(stare_finala_cu_parametrii(m1, c1, cb1))
    while(ok):
        ok = 0
        if flag is 0:
            flag = 1
            if stare_precedenta[0] == 1:
                m = stare_precedenta[2]
                c = stare_precedenta[3]
            else:
                m = stare_precedenta[4]
                c = stare_precedenta[5]
            for i in range((-1)*m, m):
                for j in range((-1)*c, c):
                    if i + j <= stare_precedenta[1]:
                        if validare_tranzitie(stare_precedenta, i, j) :
                            ok = 1
                            drumuri.append([stare, tranzitie(stare_precedenta, i, j)])
        else:
            aux = []
            for k in range(0, len(drumuri)):
                stare_precedenta = drumuri[k][len(drumuri[k]) - 1]
                #print(stare_precedenta)
                if stare_precedenta[0] == 1:
                    m = stare_precedenta[2]
                    c = stare_precedenta[3]
                else:
                    m = stare_precedenta[4]
                    c = stare_precedenta[5]
                finalizat = 0
                for i in range((-1) * m, m + 1):
                    for j in range((-1) * c, c + 1):
                        if abs(i + j) <= stare_precedenta[1] and abs(i + j) > 0:
                            if validare_tranzitie(stare_precedenta, i, j) and tranzitie(stare_precedenta, i, j) not in  drumuri[k]:
                                ok = 1
                                aux.append(drumuri[k] + [tranzitie(stare_precedenta, i, j)])
                                #print(stare_precedenta)
                                if tranzitie(stare_precedenta, i, j) == stare_finala_cu_parametrii(m1,c1,cb1):
                                    return drumuri[k] + [tranzitie(stare_precedenta, i, j)]


            drumuri = aux.copy()
            for i in range(0, len(drumuri)):
                if stare_finala_cu_parametrii(m1,c1,cb1) in drumuri[i]:
                    return (drumuri[i])
                    ok = 0
                    break


ok = 0

def dfs(stare,stari_anterioare,adancime, m, c, cb):
    global ok
    stari_anterioare.append(stare)
    for m in range((-1)*stare[1],stare[1]+1):
        for c in range((-1)*stare[1],stare[1]+1):
            if validare_tranzitie(stare,m,c) and (tranzitie(stare,m,c) not in stari_anterioare) and ok == 0 and adancime>len(stari_anterioare):
                stare = tranzitie(stare,m,c)
                if stare == stare_finala_cu_parametrii(m,c,cb):
                    stari_anterioare.append(stare)
                    ok = 1
                    return
                dfs(stare,stari_anterioare,adancime,m, c, cb)

def strategia_iddfs(stare):
    m = stare[2]
    c = stare[3]
    cb = stare[1]
    adancime  = 1
    stari_anterioare = []
    #for i in range(0,adancime):
    while stare_finala_cu_parametrii(m,c,cb) not in stari_anterioare:
        adancime += 1
        stari_anterioare = []
        dfs(stare, stari_anterioare, adancime, m, c, cb)
        if stari_anterioare[len(stari_anterioare)-1] == stare_finala_cu_parametrii(m,c,cb):
            break
        if adancime>100:
            return "Nu am gasit!"
    if stare_finala_cu_parametrii(m,c,cb) in stari_anterioare:
        return stari_anterioare
    else:
        return []
#print(statistici())

def pasi_ramasi(stare):
    if stare[0] == 1:
        return int((stare[2] + stare[3]) / stare[1])
    else:
        return int((stare[2] + stare[3] + 1) / stare[1])

def pasi_ramasi2(stare):
    x =  min(stare[2],stare[3]) #perechi
    y = stare[2]-x
    return int((x+y)/stare[1])


def strategia_a_star(coada):
    vizitate = []
    vizitate_stari = []
    m1 =  coada[0][0][2]
    c1 =  coada[0][0][3]
    cb1 =  coada[0][0][1]
    while(coada != []):
        stare = coada[0][0]
        distanta = coada[0][1]
        drum = coada[0][2]
        coada = coada[1:]
        if stare not in vizitate_stari:
            vizitate_stari = vizitate_stari + [stare]
            vizitate = vizitate + [(stare, distanta, drum)]
            if stare[0] == 1:
                m = stare[2]
                c = stare[3]
            else:
                m = stare[4]
                c = stare[5]
            for i in range((-1)*m, m + 1):
                for j in range((-1)*c, c + 1):
                    if validare_tranzitie(stare, i, j) == True:
                        coada = coada + [(tranzitie(stare, i ,j), distanta - pasi_ramasi2(stare)  + 1 + pasi_ramasi2(tranzitie(stare, i, j)), drum + [stare])]
                        if tranzitie(stare, i, j) == stare_finala_cu_parametrii(m1, c1, cb1):
                            return drum + [stare] + [tranzitie(stare, i ,j)]

        vizitate.sort(key=lambda x: x[1])
    return vizitate

def statistici_finala():
    medie__timp_random = 0
    medie_lungime_random = 0
    medie__timp_iddfs = 0
    medie_lungime_iddfs = 0
    medie__timp_bkt = 0
    medie_lungime_bkt = 0
    medie__timp_a_star = 0
    medie_lungime_a_star = 0
    contor = 10
    while(contor > 0):
        print(contor)
        contor = contor - 1
        ok = 0
        while ok == 0:
            print("59")
            m = random.randint(3, 15)
            c = random.randint(3, 15)
            b = random.randint(2, 5)
            if verificare_stare_initiala(stare_initiala_cu_parametrii(m,c, b)) is True:
                ok = 1
        print((m,c, b))
        stare = stare_initiala_cu_parametrii(m,c, b)

        start_time = time.time()
        rezultat = strategia_random(stare)
        print("random")
        print(time.time() - start_time)
        medie__timp_random = medie__timp_random + (time.time() - start_time)
        medie_lungime_random = medie_lungime_random + len(rezultat)


        #a_star
        start_time = time.time()
        rezultat = strategia_a_star([(stare, 0, [])])
        print("a*")
        print(time.time() - start_time)
        medie__timp_a_star = medie__timp_a_star + (time.time() - start_time)
        medie_lungime_a_star = medie_lungime_a_star + len(rezultat)


        #iddfs
        start_time = time.time()
        rezultat = strategia_iddfs(stare)
        print("iddfs")
        print(time.time() - start_time)
        print( rezultat )
        medie__timp_iddfs = medie__timp_iddfs + (time.time() - start_time)
        medie_lungime_iddfs = medie_lungime_iddfs + len(rezultat)


        #bkt
        #start_time = time.time()
        #rezultat = strategia_backtracking(stare)
        #print("bkt")
        #print(time.time() - start_time)
        #print(rezultat)
        #medie__timp_bkt = medie__timp_bkt + (time.time() - start_time)
        #medie_lungime_bkt = medie_lungime_bkt + len(rezultat)
    return (float(medie_lungime_random / 10 ), medie__timp_random / 10)

def statistici_iddfs():
    medie__timp_iddfs = 0
    medie_lungime_iddfs = 0
    contor = 10
    while(contor > 0):
        contor = contor - 1

        ok = 0
        while ok == 0:
            m = random.randint(3, 15)
            c = random.randint(3, 15)
            b = random.randint(2, 5)
            if verificare_stare_initiala(stare_initiala_cu_parametrii(m,c, b)) is True:
                ok = 1
        print((m,c, b))
        stare = stare_initiala_cu_parametrii(m,c, b)
        start_time = time.time()
        rezultat = strategia_iddfs(stare)
        print(time.time() - start_time)
        print(rezultat)
        medie__timp_iddfs = medie__timp_iddfs + (time.time() - start_time)
        medie_lungime_iddfs = medie_lungime_iddfs + len(rezultat)
    return (float(medie_lungime_iddfs / 10 ), medie__timp_iddfs)

def statistici_backtracking():
    medie__timp_bkt = 0
    medie_lungime_bkt = 0
    contor = 10
    while(contor > 0):
        contor = contor - 1
        ok = 0
        while ok == 0:
            m = random.randint(3, 15)
            c = random.randint(3, 15)
            b = random.randint(2, 5)
            if verificare_stare_initiala(stare_initiala_cu_parametrii(m,c, b)) is True:
                ok = 1
        print((m,c, b))
        stare = stare_initiala_cu_parametrii(m,c, b)
        print(stare)
        start_time = time.time()
        rezultat = strategia_backtracking(stare)
        print(time.time() - start_time)
        print(rezultat)
        medie__timp_bkt = medie__timp_bkt + (time.time() - start_time)
        medie_lungime_bkt = medie_lungime_bkt + len(rezultat)
    return (float(medie_lungime_bkt / 10 ), medie__timp_bkt)


def statistici_a_star():
    medie__timp_bkt = 0
    medie_lungime_bkt = 0
    contor = 10
    while(contor > 0):
        contor = contor - 1
        ok = 0
        while ok == 0:
            m = random.randint(3, 15)
            c = random.randint(3, 15)
            b = random.randint(2, 5)
            if verificare_stare_initiala(stare_initiala_cu_parametrii(m,c, b)) is True:
                ok = 1
        print((m,c, b))
        stare = stare_initiala_cu_parametrii(m,c, b)
        print(stare)
        start_time = time.time()
        rezultat = strategia_a_star([(stare, 0,[])])
        print(time.time() - start_time)
        print(rezultat)
        medie__timp_bkt = medie__timp_bkt + (time.time() - start_time)
        medie_lungime_bkt = medie_lungime_bkt + len(rezultat)
    return (float(medie_lungime_bkt / 10 ), medie__timp_bkt)


#print(strategia_a_star([(stare_initiala(), 0,[])]))

print(statistici_finala())








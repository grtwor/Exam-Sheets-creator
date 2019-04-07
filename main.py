
import random


def los(L, rand, tmp):
    while True:
        x = L[random.choice([i for i in range(0, len(L)) if i != rand])][1]
        if x not in tmp:
            tmp.append(x)
            break
    return x


def open_file(x):
    L = []
    txt_file = open(x, 'r')
    lines_count = len(txt_file.readlines())
    txt_file.seek(0)
    for item in range(lines_count):
        line = txt_file.readline()
        line = line.rstrip()
        word = line.split(',')
        L.append(word)
    txt_file.close()
    return L



L = open_file('stolice.txt')

print("Ile Formularzy chcesz utworzyć: ", end='')
numbers = input()
numbers = int(numbers)

for form in range(1,numbers + 1):

    spr = 'sprawdzian %d.txt' % form
    odp = 'odpowiedzi %d.txt' % form
    sprawdzian = open(spr, 'w+')
    odpowiedzi = open(odp, 'w+')

    country = []
    cp_L = L[:]
    switch = 0
    tmp = []

    sprawdzian.write("Imie i nazwisko:\n\nData:\n\nSemestr:\n\t\t\tStolice - sprawdzian (Formularz %d)" % form)
    for i in range(0,len(L)):
        while switch:
            rand = random.randint(0,len(cp_L) - 1)
            if L[rand] not in country:
                print("%d Jaka stolice ma panstwo %s: " % (i, L[rand][0]), file=sprawdzian)
                country.append(L[rand])
                switch = 0
                set_on = random.randint(0,3)

                if set_on == 0:
                    print("\tA. ", L[rand][1], file=sprawdzian)
                    print("%d. A" % i, file=odpowiedzi)
                else:
                    print("\tA. ", los(L, rand, tmp), file=sprawdzian)


                if set_on == 1:
                    print("\tB. ", L[rand][1], file=sprawdzian)
                    print("%d. B" % i, file=odpowiedzi)
                else:
                    print("\tB. ", los(L, rand, tmp), file=sprawdzian)


                if set_on == 2:
                    print("\tC. ", L[rand][1], file=sprawdzian)
                    print("%d. C" % i, file=odpowiedzi)
                else:
                    print("\tC. ", los(L, rand, tmp), file=sprawdzian)


                if set_on == 3:
                    print("\tD. ", L[rand][1], file=sprawdzian)
                    print("%d. D" % i, file=odpowiedzi)
                else:
                    print("\tD. ", los(L, rand, tmp), file=sprawdzian)

        print('\n', file=sprawdzian)
        tmp = []
        switch = 1




    odpowiedzi.close()
    sprawdzian.close()

print("Pomyślnie utworzono %d formularzy!" % numbers)

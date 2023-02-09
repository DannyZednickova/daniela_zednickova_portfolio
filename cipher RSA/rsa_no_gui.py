import math

from mpmath.libmp.backend import xrange
import random
import numpy as np
import unicodedata
def miller_rabin(n, k=4):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True




pcko = 0
qcko = 0
Fi = 0
nko = 0
ecko = 0
dcko = 0
while miller_rabin(pcko) == False:
    pcko = random.randint(10 ** 18, 10 ** 19 - 1)
while miller_rabin(qcko) == False or pcko == qcko:
    qcko = random.randint(10 ** 18, 10 ** 19 - 1)
nko = pcko * qcko
print("nko", nko)
Fi = (pcko - 1) * (qcko - 1)
ecko = random.randint(1, Fi)
while math.gcd(ecko, Fi) != 1:
    ecko = random.randint(1, Fi)
print("ecko", ecko)
dcko = pow(ecko, -1, Fi)
print("dcko", dcko)


nko = 31899742020626236821590379905597924473
dcko = 2633725140919603666094362476201995477
ecko = 17627198273146631234510581261630459501


text = "Ahoj jak se mas"
#print(text)




def filter_text(text):
    text =  ''.join(c for c in unicodedata.normalize('NFD', text)
                  if unicodedata.category(c) != 'Mn')
    return text

text = filter_text(text)


def list_of_binaries(text):
    text_asci = []
    tmp = []
    for char in text:
        text_asci.append((ord(char)))  # prevadi do asci

    #print(text_asci)
    tmp = []
    for char in range(len(text_asci)):
        #print(text_asci[char])
        binar = (bin(text_asci[char])[2:].zfill(8))
        tmp.append(binar)
    n = 8
    l = tmp
    matrix = [l[i:i + n] for i in xrange(0, len(l), n)]
    print("Chary prevedene na binary:",matrix)
    return matrix


list_of_bin = list_of_binaries(text)


def full_fill_list(list_of_bin):
    colum_num = len(list_of_bin)
    # print(colum_num)
    # print(list_of_bin[colum_num - 1])
    # print(len(list_of_bin[colum_num - 1]))
    while len(list_of_bin[colum_num - 1]) != 8:
        list_of_bin[colum_num - 1].append('00000000')
    #print(list_of_bin)

    return list_of_bin


list_of_bin = (full_fill_list(list_of_bin))

list_of_bin = np.array(list_of_bin)


# print(list_of_bin)


def make_huge_number(list_of_bin):
    row_count = len(list_of_bin)

    longbin = ""
    list_of_long_bins = []
    #print(list_of_bin[0])

    for bins in range(row_count):
        longbin = ''.join([str(x) for x in list_of_bin[bins]])
        list_of_long_bins.append(longbin)

    #print("Velke binarni cislo:",list_of_long_bins)
    long_list_of_decimal = []
    for bins in range(len(list_of_long_bins)):
        dec = int(list_of_long_bins[bins], 2)
        long_list_of_decimal.append(dec)
    #print("Velke dec cislo z binaru:",long_list_of_decimal)

    return long_list_of_decimal


huge_number = make_huge_number(list_of_bin)
print("huge number", huge_number)



def cipher_math(huge_number, e, n):
    final = []
    for num in range(len(huge_number)):
        final.append(pow(huge_number[num], e, n))

    final_string = ''.join(map(str, final))
    return final_string


#print(cipher_math(huge_number,ecko,nko))



final_list_cipher = cipher_math(huge_number, ecko, nko)
print("Finalni sifra po matice:",final_list_cipher)



final_string = ''.join(map(str, final_list_cipher))
n = 40
split = [int(final_string[idx:idx + n]) for idx in range(0, len(final_string), n)]
#print("Splite: ",split)






def decpher_math(final_list_cipher, d, n):
    final = []
    for num in range(len(final_list_cipher)):
        final.append(pow(final_list_cipher[num], d, n))

    return final





def decipher(final_string, dcko, nko):
    final_string = ''.join(map(str, final_string))
    n = 40
    split = [int(final_string[idx:idx + n]) for idx in range(0, len(final_string), n)]

    decipher_first = decpher_math(split, dcko, nko)
    #print(decipher_first)
    #print(decipher_first)
    tmp = []
    for numbers in range(len(decipher_first)):
        #print(decipher_first[numbers])
        tmp.append(bin(decipher_first[numbers])[2:].zfill(8))

    #print(tmp)
    count = 0
    list_of_full_bin = []
    for i in range(len(tmp)):
        for intgr in tmp[i]:
            count += 1
        while len(tmp[i]) != 64:
            tmp[i] = "0" + tmp[i]
        list_of_full_bin.append(tmp[i])
        count = 0

    #print(list_of_full_bin)
    listik = list_of_full_bin

    list_of_bins_decode = []

    for i in range(len(listik)):

        cislo = listik[i]
        list_of_bins_decode.append( [cislo [i:i+8] for i in range(0, len(cislo ), 8)])


    #print(len(list_of_bins_decode))

    asci = []
    for integer in range(len(list_of_bins_decode)):
        for i in range(8):
            if list_of_bins_decode[integer][i] == "00000000":
                continue
            #print(list_of_bins_decode[integer][i])
            asci.append( int(list_of_bins_decode[integer][i],2))


    string = ''
    for nums in range(len(asci)):
        string += chr(asci[nums])

    return string



print(decipher(split,dcko,nko))

#print(decipher("1614388833626250398238696937324474383",993215358379418856342256699573896619,5772274718974858270031335227789574259))

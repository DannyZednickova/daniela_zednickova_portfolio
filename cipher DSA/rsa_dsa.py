import math
from mpmath.libmp.backend import xrange
import random
import unicodedata
def miller_rabin(n, k=4):
    """
    Miller rabin  an algorithm which determines whether a given number is likely to be prime.
    """
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


def generate_keys():
    """
    This function generates keys - public and private key.
    """
    pcko = 0
    qcko = 0
    while miller_rabin(pcko) is False:
        pcko = random.randint(10 ** 19, 10 ** 20 - 1)
    while miller_rabin(qcko) is False or pcko == qcko:
        qcko = random.randint(10 ** 19, 10 ** 20 - 1)
    nko = pcko * qcko
    Fi = (pcko - 1) * (qcko - 1)
    ecko = random.randint(1, Fi) #verejny
    while math.gcd(ecko, Fi) != 1:
        ecko = random.randint(1, Fi)

    dcko = pow(ecko, -1, Fi) #privatni
    return nko,dcko,ecko



generovani = generate_keys()                   #hodnoty jsou zadany pro testovani fixne!
nko = 4831367096030430613379032405160958223447#  generovani[0]
#print("nko",nko)
dcko = 782737812411892346527126054710098736121# generovani[1] #
# print("Tohle je privatni klic, kterym se sifruje: ",dcko) #privatni
ecko = 1579651202565084150106683771097796942553 # generovani[2]
# print("Tohle je verejny klic, kterym se desifruje: ",ecko) #verejny

def filter_text(text):
    text =  ''.join(c for c in unicodedata.normalize('NFD', text)
                  if unicodedata.category(c) != 'Mn')
    return text


open_text = "02253a2ea27a32e7957c2f271822e09180a442f3c27fcec448ca2c1cd8d"

def cipher_func(open_text):
    """
    This funcion is main function that takes an open text , divide it into 8 chars, makes
    matrix with this 8 chars in one and  turns it into asci and then binary. It basically typical RSA algorithm.
    :param open_text:
    :return long list of decimal:
    """
    text_asci = []
    for char in open_text:
        text_asci.append((ord(char)))  # prevadi do asci
    tmp = []
    for char in range(len(text_asci)):
        binar = (bin(text_asci[char])[2:].zfill(8))
        tmp.append(binar)
    n = 8
    l = tmp
    matrix = [l[i:i + n] for i in xrange(0, len(l), n)]
    colum_num = len(matrix)
    while len(matrix[colum_num - 1]) != 8:
        matrix[colum_num - 1].append('00000000')
    row_count = len(matrix)

    list_of_long_bins = []

    for bins in range(row_count):
        longbin = ''.join([str(x) for x in matrix[bins]])
        list_of_long_bins.append(longbin)

    long_list_of_decimal = []
    for bins in range(len(list_of_long_bins)):
        dec = int(list_of_long_bins[bins], 2)
        long_list_of_decimal.append(dec)
    return long_list_of_decimal


def cipher_math(huge_number,key_e,n):
    """
    RSA math - basic math funciton takes huge number, public key and "n" and cipeher varied open text.
    :param huge_number:
    :param key_e:
    :param n:
    :return final_strings:
    """
    final = []
    for num in range(len(huge_number)):
        final.append(pow(huge_number[num], key_e, n))

    final_strings = ' '.join(str(item) for item in final)
    return final_strings


def decpher_math(cipher_final_str, key_d, n):
    list_of_strings = cipher_final_str.split(' ')
    list_of_integers = list(map(int, list_of_strings))
    final = []
    for num in range(len(list_of_integers)):
        final.append(pow(list_of_integers[num], key_d, n))
    return final


def decipher_func(decipher_after_math):
    bin_list = []
    for num in range(len(decipher_after_math)):
        dec_string = bin(decipher_after_math[num])
        dec_string = str(dec_string)
        dec_string = dec_string.replace("b","")
        while len(dec_string) != 64:
            dec_string = "0" + dec_string
        bin_list.append(dec_string)

    list_of_bins_eights = []
    for i in range(len(bin_list)):
        cislo = bin_list[i]
        list_of_bins_eights.append( [cislo [i:i+8] for i in range(0, len(cislo ), 8)])

    asci = []
    for integer in range(len(list_of_bins_eights)):
        for i in range(8):
            if list_of_bins_eights[integer][i] == "00000000":
                continue
            # print(list_of_bins_decode[integer][i])
            asci.append(int(list_of_bins_eights[integer][i], 2))

    ot_deciphered = ''
    for nums in range(len(asci)):
        ot_deciphered += chr(asci[nums])

    return ot_deciphered

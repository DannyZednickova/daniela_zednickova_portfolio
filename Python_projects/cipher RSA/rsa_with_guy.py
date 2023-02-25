from mpmath.libmp.backend import xrange
from sympy import randprime, totient
from math import gcd
from random import randint
import random
import unicodedata

from PyQt5 import QtCore, QtGui, QtWidgets


def list_of_binaries(text):
    text_asci = []
    tmp = []
    for char in text:
        text_asci.append((ord(char)))  # prevadi do asci

    # print(text_asci)
    tmp = []
    for char in range(len(text_asci)):
        # print(text_asci[char])
        binar = (bin(text_asci[char])[2:].zfill(8))
        tmp.append(binar)
    n = 8
    l = tmp
    matrix = [l[i:i + n] for i in xrange(0, len(l), n)]
    print("Chary prevedene na binary:", matrix)
    return matrix


def full_fill_list(list_of_bin):
    colum_num = len(list_of_bin)
    while len(list_of_bin[colum_num - 1]) != 8:
        list_of_bin[colum_num - 1].append('00000000')
    print(list_of_bin)
    return list_of_bin



def make_huge_number(list_of_bin):
    row_count = len(list_of_bin)
    list_of_long_bins = []


    for bins in range(row_count):
        longbin = ''.join([str(x) for x in list_of_bin[bins]])
        list_of_long_bins.append(longbin)

    print("Velke binarni cislo:", list_of_long_bins)
    long_list_of_decimal = []
    for bins in range(len(list_of_long_bins)):
        dec = int(list_of_long_bins[bins], 2)
        long_list_of_decimal.append(dec)
    print("Velke dec cislo z binaru:", long_list_of_decimal)

    return long_list_of_decimal


def cipher_math(huge_number, e, n):
    final = []
    for num in range(len(huge_number)):
        final.append(pow(huge_number[num], e, n))

    final_string = ' '.join(map(str, final))
    return final_string


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
    tmp = []
    for numbers in range(len(decipher_first)):
        tmp.append(bin(decipher_first[numbers])[2:].zfill(8))
    count = 0
    list_of_full_bin = []
    for i in range(len(tmp)):
        for intgr in tmp[i]:
            count += 1
        while len(tmp[i]) != 64:
            tmp[i] = "0" + tmp[i]
        list_of_full_bin.append(tmp[i])
        count = 0

    listik = list_of_full_bin

    list_of_bins_decode = []

    for i in range(len(listik)):
        cislo = listik[i]
        list_of_bins_decode.append([cislo[i:i + 8] for i in range(0, len(cislo), 8)])
    asci = []
    for integer in range(len(list_of_bins_decode)):
        for i in range(8):
            if list_of_bins_decode[integer][i] == "00000000":
                continue

            asci.append(int(list_of_bins_decode[integer][i], 2))

    string = ''
    for nums in range(len(asci)):
        string += chr(asci[nums])

    return string


def filter_text(text):
    text = ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')
    return text


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


class Ui_Form(object):

    def check_input_cipher(self):
        try:
            self.E = int(self.VerejnyKlic.text())
            self.D = int(self.PrivatniKlic.text())
            self.N = int(self.nklic.text())
        except:
            self.warning_2.setText("Tohle nejde")
            return True
        return False

    def check_input_decipher(self):
        try:
            self.E = int(self.VerejnyKlic.text())
            self.D = int(self.PrivatniKlic.text())
            self.N = int(self.nklic.text())
        except:
            self.warning_2.setText("Tohle nejde")
            return True
        return False

    def generate_key(self):
        p = 0
        q = 0
        # 1
        while miller_rabin(p) == False:
            p = randprime(10 ** 19, (10 ** 20) - 1)  # generuje dostatecne velke prvocislo
        while miller_rabin(q) == False:
            q = randprime(10 ** 19, (10 ** 20) - 1)
        while q == p:
            q = randprime(10 ** 19, (10 ** 20) - 1)
        n = p * q
        fi_n = (p - 1) * (q - 1)  #
        e = randint(1, fi_n)
        while gcd(e, fi_n) != 1:
            e = randint(1, fi_n)  ## public key
        d = pow(e, -1, fi_n)  # private key

        self.E = e
        self.D = d
        self.N = n

        self.nklic.setText(str(self.N))
        self.VerejnyKlic.setText(str(self.E))
        self.PrivatniKlic.setText(str(self.D))

    def restart_button(self):
        self.nklic.setText("")
        self.VerejnyKlic.setText("")
        self.PrivatniKlic.setText("")
        self.otevrenyText.setText("")
        self.SifrovanText.setText("")
        self.warning_2.setText("")

    def Sifruj(self, key):

        ot = str(self.otevrenyText.text().strip())
        if ot == "":
            self.warning_2.setText("Neco je spatne...")
        else:
            ot = filter_text(ot)
            listOfBin = list_of_binaries(ot)
            fullListOfBins = full_fill_list(listOfBin)
            huge_number = make_huge_number(fullListOfBins)
            final_cipher = cipher_math(huge_number, self.E, self.N)
            self.final = final_cipher
            print(final_cipher)
            self.warning_3.setText(final_cipher)
            self.SifrovanText.setText(final_cipher)

    def Desifr(self):
        ct = self.final
        deciphered = decipher(ct, self.D, self.N)
        self.warning_2.setText(deciphered)
        self.SifrovanText.setText(deciphered)

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(993, 892)
        Form.setStyleSheet("background-color:rgb(36, 41, 50)\n"
                           "")
        self.VerejnyKlic = QtWidgets.QLineEdit(Form)
        self.VerejnyKlic.setGeometry(QtCore.QRect(20, 90, 441, 51))
        self.VerejnyKlic.setStyleSheet("QLineEdit {\n"
                                       "border:1px solid white;\n"
                                       "border-radius: 20px;\n"
                                       "border-radius: 20px;\n"
                                       "color: #FFF;\n"
                                       "padding-left:10px;\n"
                                       "padding-right: 10px;\n"
                                       "padding-top:10px;\n"
                                       "padding-bottom:10px;\n"
                                       "\n"
                                       "\n"
                                       "}")
        self.VerejnyKlic.setObjectName("VerejnyKlic")
        self.PrivatniKlic = QtWidgets.QLineEdit(Form)
        self.PrivatniKlic.setGeometry(QtCore.QRect(500, 90, 441, 51))
        self.PrivatniKlic.setStyleSheet("QLineEdit {\n"
                                        "border:1px solid white;\n"
                                        "border-radius: 20px;\n"
                                        "color: #FFF;\n"
                                        "padding-left:10px;\n"
                                        "padding-right: 10px;\n"
                                        "padding-top:10px;\n"
                                        "padding-bottom:10px;\n"
                                        "\n"
                                        "\n"
                                        "}")
        self.PrivatniKlic.setObjectName("PrivatniKlic")
        self.GenerovatKlice = QtWidgets.QPushButton(Form)
        self.GenerovatKlice.setGeometry(QtCore.QRect(390, 240, 221, 41))
        self.GenerovatKlice.setStyleSheet("QPushButton{\n"
                                          "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                          "    color:rgb(148, 148, 148);\n"
                                          "    border-radius: 20px;\n"
                                          "    border: 1px solid rgb(148, 148, 148);\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    color:rgb(255, 255, 255);\n"
                                          "\n"
                                          "}")
        self.GenerovatKlice.setObjectName("GenerovatKlice")
        self.GenerovatKlice.clicked.connect(self.generate_key)
        self.labelVerejnyKlic = QtWidgets.QLabel(Form)
        self.labelVerejnyKlic.setGeometry(QtCore.QRect(30, 60, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelVerejnyKlic.setFont(font)
        self.labelVerejnyKlic.setStyleSheet("QLabel{\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "}")
        self.labelVerejnyKlic.setObjectName("labelVerejnyKlic")
        self.labelPrivatniKlic = QtWidgets.QLabel(Form)
        self.labelPrivatniKlic.setGeometry(QtCore.QRect(520, 60, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelPrivatniKlic.setFont(font)
        self.labelPrivatniKlic.setStyleSheet("QLabel{\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "}")
        self.labelPrivatniKlic.setObjectName("labelPrivatniKlic")
        self.otevrenyText = QtWidgets.QLineEdit(Form)
        self.otevrenyText.setGeometry(QtCore.QRect(30, 300, 931, 81))
        self.otevrenyText.setStyleSheet("QLineEdit {\n"
                                        "\n"
                                        "border:1px solid white;\n"
                                        "border-radius: 20px;\n"
                                        "color: #FFF;\n"
                                        "padding-left:10px;\n"
                                        "padding-right: 10px;\n"
                                        "padding-top:10px;\n"
                                        "padding-bottom:10px;\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "}")
        self.otevrenyText.setText("")
        self.otevrenyText.setObjectName("otevrenyText")
        self.SifrovanText = QtWidgets.QLineEdit(Form)
        self.SifrovanText.setGeometry(QtCore.QRect(30, 440, 931, 81))
        self.SifrovanText.setStyleSheet("QLineEdit {\n"
                                        "\n"
                                        "border:1px solid white;\n"
                                        "border-radius: 20px;\n"
                                        "color: #FFF;\n"
                                        "padding-left:10px;\n"
                                        "padding-right: 10px;\n"
                                        "padding-top:10px;\n"
                                        "padding-bottom:10px;\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "}")
        self.SifrovanText.setText("")
        self.SifrovanText.setObjectName("SifrovanText")
        self.sifrovatButton = QtWidgets.QPushButton(Form)
        self.sifrovatButton.setGeometry(QtCore.QRect(190, 530, 261, 41))
        self.sifrovatButton.setStyleSheet("QPushButton{\n"
                                          "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                          "    color:rgb(148, 148, 148);\n"
                                          "    border-radius: 20px;\n"
                                          "    border: 1px solid rgb(148, 148, 148);\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    color:rgb(255, 255, 255);\n"
                                          "\n"
                                          "}")
        self.sifrovatButton.setObjectName("sifrovatButton")
        self.sifrovatButton.clicked.connect(self.Sifruj)
        self.desifrovatButton = QtWidgets.QPushButton(Form)
        self.desifrovatButton.setGeometry(QtCore.QRect(520, 530, 241, 41))
        self.desifrovatButton.setStyleSheet("QPushButton{\n"
                                            "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                            "    color:rgb(148, 148, 148);\n"
                                            "    border-radius: 20px;\n"
                                            "    border: 1px solid rgb(148, 148, 148);\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    color:rgb(255, 255, 255);\n"
                                            "\n"
                                            "}")
        self.desifrovatButton.setObjectName("desifrovatButton")
        self.desifrovatButton.clicked.connect(self.Desifr)
        self.labelPrivatniKlic_2 = QtWidgets.QLabel(Form)
        self.labelPrivatniKlic_2.setGeometry(QtCore.QRect(30, 270, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelPrivatniKlic_2.setFont(font)
        self.labelPrivatniKlic_2.setStyleSheet("QLabel{\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "}")
        self.labelPrivatniKlic_2.setObjectName("labelPrivatniKlic_2")
        self.labelPrivatniKlic_3 = QtWidgets.QLabel(Form)
        self.labelPrivatniKlic_3.setGeometry(QtCore.QRect(30, 400, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelPrivatniKlic_3.setFont(font)
        self.labelPrivatniKlic_3.setStyleSheet("QLabel{\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "}")
        self.labelPrivatniKlic_3.setObjectName("labelPrivatniKlic_3")
        self.nadpis = QtWidgets.QLabel(Form)
        self.nadpis.setGeometry(QtCore.QRect(360, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.nadpis.setFont(font)
        self.nadpis.setStyleSheet("QLabel{\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}")
        self.nadpis.setObjectName("nadpis")
        self.restartButton = QtWidgets.QPushButton(Form)
        self.restartButton.setGeometry(QtCore.QRect(360, 840, 221, 41))
        self.restartButton.setStyleSheet("QPushButton{\n"
                                         "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                         "    color:rgb(148, 148, 148);\n"
                                         "    border-radius: 20px;\n"
                                         "    \n"
                                         "    background-color: rgb(213, 20, 78);\n"
                                         "    border: 1px solid rgb(148, 148, 148);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    color:red;\n"
                                         "\n"
                                         "}")
        self.restartButton.setObjectName("restartButton")
        self.restartButton.clicked.connect(self.restart_button)
        self.warning_2 = QtWidgets.QLabel(Form)
        self.warning_2.setGeometry(QtCore.QRect(30, 600, 911, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.warning_2.setFont(font)
        self.warning_2.setStyleSheet("QLabel {\n"
                                     "color: rgb(153, 227, 113);\n"
                                     "}")
        self.warning_2.setObjectName("warning_2")
        self.warning_3 = QtWidgets.QLabel(Form)
        self.warning_3.setGeometry(QtCore.QRect(30, 670, 911, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.warning_3.setFont(font)
        self.warning_3.setStyleSheet("QLabel {\n"
                                     "color: rgb(153, 227, 113);\n"
                                     "}")
        self.warning_3.setObjectName("warning_3")
        self.nklic = QtWidgets.QLineEdit(Form)
        self.nklic.setGeometry(QtCore.QRect(280, 180, 441, 51))
        self.nklic.setStyleSheet("QLineEdit {\n"
                                 "border:1px solid white;\n"
                                 "border-radius: 20px;\n"
                                 "color: #FFF;\n"
                                 "padding-left:10px;\n"
                                 "padding-right: 10px;\n"
                                 "padding-top:10px;\n"
                                 "padding-bottom:10px;\n"
                                 "\n"
                                 "\n"
                                 "}")
        self.nklic.setObjectName("nklic")
        self.labelPrivatniKlic_4 = QtWidgets.QLabel(Form)
        self.labelPrivatniKlic_4.setGeometry(QtCore.QRect(290, 150, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelPrivatniKlic_4.setFont(font)
        self.labelPrivatniKlic_4.setStyleSheet("QLabel{\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "}")
        self.labelPrivatniKlic_4.setObjectName("labelPrivatniKlic_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.GenerovatKlice.setText(_translate("Form", "GENEROVAT KLÍČE"))
        self.labelVerejnyKlic.setText(_translate("Form", "Veřejný klíč"))
        self.labelPrivatniKlic.setText(_translate("Form", "Privátní klíč"))
        self.sifrovatButton.setText(_translate("Form", "ŠIFROVAT"))
        self.desifrovatButton.setText(_translate("Form", "DEŠIFROVAT"))
        self.labelPrivatniKlic_2.setText(_translate("Form", "Otevřený text"))
        self.labelPrivatniKlic_3.setText(_translate("Form", "Šifrovaný text"))
        self.nadpis.setText(_translate("Form", "RSA ŠIFRA - DRÁBKOVÁ"))
        self.restartButton.setText(_translate("Form", "RESTARTOVAT"))
        self.warning_2.setText(_translate("Form", ""))
        self.warning_3.setText(_translate("Form", ""))
        self.labelPrivatniKlic_4.setText(_translate("Form", "Člen N"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

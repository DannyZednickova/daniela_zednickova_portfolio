import hashlib
import time
import rsa_dsa
import os
from os.path import basename
import zipfile
import base64
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox


class Ui_Form(QMainWindow):

    def load_message(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*)", options=options)
        self.hashed_line = ""
        if fileName:
            # print(fileName)
            self.path_of_message = fileName
            self.name_of_message = os.path.basename(fileName)
            file_size = str(os.path.getsize(fileName))
            file_name = os.path.basename(fileName)
            modified = os.path.getmtime(fileName)
            time_modified = time.ctime(modified)

            with open(fileName, 'rb') as f:
                self.label_nazev.setText(file_name)
                self.label_cesta.setText(fileName)
                self.label_velikost.setText(file_size)
                self.label_datum_uprav.setText(time_modified)
                lines = f.readlines()
                for line in lines:
                    print(line)
                    self.hashed_line = hashlib.sha256(line.rstrip()).hexdigest()
        print(self.hashed_line)

    def generate_keys(self):
        try:
            path_message = self.path_of_message
            name_message = self.name_of_message
            path_message = path_message.replace(name_message, "")
            # print(path_message)

            generovani = rsa_dsa.generate_keys()
            self.nko = generovani[0]
            self.dcko = generovani[1]  # private - SIFROVANI
            self.ecko = generovani[2]  # PUBLIC - desifrovani

            try:
                # os.mkdir(path_message)
                save_key_private = open(path_message + "private.priv", "w")
                save_key_private.write(str(self.dcko))
                save_key_private.write("\n")
                save_key_private.write(str(self.nko))
                save_key_private.close()

                save_key_public = open(path_message + "public.publ", "w")
                save_key_public.write(str(self.ecko))
                save_key_public.write("\n")
                save_key_public.write(str(self.nko))
                save_key_public.close()
            except:
                self.label_podepsano.setText("Něco se nepovedlo pči generování klíče!")
                QMessageBox.about(self, "Klíče", "Něco se nepovedlo při generování klíče")

            with zipfile.ZipFile(path_message + "/public_zip.zip", mode="w") as archive:
                archive.write(path_message + "/public.publ", basename("public.publ"))
            #     with zipfile.ZipFile(path_message + "/public_zip.zip", mode="w") as archive:
            #         archive.write(path_message +"/public.publ", basename("public.publ"))

            with zipfile.ZipFile(path_message + "/private_zip.zip", mode="w") as archive2:
                archive2.write(path_message + "/private.priv", basename("private.priv"))
                # with zipfile.ZipFile(path_message + "/private_zip.zip", mode="w") as archive2:
                #     archive2.write(path_message +"/pivate.priv", basename("private.priv"))

            if os.path.exists(path_message + 'public.publ') == True and os.path.exists(
                    path_message + 'private.priv') == True and os.path.exists(
                    path_message + 'private_zip.zip') == True and os.path.exists(
                    path_message + 'private_zip.zip') == True:
                QMessageBox.about(self, "Klíče", "Klíče byly generovány a zazipovány.")
            elif os.stat(path_message + 'public.publ').st_size == 0 or os.stat(
                    path_message + 'private.priv').st_size == 0:
                QMessageBox.about(self, "Klíče", "Něco neproběhlo v pořádku. Klíče se nevygenerovaly.")

            # directory = pathlib.Path(path_message + "keys")
            # with zipfile.ZipFile(path_message + "keys_zip.zip", mode="w") as archive:
            #     for file_path in directory.iterdir():
            #         archive.write(file_path, arcname=file_path.name)
            # with zipfile.ZipFile(path_message + "directory.zip", mode="r") as archive:
            #     archive.printdir()
        except:
            QMessageBox.about(self, "Klíče", "Nelze generovat klíče bez zprávy... ")

    def sign_document(self):
        try:
            hashed = self.hashed_line
            path_message = self.path_of_message
            name_message = self.name_of_message
            path_message = path_message.replace(name_message, "")
            # print(path_message)
            # os.mkdir(path_message + "/signed")
            try:
                signature = rsa_dsa.cipher_math(rsa_dsa.cipher_func(hashed), self.dcko, self.nko)
                # print(signature)
                message_bytes = signature.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')
                # print(base64_message)

                fileName = open(path_message + "/signature.sign", "w")
                fileName.write(base64_message)
                fileNamePath = path_message + "/signature.sign"
                fileName.close()
            except:

                QMessageBox.about(self, "Podpis ", "Něco se nepovedlo, podpis neproběhl")

            # self.path_of_signature =""
            # self.name_of_signature =""
            # if fileName:
            #     print(fileName)
            #     self.path_of_signature = fileNamePath
            #     self.name_of_signature = "signature.sgn"
            #     self.path_of_signature = self.path_of_signature.replace(self.name_of_signature,"")
            #     file = open(fileName, 'w')
            #     file.write(base64_message)

            # print(fileNamePath)
            # src_path = path_message + "message.msg"
            # dst_path = path_message + "/signed/message.msg"
            # print(src_path)
            # shutil.copy(src_path, dst_path)

            with zipfile.ZipFile("outputs_from_dsa/sign.zip", mode="w") as archive:
                archive.write("outputs_from_dsa/message.msg", basename("message.msg"))
                archive.write("outputs_from_dsa/signature.sign", basename("signature.sign"))

            # directory = pathlib.Path(path_message + "signed")
            # with zipfile.ZipFile(path_message + "signed.zip", mode="w") as archive:
            #     for file_path in directory.iterdir():
            #         archive.write(file_path, arcname=file_path.name)
            # with zipfile.ZipFile(path_message + "directory.zip", mode="r") as archive:
            #     archive.printdir()

            if os.path.exists(path_message + 'sign.zip') == True and os.stat(path_message + 'sign.zip').st_size > 0:
                QMessageBox.about(self, "Podpis", "Dokument byl podepsán a zazipován společně se zprávou.")
                self.label_podepsano.setText("Dokument je podepsán a uložen. Vše proběhlo v pořádku.")
            else:
                QMessageBox.about(self, "Podpis",
                                  "Dokument nelze podepsat. Zkontrolujte, zda jsou generovány klíče a nahrána zpráva.")

        except:
            QMessageBox.about(self, "Podpis",
                              "Dokument nelze podepsat. Zkontrolujte, zda jsou generovány klíče a nahrána zpráva.")

        # https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/ decoding BASE 64

    def signature_open(self):
        try:
            options = QFileDialog.Options()
            fileNameSign, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                          "All Files (*)", options=options)
            self.path_of_signature = ""
            if fileNameSign:
                # print(os.path.basename(fileNameSign))
                # print(fileNameSign) #D:/PROGRAMOVANI/DRUHAK/KRYPTO/DSA/overeni_dsa_test/signed.zip
                file_zipped = os.path.basename(fileNameSign)
                self.path_of_signature = fileNameSign
                self.path_of_signature = self.path_of_signature.replace(file_zipped, "")
                # print(path_of_signature) #D:/PROGRAMOVANI/DRUHAK/KRYPTO/DSA/overeni_dsa_test/
                #
                with zipfile.ZipFile(fileNameSign, 'r') as zipObj:
                    # Extract all the contents of zip file in different directory
                    zipObj.extractall(self.path_of_signature)

            name_signature = os.path.basename(fileNameSign)
            name_message = os.path.basename(self.path_of_signature + "message.msg")
            self.hashed_tranfered_line = ""
            with open(self.path_of_signature + "message.msg", 'rb') as f:
                lines = f.readlines()
                for line in lines:
                    # print(line)
                    self.hashed_tranfered_line = hashlib.sha256(line.rstrip()).hexdigest()
            print(self.hashed_tranfered_line)

            self.label_hash_zpravy.setText(self.hashed_tranfered_line)
            if self.hashed_tranfered_line:
                QMessageBox.about(self, "Hash zpravy", "Hash zpravy byl proveden.")
        except:
            QMessageBox.about(self, "Podpis", "Nelze otevřít dokument pro ověření... ")

    def load_private_key(self):
        try:
            options = QFileDialog.Options()
            fileNameSign, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                          "All Files (*)", options=options)
            path_of_private_key = ""
            if fileNameSign:
                # print(os.path.basename(fileNameSign))
                # print(fileNameSign) #D:/PROGRAMOVANI/DRUHAK/KRYPTO/DSA/overeni_dsa_test/signed.zip
                file_zipped = os.path.basename(fileNameSign)
                path_of_private_key = fileNameSign
                path_of_private_key = path_of_private_key.replace(file_zipped, "")
                # print(path_of_signature) #D:/PROGRAMOVANI/DRUHAK/KRYPTO/DSA/overeni_dsa_test/
                #
                with zipfile.ZipFile(fileNameSign, 'r') as zipObj:
                    # Extract all the contents of zip file in different directory
                    zipObj.extractall(path_of_private_key)
            # print(path_of_private_key)

            tmp = []
            with open(path_of_private_key + "public.publ", 'rb') as f:
                lines = f.readlines()
                for line in lines:
                    tmp.append(int(line))
            # print(tmp)

            self.ecko_decipher = tmp[0]
            self.nko_decipher = tmp[1]

            self.label_privatni_klic.setText(str(self.ecko_decipher))
            self.label_privatni_klic_2.setText(str(self.nko_decipher))
        except:
            QMessageBox.about(self, "Privátní klíč",
                              "Nelze nahrát klíč pro dešifrování. Zkontrolujte, zda máte vše potřebné... ")

    def verify_signature(self):
        try:
            # print(self.path_of_signature)
            signature = ""
            with open(self.path_of_signature + "signature.sign", 'rb') as f:
                lines = ""
                for line in f.readlines():
                    lines += (line.rstrip().decode("utf-8"))
                    signature = lines
            f.close()

            base64_message = signature
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            message = str(message)
            print(message)
            print(self.ecko_decipher)
            print(self.nko_decipher)

            self.verified_message = rsa_dsa.decipher_func(
                rsa_dsa.decpher_math(message, self.ecko_decipher, self.nko_decipher))
            # print(self.verified_message)
            self.label_hash_desifrovan.setText(self.verified_message)

            if self.hashed_tranfered_line == self.verified_message:
                self.true_false_finish_label.setText(
                    "JE TO VSECK NAPROSTO BOŽÍ A FUNGUJE TO!!!! JICHUUU KRYPTOLOGIE JE BOŽÍ :D ")
                QMessageBox.about(self, "Ověření dokumentu", " OVĚŘENÍ SE POVEDLO! ZPRÁVA JE OKAA :) ")
            else:
                self.true_false_finish_label.setText("OVĚŘENÍ SE NEZDAŘILO!! JE TO VŠECKO ŠPATNĚ!")
                QMessageBox.about(self, "Ověření dokumentu", "OVĚŘENÍ SE NEZDAŘILO!! JE TO VŠECKO ŠPATNĚ! ")

        except:
            QMessageBox.about(self, "Ověření dokumentu", "Dokument nelze ověřit, nahráli jste vše potřebné?  ")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1312, 758)
        Form.setStyleSheet("background-color:rgb(36, 41, 50)")
        self.button_nahrat = QtWidgets.QPushButton(Form)
        self.button_nahrat.setGeometry(QtCore.QRect(40, 50, 351, 41))
        self.button_nahrat.setStyleSheet("QPushButton{\n"
                                         "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                         "    color:rgb(148, 148, 148);\n"
                                         "    border-radius: 20px;\n"
                                         "    border: 1px solid rgb(148, 148, 148);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    color:rgb(255, 255, 255);\n"
                                         "\n"
                                         "}")
        self.button_nahrat.setObjectName("button_nahrat")
        self.button_nahrat.clicked.connect(self.load_message)
        self.label_nazev = QtWidgets.QLabel(Form)
        self.label_nazev.setGeometry(QtCore.QRect(30, 130, 631, 21))
        self.label_nazev.setStyleSheet("QLabel {\n"
                                       "color: rgb(153, 227, 113);\n"
                                       "}")
        self.label_nazev.setObjectName("label_nazev")
        self.label_cesta = QtWidgets.QLabel(Form)
        self.label_cesta.setGeometry(QtCore.QRect(30, 190, 631, 21))
        self.label_cesta.setStyleSheet("QLabel {\n"
                                       "color: rgb(153, 227, 113);\n"
                                       "}")
        self.label_cesta.setObjectName("label_cesta")
        self.label_velikost = QtWidgets.QLabel(Form)
        self.label_velikost.setGeometry(QtCore.QRect(30, 250, 631, 21))
        self.label_velikost.setStyleSheet("QLabel {\n"
                                          "color: rgb(153, 227, 113);\n"
                                          "}")
        self.label_velikost.setObjectName("label_velikost")
        self.label_datum_uprav = QtWidgets.QLabel(Form)
        self.label_datum_uprav.setGeometry(QtCore.QRect(30, 310, 631, 21))
        self.label_datum_uprav.setStyleSheet("QLabel {\n"
                                             "color: rgb(153, 227, 113);\n"
                                             "}")
        self.label_datum_uprav.setObjectName("label_datum_uprav")
        self.button_podepsat = QtWidgets.QPushButton(Form)
        self.button_podepsat.setGeometry(QtCore.QRect(50, 420, 351, 41))
        self.button_podepsat.setStyleSheet("QPushButton{\n"
                                           "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                           "    color:rgb(148, 148, 148);\n"
                                           "    border-radius: 20px;\n"
                                           "    border: 1px solid rgb(148, 148, 148);\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "    color:rgb(255, 255, 255);\n"
                                           "\n"
                                           "}")
        self.button_podepsat.setObjectName("button_podepsat")
        self.button_podepsat.clicked.connect(self.sign_document)
        self.label_podepsano = QtWidgets.QLabel(Form)
        self.label_podepsano.setGeometry(QtCore.QRect(40, 510, 391, 21))
        self.label_podepsano.setStyleSheet("QLabel {\n"
                                           "color: rgb(153, 227, 113);\n"
                                           "}")
        self.label_podepsano.setObjectName("label_podepsano")
        self.button_overit_podpis = QtWidgets.QPushButton(Form)
        self.button_overit_podpis.setGeometry(QtCore.QRect(810, 440, 351, 41))
        self.button_overit_podpis.setStyleSheet("QPushButton{\n"
                                                "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                                "    color:rgb(148, 148, 148);\n"
                                                "    border-radius: 20px;\n"
                                                "    border: 1px solid rgb(148, 148, 148);\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    color:rgb(255, 255, 255);\n"
                                                "\n"
                                                "}")
        self.button_overit_podpis.setObjectName("button_overit_podpis")
        self.button_overit_podpis.clicked.connect(self.verify_signature)
        self.label_hash_zpravy = QtWidgets.QLabel(Form)
        self.label_hash_zpravy.setGeometry(QtCore.QRect(470, 520, 711, 21))
        self.label_hash_zpravy.setStyleSheet("QLabel {\n"
                                             "color: rgb(153, 227, 113);\n"
                                             "}")
        self.label_hash_zpravy.setObjectName("label_hash_zpravy")
        self.label_hash_desifrovan = QtWidgets.QLabel(Form)
        self.label_hash_desifrovan.setGeometry(QtCore.QRect(470, 590, 711, 21))
        self.label_hash_desifrovan.setStyleSheet("QLabel {\n"
                                                 "color: rgb(153, 227, 113);\n"
                                                 "}")
        self.label_hash_desifrovan.setObjectName("label_hash_desifrovan")
        self.button_restart = QtWidgets.QPushButton(Form)
        self.button_restart.setGeometry(QtCore.QRect(30, 560, 331, 41))
        self.button_restart.setStyleSheet("QPushButton{\n"
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
        self.button_restart.setObjectName("button_restart")
        self.true_false_finish_label = QtWidgets.QLabel(Form)
        self.true_false_finish_label.setGeometry(QtCore.QRect(40, 650, 1161, 61))
        self.true_false_finish_label.setStyleSheet("QLabel {\n"
                                                   "color: rgb(153, 227, 113);\n"
                                                   "}")
        self.true_false_finish_label.setObjectName("true_false_finish_label")
        self.nadpis = QtWidgets.QLabel(Form)
        self.nadpis.setGeometry(QtCore.QRect(520, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.nadpis.setFont(font)
        self.nadpis.setStyleSheet("QLabel{\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}")
        self.nadpis.setObjectName("nadpis")
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(30, 100, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setStyleSheet("QLabel{\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}")
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(30, 160, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setStyleSheet("QLabel{\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}")
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(30, 220, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label3.setFont(font)
        self.label3.setStyleSheet("QLabel{\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}")
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(Form)
        self.label4.setGeometry(QtCore.QRect(30, 280, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label4.setFont(font)
        self.label4.setStyleSheet("QLabel{\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}")
        self.label4.setObjectName("label4")
        self.label7 = QtWidgets.QLabel(Form)
        self.label7.setGeometry(QtCore.QRect(470, 490, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label7.setFont(font)
        self.label7.setStyleSheet("QLabel{\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}")
        self.label7.setObjectName("label7")
        self.label8 = QtWidgets.QLabel(Form)
        self.label8.setGeometry(QtCore.QRect(470, 560, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label8.setFont(font)
        self.label8.setStyleSheet("QLabel{\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}")
        self.label8.setObjectName("label8")
        self.Label5 = QtWidgets.QLabel(Form)
        self.Label5.setGeometry(QtCore.QRect(690, 260, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Label5.setFont(font)
        self.Label5.setStyleSheet("QLabel{\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}")
        self.Label5.setObjectName("Label5")
        self.button_generovat = QtWidgets.QPushButton(Form)
        self.button_generovat.setGeometry(QtCore.QRect(50, 360, 351, 41))
        self.button_generovat.setStyleSheet("QPushButton{\n"
                                            "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                            "    color:rgb(148, 148, 148);\n"
                                            "    border-radius: 20px;\n"
                                            "    border: 1px solid rgb(148, 148, 148);\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    color:rgb(255, 255, 255);\n"
                                            "\n"
                                            "}")
        self.button_generovat.setObjectName("button_podepsat_2")
        self.button_generovat.clicked.connect(self.generate_keys)
        self.button_nahrat_elpodpis = QtWidgets.QPushButton(Form)
        self.button_nahrat_elpodpis.setGeometry(QtCore.QRect(890, 70, 351, 41))
        self.button_nahrat_elpodpis.setStyleSheet("QPushButton{\n"
                                                  "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                                  "    color:rgb(148, 148, 148);\n"
                                                  "    border-radius: 20px;\n"
                                                  "    border: 1px solid rgb(148, 148, 148);\n"
                                                  "}\n"
                                                  "QPushButton:hover{\n"
                                                  "    color:rgb(255, 255, 255);\n"
                                                  "\n"
                                                  "}")
        self.button_nahrat_elpodpis.setObjectName("button_nahrat_elpodpis")
        self.button_nahrat_elpodpis.clicked.connect(self.signature_open)
        self.button_nahrat_klice = QtWidgets.QPushButton(Form)
        self.button_nahrat_klice.setGeometry(QtCore.QRect(900, 240, 351, 41))
        self.button_nahrat_klice.setStyleSheet("QPushButton{\n"
                                               "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                               "    color:rgb(148, 148, 148);\n"
                                               "    border-radius: 20px;\n"
                                               "    border: 1px solid rgb(148, 148, 148);\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    color:rgb(255, 255, 255);\n"
                                               "\n"
                                               "}")
        self.button_nahrat_klice.setObjectName("button_nahrat_klice")
        self.button_nahrat_klice.clicked.connect(self.load_private_key)
        self.label_privatni_klic = QtWidgets.QLabel(Form)
        self.label_privatni_klic.setGeometry(QtCore.QRect(690, 300, 551, 21))
        self.label_privatni_klic.setStyleSheet("QLabel {\n"
                                               "color: rgb(153, 227, 113);\n"
                                               "}")
        self.label_privatni_klic.setObjectName("label_privatni_klic")
        self.label_privatni_klic_2 = QtWidgets.QLabel(Form)
        self.label_privatni_klic_2.setGeometry(QtCore.QRect(690, 380, 551, 21))
        self.label_privatni_klic_2.setStyleSheet("QLabel {\n"
                                                 "color: rgb(153, 227, 113);\n"
                                                 "}")
        self.label_privatni_klic_2.setObjectName("label_privatni_klic_2")
        self.Label5_2 = QtWidgets.QLabel(Form)
        self.Label5_2.setGeometry(QtCore.QRect(690, 340, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Label5_2.setFont(font)
        self.Label5_2.setStyleSheet("QLabel{\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "}")
        self.Label5_2.setObjectName("Label5_2")
        self.label_signaturesgn = QtWidgets.QLabel(Form)
        self.label_signaturesgn.setGeometry(QtCore.QRect(680, 180, 551, 21))
        self.label_signaturesgn.setStyleSheet("QLabel {\n"
                                              "color: rgb(153, 227, 113);\n"
                                              "}")
        self.label_signaturesgn.setObjectName("label_signaturesgn")
        self.label_messagemsg = QtWidgets.QLabel(Form)
        self.label_messagemsg.setGeometry(QtCore.QRect(680, 130, 551, 21))
        self.label_messagemsg.setStyleSheet("QLabel {\n"
                                            "color: rgb(153, 227, 113);\n"
                                            "}")
        self.label_messagemsg.setObjectName("label_messagemsg")
        self.label_datum_uprav.raise_()
        self.label_velikost.raise_()
        self.button_nahrat.raise_()
        self.label_nazev.raise_()
        self.label_cesta.raise_()
        self.button_podepsat.raise_()
        self.label_podepsano.raise_()
        self.button_overit_podpis.raise_()
        self.label_hash_zpravy.raise_()
        self.label_hash_desifrovan.raise_()
        self.button_restart.raise_()
        self.true_false_finish_label.raise_()
        self.nadpis.raise_()
        self.label1.raise_()
        self.label2.raise_()
        self.label3.raise_()
        self.label4.raise_()
        self.label7.raise_()
        self.label8.raise_()
        self.Label5.raise_()
        self.button_generovat.raise_()
        self.button_nahrat_elpodpis.raise_()
        self.button_nahrat_klice.raise_()
        self.label_privatni_klic.raise_()
        self.label_privatni_klic_2.raise_()
        self.Label5_2.raise_()
        self.label_signaturesgn.raise_()
        self.label_messagemsg.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_nahrat.setText(_translate("Form", "NAHRÁT SOUBOR"))
        self.label_nazev.setText(_translate("Form", "Název souboru + přípona"))
        self.label_cesta.setText(_translate("Form", "Cesta k souboru"))
        self.label_velikost.setText(_translate("Form", "Velikost souboru"))
        self.label_datum_uprav.setText(_translate("Form", "Datum poslední úpravy"))
        self.button_podepsat.setText(_translate("Form", "PODEPSAT SOUBOR"))
        self.label_podepsano.setText(_translate("Form", ""))
        self.button_overit_podpis.setText(_translate("Form", "OVĚŘIT PODPIS"))
        self.label_hash_zpravy.setText(_translate("Form", ""))
        self.label_hash_desifrovan.setText(_translate("Form", ""))
        self.button_restart.setText(_translate("Form", "RESTARTOVAT"))
        self.true_false_finish_label.setText(
            _translate("Form", ""))
        self.nadpis.setText(_translate("Form", "DSA - DRÁBKOVÁ"))
        self.label1.setText(_translate("Form", "Název souboru"))
        self.label2.setText(_translate("Form", "Cesta k souboru"))
        self.label3.setText(_translate("Form", "Velikost souboru"))
        self.label4.setText(_translate("Form", "Datum poslední úpravy"))
        self.label7.setText(_translate("Form", "Hash zprávy"))
        self.label8.setText(_translate("Form", "Hash získaný dešifrováním"))
        self.Label5.setText(_translate("Form", "Veřejný klíč"))
        self.button_generovat.setText(_translate("Form", "GENEROVAT KLÍČE"))
        self.button_nahrat_elpodpis.setText(_translate("Form", "NAHRÁT ELEKTRONICKÝ PODPIS"))
        self.button_nahrat_klice.setText(_translate("Form", "NAHRÁT VEŘEJNÝ KLÍČ K DEŠIFROVÁNÍ"))
        self.label_privatni_klic.setText(_translate("Form", "Veřejný klíč"))
        self.label_privatni_klic_2.setText(_translate("Form", "\"N\"ko"))
        self.Label5_2.setText(_translate("Form", "\"N\"ko"))
        self.label_signaturesgn.setText(_translate("Form", ""))  # Nahrali a rozbalili jste soubor signature.sgn
        self.label_messagemsg.setText(_translate("Form", ""))  # Nahrali a rozbalili jste soubor message.msg


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

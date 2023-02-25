import unicodedata
import re
from random import randint
import numpy as np
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui, uic


class Ui_Form(object):
    index_row_alh = {
        0: "A",
        1: "D",
        2: "F",
        3: "G",
        4: "X",
        5: "V"
    }

    index_col_alh = {
        0: "A",
        1: "D",
        2: "F",
        3: "G",
        4: "X",
        5: "V"
    }
    special = {
        ' ': 'XSPACEX',
    }

    alph_cz = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y',
               'Z']
    alph_en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z']

    alph_cz_numbers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                       'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self):
        self.comboLanguage = None

    def format_key_and_alpha(self, string):
        """This function formats input key for cipher and also format."""
        string = string.replace(" ", "")
        string = ''.join("" if c.isdigit() else c for c in string)
        string = string.upper()
        string = ''.join(c for c in unicodedata.normalize('NFD', string)
                         if unicodedata.category(c) != 'Mn')
        string = re.sub('\W+', '', string)
        removed_duplicate = ""
        for i in string:
            if i in removed_duplicate:
                pass
            else:
                removed_duplicate = removed_duplicate + i
        return removed_duplicate

    def text_format(self, text):
        """This function make sure, that the text input has proper text format."""
        new_text = ""
        for t in text:
            if t in self.special.keys():
                new_text += self.special[t]
            else:
                new_text += t.upper()
        new_text = re.sub('\W+', '', new_text)
        new_text = ''.join(c for c in unicodedata.normalize('NFD', new_text)
                           if unicodedata.category(c) != 'Mn')
        return new_text

    def alpha_random(self, original_aplh):
        """Makes a random aplhapbet."""
        random_alph = []
        i = len(original_aplh) - 1
        while original_aplh:
            index = randint(0, i)
            random_alph.append(original_aplh.pop(index))
            i -= 1
        return random_alph

    def random_table_aplhas(self, random_apha_list, switch_mode):
        """Makes a table from random alphabet."""
        if switch_mode == 0:
            elements = []
            for i in random_apha_list:
                if i not in elements:
                    elements.append(i)

            matrix = []
            while elements:
                matrix.append(elements[:5])
                elements = elements[5:]
            return matrix
        if switch_mode == 1:
            elements = []
            for i in random_apha_list:
                if i not in elements:
                    elements.append(i)
            matrix = []
            while elements:
                matrix.append(elements[:6])
                elements = elements[6:]
            return matrix

    def encode_text(self, test_matrix, textik):
        """The function returns paired text. The argument is a classic matrix,
        then it is converted to an np array to find an index.
        """
        arr = np.array(test_matrix)
        ciphered_text = ''
        for char in textik:
            result = np.where(arr == char)
            result = list(zip(result[0], result[1]))
            for key, value in self.index_col_alh.items():
                if result[0][0] == key:
                    ciphered_text += value
            for key, value in self.index_row_alh.items():
                if result[0][1] == key:
                    ciphered_text += value
        return ciphered_text

    def cipher_list(self, ciphered_text, key):
        """Return the letters that pass first
        encryption stages in the ADVFX matrix. It already returns it in
        letters that depend on lenght of a key.
        :param ciphered_text, key:
        :return:
        """
        len_key = len(key)
        ciphered_text = ' '.join(
            ciphered_text[i:i + len_key] for i in range(0, len(ciphered_text), len_key))
        cipher_in_list = []
        help = []
        i = 0
        for char in ciphered_text:
            if char == " ":
                cipher_in_list.append(help)
                help = []
                i = 0
                continue
            help.append(char)
            i += 1
        cipher_in_list.append(help)
        cipher_in_list = [ele for ele in cipher_in_list if ele != []]
        count_of_lists = len(cipher_in_list)
        check_last_item = len(cipher_in_list[count_of_lists - 1])

        for i in range(0, len_key):
            if check_last_item < len_key:
                cipher_in_list[count_of_lists - 1].append(" ")
                check_last_item += 1
            else:
                continue
        return cipher_in_list

    def key_list(self, plain_key):
        """This function makes from plain key sorted key list for principal of the cipher.
        :param plain_key:
        :return:
        """
        key_char_index = 0
        list_sorted_key = []

        for char in plain_key:
            list_sorted_key.append(char + str(key_char_index))
            key_char_index += 1
        return sorted(list_sorted_key)

    def get_final_encoded_cipher(self, key_sorted, matrix):
        """This function takes sorted key and matrix and makes a final cipher.
        :param key_sorted, matrix:
        :return:
        """
        ciphered_text_final = ''
        for item in key_sorted:
            i = 0
            while i < len(matrix):
                ciphered_text_final += matrix[i][int(item[1])]
                i += 1
            ciphered_text_final += ' '
        return ciphered_text_final

    def decode_get_cipher_into_list_again(self, cipher):
        """There will be a docstring.
        :param cipher:
        :return:
        """
        cipher_in_list = []
        help = []
        i = 0
        for char in cipher:
            if char == " ":
                cipher_in_list.append(help)
                help = []
                i = 0
                continue
            else:
                help.append(char)
            i += 1
        cipher_in_list.append(help)
        cipher_in_list = [ele for ele in cipher_in_list if ele != []]
        couunt_lists = len(cipher_in_list)
        for i in range(0, couunt_lists):
            if len(cipher_in_list[i]) < len(cipher_in_list[0]):
                cipher_in_list[i].append(" ")
        return cipher_in_list

    def decode_trans_list_order(self, sorted_key, matrix):
        """It takes the cipher and breaks it back into the table.
        It divides it based on " " - create a new table after the space.
        :param sorted_key, matrix:
        :return:
        """
        nums_of_order = ''
        i = 0
        while i < len(sorted_key):
            for j in sorted_key:
                if (int(j[1])) == i:
                    nums_of_order += str(sorted_key.index(j))
                    i += 1
        list_order = []
        for row in nums_of_order:
            list_order.append(matrix[int(row)])

        print(list_order)
        return list_order

    def decode_full_fill_list(self, sorted_key, decode_list):
        """Takes a deciphered plain text and fill it to list.
        :param sorted_key, decode_list:
        :return:
        """
        num_rows = len(decode_list[0])
        i = 0
        tmp = 0
        while i < len(sorted_key):
            for j in range(0, len(decode_list[i])):
                tmp += 1
            if tmp == num_rows - 1:
                decode_list[i].append(" ")
            tmp = 0
            i += 1
        print(decode_list)
        return decode_list

    def decode_get_it_from_matrix(self, matrix, sorted_key):
        """From list make a string.
        :param matrix, sorted_key:
        :return:
        """
        i = 0
        var = ""
        while i < len(matrix[0]):
            for element in range(0, len(sorted_key)):
                var += str(matrix[element][i])
            i += 1
        print(var)
        return var

    def decode_text(self, textik):
        """
        bla bla bla

        :param textik:
        :return:
        """
        ciphered_text = ' '.join(textik[i:i + 2] for i in range(0, len(textik), 2))  # only print
        cipher_in_list = []
        help = []
        i = 0
        for char in ciphered_text:
            if char == " ":
                cipher_in_list.append(help)
                help = []
                i = 0
                continue
            help.append(char)
            i += 1
        cipher_in_list.append(help)
        cipher_in_list = [ele for ele in cipher_in_list if ele != []]
        print(cipher_in_list)
        return cipher_in_list

    def decode_final_decode_to_normal(self, cipher_in_list_almost_final, matrix):
        """There will be a docstring."""
        temp_list = []
        temp_string = ""
        for i in range(0, len(cipher_in_list_almost_final)):
            first = cipher_in_list_almost_final[i][0]
            second = cipher_in_list_almost_final[i][1]
            first = list(self.index_col_alh.keys())[list(self.index_col_alh.values()).index(first)]
            temp_string += str(first)
            second = list(self.index_row_alh.keys())[list(self.index_row_alh.values()).index(second)]
            temp_string += str(second)
        temp_string = ' '.join(temp_string[i:i + 2] for i in range(0, len(temp_string), 2))  # only print
        help = []
        i = 0
        for char in temp_string:
            if char == " ":
                temp_list.append(help)
                help = []
                i = 0
                continue
            help.append(char)
            i += 1
        temp_list.append(help)
        final_string = ""
        for i in range(0, len(temp_list)):
            first = int(temp_list[i][0])
            second = int(temp_list[i][1])
            final_string += matrix[first][second]
        print(final_string)
        return final_string

    def get_normal_text_back(self, text):
        """There will be a docstring."""
        text = text.replace("XSPACEX", " ")
        return text

    def check_cipher(self, string, mode):
        """There will be a docstring."""
        if mode == 0:
            pattern = "ADFGX"
            if re.search(pattern, string):
                return string
            return self.warning.setText("Tyto znaky nelze desifrovat")
        if mode == 1:
            pattern = "ADFGVX"
            if re.search(pattern, string):
                return string
            return self.warning.setText("Tyto znaky nelze desifrovat")

    def error_input(self):
        """There will be a docstring."""
        error = 0
        try:
            str(self.otevrenyText.text())
            str(self.sifrovanyText.text())
            str(self.klic.text())
            str(self.abecedaInput.text())
        except:
            error = 2
        return error

    def generate_metrix(self):
        """There will be a docstring."""
        if self.comboMatrix.currentText() == "ADFGX" and self.comboLanguage.currentText() == "CZ":
            alphabet_cz = self.alpha_random(self.alph_cz.copy())
            alph_cz_matrix = self.random_table_aplhas(alphabet_cz, 0)
            return alph_cz_matrix
        if self.comboMatrix.currentText() == "ADFGX" and self.comboLanguage.currentText() == "ENG":
            alphabet_en = self.alpha_random(self.alph_en.copy())
            alph_en_matrix = self.random_table_aplhas(alphabet_en, 0)
            return alph_en_matrix
        if self.comboMatrix.currentText() == "ADFGVX":
            alphabet_six = self.alpha_random(self.alph_cz_numbers.copy())
            alph_six_matrix = self.random_table_aplhas(alphabet_six, 1)
            return alph_six_matrix

    def restart_button(self):
        self.tabulkaAbecedy.clear()
        self.abecedaInput.setText("")
        self.klic.setText("")
        self.sifrovanyText.setText("")
        self.warning.setText("")
        self.otevrenyText.setText("")
        self.warning.setText("")
        self.zobrazeniSifer.setText("")

    def fill_table(self, matrix, matrix_string):
        """There will be a docstring."""
        line = 0
        row = 0
        lenght = len(matrix)
        print(lenght)
        for char in matrix_string:
            self.tabulkaAbecedy.setColumnCount(lenght)
            self.tabulkaAbecedy.setRowCount(lenght)
            if lenght == 5:
                self.tabulkaAbecedy.setHorizontalHeaderLabels(['A', 'D', 'F', 'G', 'X'])
                self.tabulkaAbecedy.setVerticalHeaderLabels(['A', 'D', 'F', 'G', 'X'])
            else:
                self.tabulkaAbecedy.setHorizontalHeaderLabels(['A', 'D', 'F', 'G', 'X', 'V'])
                self.tabulkaAbecedy.setVerticalHeaderLabels(['A', 'D', 'F', 'G', 'X', 'V'])

            self.tabulkaAbecedy.setColumnWidth(0, 100)
            self.tabulkaAbecedy.setColumnWidth(1, 100)
            self.tabulkaAbecedy.setColumnWidth(2, 100)
            self.tabulkaAbecedy.setColumnWidth(3, 100)
            self.tabulkaAbecedy.setColumnWidth(4, 100)
            self.tabulkaAbecedy.setStyleSheet(
                "QHeaderView::section {\n"
                "background-color:rgb(36, 41, 50);\n"
                "color: #FFF;\n"
                "}\n"
                "\n"
                "QTableCornerButton::section {\n"
                "background-color:rgb(36, 41, 50);\n"
                "}"
                "QTableWidget{\n"
                "border:1px solid white;\n"
                "color: #FFF;\n"
                "font-color: #FFF"
                "aligment: center"
                "}\n"
            )

            self.tabulkaAbecedy.setItem(line, row, QTableWidgetItem(char))
            row += 1
            if row == lenght:
                row = 0
                line += 1

    def code(self):
        """There will be a docstring."""
        klic = str(self.klic.text())
        otevreny_text = str(self.otevrenyText.text())
        sifrovaci_abeceda = str(self.abecedaInput.text())
        if str(self.klic.text()) == "" or str(self.otevrenyText.text()) == "":
            self.warning.setText("Musíš zadat kód či text!")
        else:
            klic = self.format_key_and_alpha(klic)
            otevreny_text = self.text_format(otevreny_text)
            sifrovaci_abeceda = self.format_key_and_alpha(sifrovaci_abeceda)

            if len(sifrovaci_abeceda) == 0:
                self.abecedaInput.setText("")
                matrix = self.generate_metrix()
                matrix_string = ''.join(str(item) for innerlist in matrix for item in innerlist)
                self.fill_table(matrix, matrix_string)
                self.abecedaInput.setText(matrix_string)
                self.labelPouzitaAbeceda.setText(matrix_string)
                prvni_faze_sifry = self.encode_text(matrix, otevreny_text)
                dva_cipher_list = self.cipher_list(prvni_faze_sifry, klic)
                usporadat_klic = self.key_list(klic)
                hotova_sifra = self.get_final_encoded_cipher(usporadat_klic, dva_cipher_list)
                self.sifrovanyText.setText(hotova_sifra)



            elif len(
                    sifrovaci_abeceda) == 25 and self.comboMatrix.currentText() == "ADFGX" and self.comboMatrix.currentText() == "CZ":
                sifrovaci_abeceda.replace("W", "V")
                self.labelPouzitaAbeceda.setText(sifrovaci_abeceda)
                # print(sifrovaci_abeceda)
                alph_cz_list = []
                for char in sifrovaci_abeceda:
                    alph_cz_list.append(char)
                # print(alph_cz_list)
                alph_cz_matrix = self.random_table_aplhas(alph_cz_list, 0)
                print(alph_cz_matrix)
                self.fill_table(alph_cz_matrix, sifrovaci_abeceda)
                prvni_faze_sifry = self.encode_text(alph_cz_matrix, otevreny_text)
                # print(prvni_faze_sifry)
                dva_cipher_list = self.cipher_list(prvni_faze_sifry, klic)
                # print(dva_cipher_list)
                usporadat_klic = self.key_list(klic)
                hotova_sifra = self.get_final_encoded_cipher(usporadat_klic, dva_cipher_list)
                self.sifrovanyText.setText(hotova_sifra)
                self.zobrazeniSifer.setText(hotova_sifra)
                self.warning.setText("")

            elif len(
                    sifrovaci_abeceda) == 25 and self.comboMatrix.currentText() == "ADFGX" and self.comboMatrix.currentText() == "ENG":
                sifrovaci_abeceda.replace("J", "I")
                self.labelPouzitaAbeceda.setText(sifrovaci_abeceda)
                # print(sifrovaci_abeceda)
                alph_cz_list = []
                for char in sifrovaci_abeceda:
                    alph_cz_list.append(char)
                # print(alph_cz_list)
                alph_cz_matrix = self.random_table_aplhas(alph_cz_list, 0)
                print(alph_cz_matrix)
                self.fill_table(alph_cz_matrix, sifrovaci_abeceda)
                prvni_faze_sifry = self.encode_text(alph_cz_matrix, otevreny_text)
                # print(prvni_faze_sifry)
                dva_cipher_list = self.cipher_list(prvni_faze_sifry, klic)
                # print(dva_cipher_list)
                usporadat_klic = self.key_list(klic)
                hotova_sifra = self.get_final_encoded_cipher(usporadat_klic, dva_cipher_list)
                self.sifrovanyText.setText(hotova_sifra)
                self.zobrazeniSifer.setText(hotova_sifra)
                self.warning.setText("")


            elif len(sifrovaci_abeceda) == 35 and self.comboMatrix.currentText() == "ADFGVX":
                self.labelPouzitaAbeceda.setText(sifrovaci_abeceda)
                # print(sifrovaci_abeceda)
                alph_six_list = []
                for char in sifrovaci_abeceda:
                    alph_six_list.append(char)
                # print(alph_six_list)
                alph_cz_matrix = self.random_table_aplhas(alph_six_list, 1)
                # print(alph_cz_matrix)
                prvni_faze_sifry = self.encode_text(alph_cz_matrix, otevreny_text)
                # print(prvni_faze_sifry)
                dva_cipher_list = self.cipher_list(prvni_faze_sifry, klic)
                print(dva_cipher_list)
                usporadat_klic = self.key_list(klic)
                hotova_sifra = self.get_final_encoded_cipher(usporadat_klic, dva_cipher_list)
                self.sifrovanyText.setText(hotova_sifra)
                self.zobrazeniSifer.setText(hotova_sifra)
                self.warning.setText("")

            else:
                self.warning.setText(
                    "Je třeba zkontrolovat údaje, například délku vložné abecedy, či zprávně zvolenou kombinaci "
                    "jazyka s typem šifry. ")

    def decode(self):
        """There will be a docstring."""
        sifrovaci_abeceda = str(self.abecedaInput.text())
        # sifrovaci_abeceda = self.format_key_and_alpha(sifrovaci_abeceda)
        klic = str(self.klic.text())
        klic = self.format_key_and_alpha(klic)
        self.labelPouzitaAbeceda.setText(sifrovaci_abeceda)
        sifra = str(self.sifrovanyText.text())
        usporadat_klic = self.key_list(klic)

        if self.comboMatrix.currentText() == "ADFGX" and len(
                sifrovaci_abeceda) == 25 and self.comboLanguage.currentText() == "CZ":
            # self.check_cipher(sifra,0)
            sifrovaci_abeceda.replace("W", "V")
            alph_cz_list = []
            for char in sifrovaci_abeceda:
                alph_cz_list.append(char)
            matrix = self.random_table_aplhas(alph_cz_list, 0)
            print(matrix)
            self.fill_table(matrix, sifrovaci_abeceda)
            sifra_v_listu_jedna = self.decode_get_cipher_into_list_again(sifra)
            print(sifra_v_listu_jedna)
            print(usporadat_klic)
            sifra_v_listu_dva = self.decode_trans_list_order(usporadat_klic, sifra_v_listu_jedna)
            print(sifra_v_listu_dva)
            sifra_v_listu_tri = self.decode_full_fill_list(usporadat_klic, sifra_v_listu_dva)
            print(sifra_v_listu_tri)
            sifrovany_string = self.decode_get_it_from_matrix(sifra_v_listu_tri, usporadat_klic)
            print(sifrovany_string)
            predposledni_sifra = self.decode_text(sifrovany_string)
            print(predposledni_sifra)
            hotova_sifra = self.decode_final_decode_to_normal(predposledni_sifra, matrix)
            print(hotova_sifra)
            text_desifr = self.get_normal_text_back(hotova_sifra)
            self.zobrazeniSifer.setText(text_desifr)
            self.warning.setText("")

        elif self.comboMatrix.currentText() == "ADFGX" and len(
                sifrovaci_abeceda) == 25 and self.comboLanguage.currentText() == "ENG":
            sifrovaci_abeceda.replace("J", "I")
            alph_cz_list = []
            for char in sifrovaci_abeceda:
                alph_cz_list.append(char)
            matrix = self.random_table_aplhas(alph_cz_list, 0)
            print(matrix)
            self.fill_table(matrix, sifrovaci_abeceda)
            sifra_v_listu_jedna = self.decode_get_cipher_into_list_again(sifra)
            print(sifra_v_listu_jedna)
            print(usporadat_klic)
            sifra_v_listu_dva = self.decode_trans_list_order(usporadat_klic, sifra_v_listu_jedna)
            print(sifra_v_listu_dva)
            sifra_v_listu_tri = self.decode_full_fill_list(usporadat_klic, sifra_v_listu_dva)
            print(sifra_v_listu_tri)
            sifrovany_string = self.decode_get_it_from_matrix(sifra_v_listu_tri, usporadat_klic)
            print(sifrovany_string)
            predposledni_sifra = self.decode_text(sifrovany_string)
            print(predposledni_sifra)
            hotova_sifra = self.decode_final_decode_to_normal(predposledni_sifra, matrix)
            print(hotova_sifra)
            text_desifr = self.get_normal_text_back(hotova_sifra)
            self.zobrazeniSifer.setText(text_desifr)
            self.warning.setText("")

        elif self.comboMatrix.currentText() == "ADFGVX":
            alph_cz_list = []
            for char in sifrovaci_abeceda:
                alph_cz_list.append(char)
            matrix = self.random_table_aplhas(alph_cz_list, 1)
            print(matrix)
            self.fill_table(matrix, sifrovaci_abeceda)
            sifra_v_listu_jedna = self.decode_get_cipher_into_list_again(sifra)
            print(sifra_v_listu_jedna)
            print(usporadat_klic)
            sifra_v_listu_dva = self.decode_trans_list_order(usporadat_klic, sifra_v_listu_jedna)
            print(sifra_v_listu_dva)
            sifra_v_listu_tri = self.decode_full_fill_list(usporadat_klic, sifra_v_listu_dva)
            print(sifra_v_listu_tri)
            sifrovany_string = self.decode_get_it_from_matrix(sifra_v_listu_tri, usporadat_klic)
            print(sifrovany_string)
            predposledni_sifra = self.decode_text(sifrovany_string)
            print(predposledni_sifra)
            hotova_sifra = self.decode_final_decode_to_normal(predposledni_sifra, matrix)
            print(hotova_sifra)
            text_desifr = self.get_normal_text_back(hotova_sifra)
            self.zobrazeniSifer.setText(text_desifr)
            self.warning.setText("")

        if sifrovaci_abeceda == "":
            self.warning.setText("Nemám žádnou abecedu...")

    def setupUi(self, Form):
        """There will be a docstring."""
        Form.setObjectName("Form")
        Form.resize(1281, 913)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("background-color:rgb(36, 41, 50)")
        self.klic = QtWidgets.QLineEdit(Form)
        self.klic.setGeometry(QtCore.QRect(30, 80, 691, 51))
        self.klic.setStyleSheet("QLineEdit {\n"
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
        self.klic.setObjectName("klic")
        self.otevrenyText = QtWidgets.QLineEdit(Form)
        self.otevrenyText.setGeometry(QtCore.QRect(30, 170, 691, 131))
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
        self.sifrovatButton = QtWidgets.QPushButton(Form)
        self.sifrovatButton.setGeometry(QtCore.QRect(30, 490, 351, 41))
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
        self.sifrovatButton.clicked.connect(self.code)
        self.desifrovatButton = QtWidgets.QPushButton(Form)
        self.desifrovatButton.setGeometry(QtCore.QRect(390, 490, 331, 41))
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
        self.desifrovatButton.clicked.connect(self.decode)
        self.sifrovanyText = QtWidgets.QLineEdit(Form)
        self.sifrovanyText.setGeometry(QtCore.QRect(740, 80, 521, 121))
        self.sifrovanyText.setStyleSheet("QLineEdit {\n"
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
        self.sifrovanyText.setObjectName("sifrovanyText")
        self.labelKlicInput = QtWidgets.QLabel(Form)
        self.labelKlicInput.setGeometry(QtCore.QRect(40, 50, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelKlicInput.setFont(font)
        self.labelKlicInput.setStyleSheet("QLabel{\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "}")
        self.labelKlicInput.setObjectName("labelKlicInput")
        self.labelTextInput = QtWidgets.QLabel(Form)
        self.labelTextInput.setGeometry(QtCore.QRect(40, 140, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelTextInput.setFont(font)
        self.labelTextInput.setStyleSheet("QLabel{\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "}")
        self.labelTextInput.setObjectName("labelTextInput")
        self.abecedaInput = QtWidgets.QLineEdit(Form)
        self.abecedaInput.setGeometry(QtCore.QRect(30, 340, 691, 51))
        self.abecedaInput.setStyleSheet("QLineEdit {\n"
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
        self.abecedaInput.setText("")
        self.abecedaInput.setReadOnly(False)
        self.abecedaInput.setObjectName("abecedaInput")
        self.labelAbecedaInput = QtWidgets.QLabel(Form)
        self.labelAbecedaInput.setGeometry(QtCore.QRect(40, 310, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelAbecedaInput.setFont(font)
        self.labelAbecedaInput.setStyleSheet("QLabel{\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "}")
        self.labelAbecedaInput.setObjectName("labelAbecedaInput")
        self.labelSifraOutput = QtWidgets.QLabel(Form)
        self.labelSifraOutput.setGeometry(QtCore.QRect(760, 50, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelSifraOutput.setFont(font)
        self.labelSifraOutput.setStyleSheet("QLabel{\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "}")
        self.labelSifraOutput.setObjectName("labelSifraOutput")
        self.labelTableOutput = QtWidgets.QLabel(Form)
        self.labelTableOutput.setGeometry(QtCore.QRect(750, 210, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelTableOutput.setFont(font)
        self.labelTableOutput.setStyleSheet("QLabel{\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "}")
        self.labelTableOutput.setObjectName("labelTableOutput")
        self.comboMatrix = QtWidgets.QComboBox(Form)
        self.comboMatrix.setGeometry(QtCore.QRect(30, 550, 341, 41))
        self.comboMatrix.setStyleSheet("QComboBox {\n"
                                       "border:1px solid transparent;\n"
                                       "border-radius: 2px;\n"
                                       "color: #FFF;\n"
                                       "padding-left:10px;\n"
                                       "padding-right: 10px;\n"
                                       "padding-top:10px;\n"
                                       "padding-bottom:10px;\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QComboBox QListView {\n"
                                       "color: rgb(97, 97, 97);\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "QComboBox::down-arrow\n"
                                       "{\n"
                                       "image: url(D:/PROGRAMOVANI/DRUHAK/KRYPTO/PYTHON/AGDX_sifra/down-chevron.png);\n"
                                       "width: 20px;\n"
                                       "}")
        self.comboMatrix.setObjectName("comboMatrix")
        self.comboMatrix.addItem("")
        self.comboMatrix.addItem("")
        self.comboLanguage = QtWidgets.QComboBox(Form)
        self.comboLanguage.setGeometry(QtCore.QRect(390, 550, 331, 41))
        self.comboLanguage.setStyleSheet("QComboBox {\n"
                                         "border:1px solid transparent;\n"
                                         "border-radius: 2px;\n"
                                         "color: #FFF;\n"
                                         "padding-left:10px;\n"
                                         "padding-right: 10px;\n"
                                         "padding-top:10px;\n"
                                         "padding-bottom:10px;\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "QComboBox QListView {\n"
                                         "color: rgb(97, 97, 97);\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox::down-arrow\n"
                                         "{\n"
                                         "image: url(D:/PROGRAMOVANI/DRUHAK/KRYPTO/PYTHON/AGDX_sifra/down-chevron.png"
                                         ");\n "
                                         "width: 20px;\n"
                                         "}")
        self.comboLanguage.setObjectName("comboLanguage")
        self.comboLanguage.addItem("")
        self.comboLanguage.addItem("")
        self.labelMatrix = QtWidgets.QLabel(Form)
        self.labelMatrix.setGeometry(QtCore.QRect(30, 710, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelMatrix.setFont(font)
        self.labelMatrix.setStyleSheet("QLabel{\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "}")
        self.labelMatrix.setObjectName("labelMatrix")
        self.nadpis = QtWidgets.QLabel(Form)
        self.nadpis.setGeometry(QtCore.QRect(40, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.nadpis.setFont(font)
        self.nadpis.setStyleSheet("QLabel{\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}")
        self.nadpis.setObjectName("nadpis")
        self.warning = QtWidgets.QLabel(Form)
        self.warning.setGeometry(QtCore.QRect(30, 620, 1231, 61))
        self.warning.setStyleSheet("QLabel {\n"
                                   "color: rgb(153, 227, 113);\n"
                                   "}")
        self.warning.setObjectName("warning")
        self.tabulkaAbecedy = QtWidgets.QTableWidget(Form)
        self.tabulkaAbecedy.setGeometry(QtCore.QRect(740, 240, 521, 301))
        self.tabulkaAbecedy.setStyleSheet("QTableWidget{\n"
                                          "border:1px solid white;\n"
                                          "color: #FFF;\n"
                                          "font-color: #FFF"
                                          "}\n"
                                          )

        self.tabulkaAbecedy.setObjectName("tabulkaAbecedy")
        self.labelAbecedaInput_2 = QtWidgets.QLabel(Form)
        self.labelAbecedaInput_2.setGeometry(QtCore.QRect(40, 400, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelAbecedaInput_2.setFont(font)
        self.labelAbecedaInput_2.setStyleSheet("QLabel{\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "}")
        self.labelAbecedaInput_2.setObjectName("labelAbecedaInput_2")
        self.labelPouzitaAbeceda = QtWidgets.QLabel(Form)
        self.labelPouzitaAbeceda.setGeometry(QtCore.QRect(30, 440, 681, 31))
        self.labelPouzitaAbeceda.setStyleSheet("QLabel {\n"
                                               "color: rgb(153, 227, 113);\n"
                                               "}")
        self.labelPouzitaAbeceda.setObjectName("labelPouzitaAbeceda")
        self.zobrazeniSifer = QtWidgets.QLabel(Form)
        self.zobrazeniSifer.setGeometry(QtCore.QRect(30, 700, 1231, 61))
        self.zobrazeniSifer.setStyleSheet("QLabel {\n"
                                          "color: rgb(153, 227, 113);\n"
                                          "}")
        self.zobrazeniSifer.setObjectName("warning_2")
        self.restartButton = QtWidgets.QPushButton(Form)
        self.restartButton.setGeometry(QtCore.QRect(840, 560, 331, 41))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sifrovatButton.setText(_translate("Form", "ŠIFROVAT"))
        self.desifrovatButton.setText(_translate("Form", "DEŠIFROVAT"))
        self.labelKlicInput.setText(_translate("Form", "Klíč"))
        self.labelTextInput.setText(_translate("Form", "Text"))
        self.labelAbecedaInput.setText(_translate("Form", "Chci vlozit abecedu"))
        self.labelSifraOutput.setText(_translate("Form", "Šifra"))
        self.labelTableOutput.setText(_translate("Form", "Tabulka abecedy"))
        self.comboMatrix.setItemText(0, _translate("Form", "ADFGX"))
        self.comboMatrix.setItemText(1, _translate("Form", "ADFGVX"))
        self.comboLanguage.setItemText(0, _translate("Form", "CZ"))
        self.comboLanguage.setItemText(1, _translate("Form", "ENG"))
        self.labelMatrix.setText(_translate("Form", "Matrix"))
        self.nadpis.setText(_translate("Form", "ADFG(V)X - DRÁBKOVÁ"))
        self.warning.setText(_translate("Form", "WARNING"))
        self.labelAbecedaInput_2.setText(_translate("Form", "Použitá abeceda"))
        self.labelPouzitaAbeceda.setText(_translate("Form", "POUŽITÁ ABECEDA"))
        self.zobrazeniSifer.setText(_translate("Form", "ZAŠIFROVANÝ / DEŠIFROVANÝ TEXT"))
        self.restartButton.setText(_translate("Form", "RESTARTOVAT"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

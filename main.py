import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
from converter import english_to_nepali_converter, nepali_to_english_converter


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r"E:\NextStepInfoTechCourses\Python Batch 13\19 Python-Projects\05 PyQT GUI\DateConverter\date_converter.ui", self)
        self.bs_year.setValidator(QIntValidator())
        self.bs_year.setMaxLength(4)

        self.bs_month.setValidator(QIntValidator())
        self.bs_month.setMaxLength(2)

        self.bs_day.setValidator(QIntValidator())
        self.bs_day.setMaxLength(2)

        self.ad_year.setValidator(QIntValidator())
        self.ad_year.setMaxLength(4)

        self.ad_month.setValidator(QIntValidator())
        self.ad_month.setMaxLength(2)

        self.ad_day.setValidator(QIntValidator())
        self.ad_day.setMaxLength(2)

        self.convert_to_ad_button.clicked.connect(self.convert_to_ad_method)
        self.convert_to_bs_button.clicked.connect(self.convert_to_bs_method)

    def convert_to_ad_method(self):
        try:
            y = int(self.bs_year.text())
            m = int(self.bs_month.text())
            d = int(self.bs_day.text())

            result = nepali_to_english_converter(y, m, d)
            self.show_message_box("English Date", result)
        except Exception as e:
            self.show_error_message("English Date", str(e))

    def convert_to_bs_method(self):
        try:
            y = int(self.ad_year.text())
            m = int(self.ad_month.text())
            d = int(self.ad_day.text())

            result = english_to_nepali_converter(y, m, d)
            self.show_message_box("Nepali Date", result)
        except Exception as e:
            self.show_error_message("Nepali Date", str(e))

    def show_message_box(self, title, text):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setStandardButtons(QMessageBox.Ok)
        button_ok = msg_box.button(QMessageBox.Ok)
        button_ok.clicked.connect(self.clear_line_edit)
        msg_box.exec_()

    def show_error_message(self, title, text):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def clear_line_edit(self):
        self.bs_year.clear()
        self.bs_month.clear()
        self.bs_day.clear()
        self.ad_year.clear()
        self.ad_month.clear()
        self.ad_day.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

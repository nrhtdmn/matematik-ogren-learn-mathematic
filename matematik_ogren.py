import sys
import random
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QLineEdit,
    QMessageBox,
)
from PyQt5.QtCore import Qt


class MatematikOgrenmeUygulamasi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.soruOlustur()

    def initUI(self):
        self.setWindowTitle("Matematik Öğrenme Uygulaması")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.soru_etiketi = QLabel("", self)
        self.soru_etiketi.setAlignment(Qt.AlignCenter)
        self.soru_etiketi.setStyleSheet("font-size: 18px;")
        self.layout.addWidget(self.soru_etiketi)

        self.cevap_girdisi = QLineEdit(self)
        self.cevap_girdisi.setFixedSize(200, 40)
        self.cevap_girdisi.setStyleSheet("font-size: 18px;")
        self.layout.addWidget(self.cevap_girdisi, alignment=Qt.AlignCenter)

        self.buton_layout = QHBoxLayout()

        self.kontrol_butonu = QPushButton("Kontrol Et", self)
        self.kontrol_butonu.setFixedSize(120, 40)
        self.kontrol_butonu.setStyleSheet("font-size: 18px;")
        self.kontrol_butonu.clicked.connect(self.cevabiKontrolEt)
        self.buton_layout.addWidget(self.kontrol_butonu, alignment=Qt.AlignCenter)

        self.sonraki_buton = QPushButton("Sonraki Soru", self)
        self.sonraki_buton.setFixedSize(120, 40)
        self.sonraki_buton.setStyleSheet("font-size: 18px;")
        self.sonraki_buton.clicked.connect(self.soruOlustur)
        self.buton_layout.addWidget(self.sonraki_buton, alignment=Qt.AlignCenter)

        self.layout.addLayout(self.buton_layout)

        self.central_widget.setLayout(self.layout)

        self.show()

    def soruOlustur(self):
        self.operator = random.choice(["+", "-", "*", "/"])
        if self.operator == "+":
            self.sayi1 = random.randint(0, 100)
            self.sayi2 = random.randint(0, 100)
        elif self.operator == "-":
            self.sayi1 = random.randint(0, 100)
            self.sayi2 = random.randint(0, self.sayi1)
        elif self.operator == "*":
            self.sayi1 = random.randint(0, 10)
            self.sayi2 = random.randint(0, 10)
        elif self.operator == "/":
            self.sayi2 = random.randint(1, 10)
            self.sayi1 = self.sayi2 * random.randint(1, 10)

        self.soru_etiketi.setText(f"{self.sayi1} {self.operator} {self.sayi2} = ?")
        self.cevap_girdisi.clear()

    def cevabiKontrolEt(self):
        try:
            kullanici_cevabi = float(self.cevap_girdisi.text())
            dogru_cevap = eval(f"{self.sayi1} {self.operator} {self.sayi2}")
            if kullanici_cevabi == dogru_cevap:
                QMessageBox.information(self, "Doğru", "Tebrikler! Doğru cevap.")
            else:
                QMessageBox.warning(
                    self, "Yanlış", f"Yanlış cevap. Doğru cevap: {dogru_cevap}"
                )
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli bir sayı girin.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    matematik_uygulamasi = MatematikOgrenmeUygulamasi()
    sys.exit(app.exec_())

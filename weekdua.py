from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox
)
import sys

class RegisForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("WEEK 2: LAYOUT - USER REGISTRATION FORM")
        self.resize(550, 450)
        
        # data Section
        data_box = QGroupBox("Identitas")
        data_layout = QVBoxLayout()
        data_layout.addWidget(QLabel("Nama : Kayla Mizanti", self))
        data_layout.addWidget(QLabel("Nim : F1D022127", self))
        data_layout.addWidget(QLabel("Kelas : D", self))
        data_box.setLayout(data_layout)
        
        # Navigasi
        navigation_box = QGroupBox("Navigation")
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(QPushButton("Home"))
        navigation_layout.addWidget(QPushButton("About"))
        navigation_layout.addWidget(QPushButton("Contact"))
        navigation_box.setLayout(navigation_layout)
        
        # Registration Form
        regis_box = QGroupBox("User registration")
        regis_layout = QVBoxLayout()
        
        regis_layout.addWidget(QLabel("Full Name:"))
        self.full_name = QLineEdit()
        regis_layout.addWidget(self.full_name)
        
        regis_layout.addWidget(QLabel("Email:"))
        self.email = QLineEdit()
        regis_layout.addWidget(self.email)
        
        regis_layout.addWidget(QLabel("Phone:"))
        self.phone = QLineEdit()
        regis_layout.addWidget(self.phone)
        
        # Gender Selection
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QLabel("Gender:"))
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        regis_layout.addLayout(gender_layout)
        
        # Country Selection
        regis_layout.addWidget(QLabel("Country:"))
        self.country = QComboBox()
        self.country.addItems(["Select", "Indonesia", "UK", "Korea", "Belanda", "Arab"])
        regis_layout.addWidget(self.country)
        
        regis_box.setLayout(regis_layout)
        
        # Actions Section
        actions_box = QGroupBox("Actions")
        actions_layout = QHBoxLayout()
        actions_layout.addWidget(QPushButton("Submit"))
        actions_layout.addWidget(QPushButton("Cancel"))
        actions_box.setLayout(actions_layout)
        
        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(data_box)
        main_layout.addWidget(navigation_box)
        main_layout.addWidget(regis_box)
        main_layout.addWidget(actions_box)
        main_layout.addStretch()
        
        self.setLayout(main_layout)
        self.setStyleSheet("QWidget { font-size: 14px; }")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisForm()
    window.show()
    sys.exit(app.exec_())

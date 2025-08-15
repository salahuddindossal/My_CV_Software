import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QTextBrowser
)

from project_window import ProjectWindow  

class MyCVApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("My CV App")
        self.setGeometry(100, 100, 500, 500)

        self.label1 = QLabel("👋 Welcome to My CV", self)
        self.button1 = QPushButton("Click", self)
        self.button1.clicked.connect(self.open_projects)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        self.label1.setObjectName("label1")

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button1)  # Button on the left
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_layout.addItem(spacer)          # Spacer pushes everything else to the right

        layout.addLayout(h_layout)
        self.setLayout(layout)
        self.show()

    def open_projects(self):
        self.project_window = ProjectWindow()
        self.project_window.show()

# Main program
app = QApplication(sys.argv)

app.setStyleSheet("""
    QPushButton {
        background-color: blue;
        color: white;
        font-size: 14px;
        padding: 10px;
        border-radius: 15px;
        min-width: 50px;
        min-height: 50px;
        max-width: 50px;
        max-height: 50px;
    }
    QPushButton:hover {
        background-color: white;
        color: black;
    }
    QLabel#label1 {
        font-size: 80px;
        color: #34495e;
        padding-left: 550px;
    }
   
    QLabel#intro_heading {
        font-size: 30px;
        font-weight: bold;
        color: black;
        margin-bottom: 0px;
        text-decoration: underline;
    }

    QTextBrowser#intro_para {
        font-size: 20px;
        color: #333;
        margin-top: 0px;
        padding: 0px;
        background: transparent;
    }
     QLabel#edu {
        font-size: 30px;
        font-weight: bold;
        color: black;
        margin-top: 60px;
        text-decoration: underline;
    }
     QTextBrowser#edu_para {
        font-size: 20px;
        color: #333;
        margin-top: 0px;
        padding: 0px;
        background: transparent;
    }
        QLabel#skill {
        font-size: 30px;
        font-weight: bold;
        color: black;
        margin-top: 60px;
        text-decoration: underline;
        
    }
     QTextBrowser#skill_para {
        font-size: 20px;
        color: #333;
        margin-top: 0px;
        padding: 0px;
        background: transparent;
    }
""")

window = MyCVApp()
sys.exit(app.exec_())

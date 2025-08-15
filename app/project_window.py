from PyQt5.QtWidgets import QWidget, QLabel, QTextBrowser, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from skills import SkillsWindow  # Make sure this file exists and is correctly linked

class ProjectWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Projects")
        self.setGeometry(150, 150, 700, 800)  # Increased size to accommodate more content

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)

        # 🔹 INTRODUCTION
        self.label_heading = QLabel("INTRODUCTION:")
        self.label_heading.setObjectName("intro_heading")
        self.label_heading.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_heading)

        self.intro_paragraph = QTextBrowser()
        self.intro_paragraph.setObjectName("intro_para")
        self.intro_paragraph.setText(
            "I am a highly skilled and passionate Python programmer with a strong ability to solve complex problems\n"
            "and develop efficient, robust solutions.\n\n"
            "Over the years, I have gained extensive experience working with various Python libraries and frameworks\n"
            "to build applications and automate tasks effectively.\n\n"
            "Alongside my programming expertise, I am also a professional graphic designer with advanced proficiency\n"
            "in Adobe Photoshop and a creative mindset that allows me to design visually appealing graphics and user interfaces.\n\n"
            "Additionally, I have solid experience in web development, with strong command of HTML, CSS, and foundational\n"
            "knowledge of JavaScript, enabling me to create responsive and user-friendly websites.\n\n"
            "My diverse skill set and commitment to continuous learning make me capable of delivering high-quality results\n"
            "across technical and creative projects, while ensuring innovative and practical solutions for every challenge."
        )
        self.intro_paragraph.setReadOnly(True)
        self.intro_paragraph.setFrameShape(QTextBrowser.NoFrame)
        self.intro_paragraph.setFixedHeight(300)  # Ensures enough height for scrolling
        self.intro_paragraph.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.intro_paragraph.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        layout.addWidget(self.intro_paragraph)

        # 🔹 EDUCATION
        self.label_education = QLabel("EDUCATION:")
        self.label_education.setObjectName("edu")
        self.label_education.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_education)

        self.edu_paragraph = QTextBrowser()
        self.edu_paragraph.setObjectName("edu_para")
        self.edu_paragraph.setText(
            "SZABIST UNIVERSITY\t\t2024\n\n"
            "Bachelor of Science in Mechatronics Engineering"
        )
        self.edu_paragraph.setReadOnly(True)
        self.edu_paragraph.setFrameShape(QTextBrowser.NoFrame)
        self.edu_paragraph.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.edu_paragraph.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        layout.addWidget(self.edu_paragraph)

        # 🔹 CONTACT
        self.label_contact = QLabel("CONTACT:")
        self.label_contact.setObjectName("work_heading")
        self.label_contact.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_contact)

        self.contact_paragraph = QTextBrowser()
        self.contact_paragraph.setObjectName("work_para")
        self.contact_paragraph.setHtml("""
            <div style="font-size: 23px; font-family: 'Segoe UI', sans-serif; color: #333; background-color: #f4f4f4; padding: 15px; border-radius: 5px;">
                <ul style="list-style: none; padding-left: 0;">
                    <li><b>Full Name:</b> Salahuddin Dossal</li>
                    <li><b>Contact Number:</b> 0335-3012271</li>
                    <li><b>Email Address:</b> salahuddindossal2006email@gmail.com</li>
                    <li><b>Location:</b> Karachi</li>
                </ul>
            </div>
        """)
        self.contact_paragraph.setReadOnly(True)
        self.contact_paragraph.setFrameShape(QTextBrowser.NoFrame)
        layout.addWidget(self.contact_paragraph)

        # 🔹 Skills Button
        self.button1 = QPushButton("Skills", self)
        self.button1.clicked.connect(self.open_skills)
        layout.addWidget(self.button1)

        self.setLayout(layout)

        self.skills_window = None

        # Stylesheet (embedded)
        self.setStyleSheet("""
            QLabel#intro_heading,
            QLabel#edu,
            QLabel#work_heading {
                font-size: 30px;
                font-weight: bold;
                color: #222;
                margin-bottom: 10px;
                text-decoration: underline;
            }

            QTextBrowser#intro_para,
            QTextBrowser#edu_para,
            QTextBrowser#work_para {
                font-size: 20px;
                color: #333;
                background: transparent;
                border: none;
            }

            QTextBrowser#work_para {
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 5px;
            }

            QPushButton {
                background-color: #0078d7;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
                font-size: 16px;
            }

            QPushButton:hover {
                background-color: #005fa3;
            }
        """)

    def open_skills(self):
        self.skills_window = SkillsWindow()
        self.skills_window.show()

from PyQt5.QtWidgets import QWidget, QLabel, QTextBrowser, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from work_exp import WorkExperienceWindow


class SkillsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Skills")
        self.setGeometry(200, 200, 400, 200)

        
        layout = QVBoxLayout()

        self.label_skills = QLabel("SKILLS:")
        self.label_skills.setObjectName("skill")
        self.label_skills.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_skills)

        self.edu_paragraph = QTextBrowser()
        self.edu_paragraph.setObjectName("skill_para")
        self.edu_paragraph.setText(
            "\n• PYHTON" \
            "\n\n• MULTIPLE PYHTON LIBERARIES" \
            "\n\n• WEB DEVELOPER" \
            "\n\n• HTML/CSS/BOOTSTRAP" \
            "\n\n• BASIC JAVASCRIPT" \
            "\n\n• GRAPHIC DESIGNING" \
            "\n\n• PROFESSIONAL PHOTOSHOP USER" \
            "\n\n• WEB DESIGNER" \
            "\n\n• BASIC OF C++" \
            "\n\n• TYPE SCRIPT" \
             "\n\n• PROBLEM SOLVING, CREATIVE" \
            
        )
        self.edu_paragraph.setReadOnly(True)
        self.edu_paragraph.setFrameShape(QTextBrowser.NoFrame)
        self.edu_paragraph.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.edu_paragraph.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        layout.addWidget(self.edu_paragraph)

        # ✅ Apply layout to the window
        self.setLayout(layout)
        self.button_work = QPushButton("Show Work Experience")
        self.button_work.clicked.connect(self.open_work_experience)
        layout.addWidget(self.button_work)
    def open_work_experience(self):
        self.work_window = WorkExperienceWindow()
        self.work_window.show()


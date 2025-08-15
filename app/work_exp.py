# work_exp.py
from PyQt5.QtWidgets import QWidget, QLabel, QTextBrowser, QVBoxLayout
from PyQt5.QtCore import Qt

class WorkExperienceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Work Experience")
        self.setGeometry(250, 250, 600, 300)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        # Heading
        self.label_heading = QLabel("WORK EXPERIENCE:")
        self.label_heading.setObjectName("work_heading")
        self.label_heading.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_heading)

        # Paragraph (you can replace this with your real experience)
        self.exp_paragraph = QTextBrowser()
        self.exp_paragraph.setObjectName("work_para")
        self.exp_paragraph.setHtml("""
    <div style="font-size: 23px; font-family: 'Segoe UI', sans-serif; color: #333; background-color: #f4f4f4; padding: 15px; border-radius: 5px;">
        <ul style="line-height: 1.6;">
            <li><b>Graphic Designer</b> – Freelance<br>
            <i>OLYMPUS INNOVATION (London)</i><br>
            Designed marketing and greeting banners for mobile apps and websites.</li>

            <li><b>Web Developer</b> – Freelance<br>
            Built responsive websites using HTML, CSS, JS, and Bootstrap for a Canadian client.</li>
        </ul>
    </div>
""")

        self.exp_paragraph.setReadOnly(True)
        self.exp_paragraph.setFrameShape(QTextBrowser.NoFrame)
        layout.addWidget(self.exp_paragraph)
        self.setLayout(layout)

         # Heading
        self.label_heading = QLabel("PROJECTS:")
        self.label_heading.setObjectName("pro_heading")
        self.label_heading.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label_heading)

        # Paragraph (you can replace this with your real experience)
        self.exp_paragraph = QTextBrowser()
        self.exp_paragraph.setObjectName("work_para")
        self.exp_paragraph.setHtml("""
         <div style="font-size: 23px; font-family: 'Segoe UI', sans-serif; color: #333; background-color: #f4f4f4; padding: 15px; border-radius: 5px;">
        <ul style="line-height: 1.6;">
            <li><b>Graphic Designer</b> – Projects<br>
            I made multiple market level banners and posters saved in my portfolio.</li>

            <br><li><b>Web Developer</b> – Projects<br>
            Builted a landing page HTML/CSS AND BOOTTSRAP, 
            <br>The landing page shows the proper designing and alignment of the text, images and containers.
            <li><b>LINK(LANDING PAGE): https://willowy-cocada-d041c2.netlify.app/</li>
            </b></li>
                                
           <br> <li><b>Web Developer</b> – 2 Projects<br>
            I created an Instagram-style login page and integrated it with a website that supports form submissions.<br>
            The form was connected to my email, so whenever someone entered their login details, the data would be sent directly to my inbox.<br>
            Additionally, after the user clicked the login button, the real Instagram website would open to maintain authenticity.<br>
            This project was developed solely for educational and demonstration purposes.

            <li><b>LINK(INSTA-LOGIN): https://shiny-sunshine-2f83eb.netlify.app/ </li>
            </b></li>
                                   
            <br><li><b>Pyhton</b> – Projects<br>
            
            I’ve developed an AI model and integrated it into a desktop assistant capable of performing multiple tasks such as opening YouTube, Google, WhatsApp, searching for songs, and more.<br>
            It uses a predefined script structure, allowing users to interact with it naturally and easily.<br><br>

            In the future, I plan to enhance it further to function more like ChatGPT—possibly by integrating APIs—but I intend to build most of it on my own.<br>
            I also aim to expand its capabilities to include features like setting alarms, creating to-do lists and reminders, sending messages, and handling other personalized tasks.<br><br>

            Eventually, I want to bring this assistant to mobile devices as a fully functional phone app.
            <br><li><b>Pyhton</b> – 2 Projects<br>
            I built this software (GUI) using PyQt and Python to showcase my CV in a professional way.<br>
            I used the <code>setHtml</code> method to incorporate HTML elements for better formatting and presentation.<br><br>

            This project highlights my skills in Python, HTML/CSS, and UI design.<br>
            However, due to some limitations and constraints within Python and PyQt, I wasn’t completely free in terms of design flexibility.
                                   
            
            <br><br><b>I have only included market-level and professional projects that reflect all of my skills.<br>
            In addition, I also have personal projects that I built just for fun, simply because I enjoy coding.</b>

            
            
            
        </ul>
    </div>
          
""")

        self.exp_paragraph.setReadOnly(True)
        self.exp_paragraph.setFrameShape(QTextBrowser.NoFrame)
        layout.addWidget(self.exp_paragraph)
        self.setLayout(layout)

        # CSS Styling
        self.setStyleSheet("""
            QLabel#work_heading {
                font-size: 30px;
                font-weight: bold;
                color: #222;
                margin-bottom: 10px;
            }

            QTextBrowser#work_para {
                    
                    color: #333;
                    background-color: #f9f9f9;
                    padding: 15px;
                    font-family: 'Segoe UI', sans-serif;
                    border-radius: 5px;
            }
            QLabel#por_heading {
                font-size: 30px;
                font-weight: bold;
                color: #222;
                margin-bottom: 10px;
            }

        """)

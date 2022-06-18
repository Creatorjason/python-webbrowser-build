from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngine import *


class JasonBrowser():

    def __int__(self):
        self.window = QWidget()
        self.window.setWindowTitle("Jason Web browser")
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(100)
        self.enter_btn = QPushButton("Enter")
        self.enter_btn.setMinimumHeight(100)

        self.prev_btn = QPushButton("Prev⤆")
        self.enter_btn.setMinimumHeight(100)

        self.next_btn = QPushButton("Next⤇")
        self.enter_btn.setMinimumHeight(100)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.enter_btn)
        self.horizontal.addWidget(self.prev_btn)
        self.horizontal.addWidget(self.next_btn)

        self.browser = QWebEngineView()

        self.enter_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.prev_btn.clicked.connect(self.browser.back())
        self.next_btn.clicked.connect(self.browser.forward())
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://google.com"))
        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("https"):
            url = "https://" + url
            self.url_bar.setText(f"https://{url}")
        self.browser.setUrl(QUrl(url))


app = QApplication([])
window = JasonBrowser()
app.exec()

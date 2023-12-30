from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

class SimpleHTML(QWidget):
    def __init__(self, html_code):
        super().__init__()
        self.setup_ui(html_code)

    def setup_ui(self, html_code):
        layout = QVBoxLayout(self)

        web_view = QWebEngineView(self)
        web_view.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        web_view.setHtml(html_code, QUrl('about:blank'))

        layout.addWidget(web_view)

        self.setLayout(layout)

def shtml_start(html_code):
    app = QApplication([])
    simple_html = SimpleHTML(html_code)
    simple_html.show()
    app.exec_()

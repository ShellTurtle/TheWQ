from PyQt6.QtWidgets import QApplication
from modules import Notepad

if __name__ == "__main__":
    app = QApplication([])
    notepad = Notepad()
    notepad.show()
    app.exec()

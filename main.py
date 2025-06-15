from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog
from PyQt6.QtGui import QIcon

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TheWQ")
        self.setGeometry(100, 100, 400, 300)
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.setWindowIcon(QIcon('./TheWQ.png'))
        
        # 创建菜单栏
        menu_bar = self.menuBar()

        # 文件菜单
        file_menu = menu_bar.addMenu("文件")
        new_action = file_menu.addAction("新建")
        new_action.triggered.connect(lambda: self.text_edit.clear())
        open_action = file_menu.addAction("打开")
        open_action.triggered.connect(self.open_file)
        save_action = file_menu.addAction("保存")
        save_action.triggered.connect(self.save_file)
        exit_action = file_menu.addAction("退出")
        exit_action.triggered.connect(self.close)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "Text Files (*.txt);;TheWQ Files (*.wq);;All Files (*)")
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.text_edit.setPlainText(content)

    def save_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "保存文件", "", "Text Files (*.txt);;TheWQ Files (*.wq);;All Files (*)")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                content = self.text_edit.toPlainText()
                f.write(content)


if __name__ == "__main__":
    app = QApplication([])
    window = Notepad()
    window.show()
    app.exec()

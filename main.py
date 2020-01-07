import sys
import mainui
import hashlib
from PyQt5.QtWidgets import QApplication,QMainWindow

def an1():
    #获得文本框内容
    text1 = ui.lineEdit.text()
    # 创建md5对象
    m = hashlib.md5()
    #Python3中默认为unicode，把它设置为utf-8
    b = text1.encode(encoding='utf-8')
    m.update(b)
    text1_md5 = m.hexdigest()
    #显示加密后的内容
    text2 = ui.lineEdit_2.setText(text1_md5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    '''增加按钮事件'''
    ui.pushButton.clicked.connect(an1)
    sys.exit(app.exec_())

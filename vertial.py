import PyQt5, sys
from designer import mainwindow_hortzontal
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()  # 创建窗口对象
    ui = mainwindow_hortzontal.Ui_MainWindow()  # ui对象的初始化
    ui.setupUi(window)  # 调用对应的方法，里面有各种按钮的显示方法
    window.show()  # 显示窗口
    sys.exit(app.exec_())  # 进入程序主循环（GUI通用实现逻辑）,并通过exit退出释放资源

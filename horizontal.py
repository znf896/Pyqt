import PyQt5, sys
from designer import mainwindow
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

if __name__ == "__main__":
    # 创建QApplication的实例
    # print(sys.argv)
    # app = QApplication(sys.argv)  # sys.argv以列表的形式显示文件路径
    #
    # # 创建窗口
    # window = QWidget()
    #
    # # 设置窗口大小
    # window.resize(500, 300)
    #
    # # 移动窗口
    # window.move(300, 300)
    #
    # #设置标题
    # window.setWindowTitle("hello Pyqt")
    #
    # #显示窗口
    # window.show()#没有循环，会导致代码运行完之后，自动退出窗口
    #
    # #进入程序主循环（GUI通用实现逻辑）,并通过exit退出释放资源
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    window = QMainWindow()  # 创建窗口对象
    ui = mainwindow.Ui_Dialog()  # ui对象的初始化
    ui.setupUi(window)  # 调用对应的方法，里面有各种按钮的显示方法
    window.show()  # 显示窗口
    sys.exit(app.exec_())  # 进入程序主循环（GUI通用实现逻辑）,并通过exit退出释放资源

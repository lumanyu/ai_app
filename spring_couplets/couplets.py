import sys

from PyQt5 import QtCore,QtGui,QtWidgets

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRectF

class MyLabel(QtWidgets.QWidget):
    def __init__(self, text=None, horizontal=False):
        super(self.__class__, self).__init__()
        self.text = text
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        #self.setStyleSheet("background-color: {};".format(QtGui.QColor(230, 0, 0).name()))
        self.horizontal=horizontal

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtCore.Qt.black)
        font_size=30
        painter.setFont(QFont('楷体', font_size)) #对联使用的字体和大小
        coor_orig_x = 20
        coor_orig_y = 100
        if self.horizontal:
            painter.translate(0, font_size*4/2) #平移到label的相对坐标（0，60）
        else:
            painter.translate(coor_orig_x, coor_orig_y) #平移到lable的相对坐标（20，100）
        #painter.rotate(-90)
        if self.text:
            #painter.drawText(QRectF(0.0,0.0,50.0,500.0), QtCore.Qt.AlignCenter, 0, 0, self.text)
            if self.horizontal:
                #painter.fillRect(QRectF(coor_orig_x,coor_orig_y,coor_orig_x+font_size*4,coor_orig_y+font_size), QtGui.QColor(230, 0, 0))
                painter.fillRect(QRectF(0,0,font_size*4,font_size+10), QtGui.QColor(230, 0, 0))
                painter.drawText(0, font_size, self.text)
            else:
                painter.fillRect(QRectF(coor_orig_x,coor_orig_y,font_size,coor_orig_y+font_size*7), QtGui.QColor(230, 0, 0))
                painter.drawText(QRectF(coor_orig_x,coor_orig_y,font_size,coor_orig_y+font_size*7),  self.text)
        painter.end()

class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        leftSide = MyLabel("桃\n花\n坞\n里\n桃\n花\n庵")
        middleSide = MyLabel('桃花庵歌', horizontal=True)
        rightSide = MyLabel('桃\n花\n庵\n下\n桃\n花\n仙')
        hBoxLayout = QtWidgets.QHBoxLayout()
        hBoxLayout.addWidget(leftSide)
        hBoxLayout.addWidget(middleSide)
        hBoxLayout.addWidget(rightSide)
        self.setLayout(hBoxLayout)
        self.setGeometry(300, 300, 250, 150)
        self.resize(550, 550) #对联画布宽高
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

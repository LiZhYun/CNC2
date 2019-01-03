#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: lizhyun
@license: 
@contact: 
@software: 
@file: cnc.py
@time: 18-12-30 下午1:15
@desc:
'''
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QDesktopWidget
from PyQt5 import QtWidgets
import CNC.edit
import math
from CNC import AutoCode
class MainWindow(QMainWindow, AutoCode.Ui_MyWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.center()
        self.Export.triggered.connect(self.export)
        self.Open.triggered.connect(self.open)
        self.Edit.triggered.connect(self.edit)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.normalGeometry2 = QRect((screen.width() - size.width()) / 2 + screen.left(),(screen.height() - size.height()) / 2,size.width(), size.height())
        self.setGeometry((screen.width() - size.width()) / 2 + screen.left(),(screen.height() - size.height()) / 2,size.width(), size.height())

    def export(self):
        choose = QMessageBox(self)
        MainButton = choose.addButton("主程序", QMessageBox.ActionRole)
        SubButton = choose.addButton("子程序", QMessageBox.ActionRole)
        CancelButton = choose.addButton("取消", QMessageBox.ActionRole)
        choose.setText("主程序 | 子程序")
        choose.setWindowTitle("选择导出文件类型")
        choose.show()
        choose.exec()
        reply = choose.clickedButton()
        if reply == MainButton:
            fileName , ok= QFileDialog.getSaveFileName(self, "主程序保存",
                                                         "./",
                                                         "MPF Files (*.mpf);; TXT Files (*.txt)")
            #self.MainText.setPlainText(fileName)
            try:
                with open(fileName, 'w') as f:
                    f.write(str(self.MainText.toPlainText()))
            except FileNotFoundError as e:
                self.error_message = QtWidgets.QErrorMessage()
                self.error_message.showMessage("请选择文件或输入文件名")
        elif reply == SubButton:
            self.message = QtWidgets.QMessageBox.about(self, "提示", "请根据需要修改主程序中调用程序名和子程序文件名")
            fileName , ok= QFileDialog.getSaveFileName(self, "子程序保存",
                                                   "./",
                                                   "SPF Files (*.spf);; TXT Files (*.txt)")
            #self.MainText.setPlainText(fileName)
            try:
                with open(fileName, 'w') as f:
                    f.write(str(self.SubText.toPlainText()))
            except FileNotFoundError as e:
                self.error_message = QtWidgets.QErrorMessage()
                self.error_message.showMessage("请选择文件或输入文件名")
        else:
            choose.close()


    def open(self):
        choose = QMessageBox(self)
        MainButton = choose.addButton("主程序", QMessageBox.ActionRole)
        SubButton = choose.addButton("子程序", QMessageBox.ActionRole)
        CancelButton = choose.addButton("取消", QMessageBox.ActionRole)
        choose.setText("主程序 | 子程序")
        choose.setWindowTitle("选择打开文件类型")
        choose.show()
        choose.exec()
        reply = choose.clickedButton()
        if reply == MainButton:
            fileName, ok = QFileDialog.getOpenFileName(self, "主程序",
                                                       "./",
                                                       "MPF Files (*.mpf);; TXT Files (*.txt)")
            try:
                with open(fileName, 'r', encoding='utf-8', errors="ignore") as f:
                    for line in f.readlines():
                        self.MainText.appendPlainText(line)
            except FileNotFoundError as e:
                self.error_message = QtWidgets.QErrorMessage()
                self.error_message.showMessage("请选择文件或输入文件名")
        elif reply == SubButton:
            fileName, ok = QFileDialog.getOpenFileName(self, "子程序",
                                                       "./",
                                                       "SPF Files (*.spf);; TXT Files (*.txt)")
            try:
                with open(fileName, 'r') as f:
                    for line in f.readlines():
                        self.SubText.appendPlainText(line)
            except FileNotFoundError as e:
                self.error_message = QtWidgets.QErrorMessage()
                self.error_message.showMessage("请选择文件或输入文件名")
        else:
            choose.close()


    def edit(self):
        self.paraedit = CNC.edit.Ui_Wizard()
        Wizard = QtWidgets.QWizard()
        self.paraedit.setupUi(Wizard)
        Wizard.show()
        Wizard.exec()
        self.format(self.paraedit)

    def format(self, wizard):
        if wizard.choosetype.workpiece == 2:
            N10x = str(float(wizard.Detailpara.SubDia) + 10)
            N30x = wizard.Detailpara.SubDia
            N30z = '-' + wizard.Detailpara.SUbArcWidth
            N30cr = wizard.Detailpara.SubArcRadius
            N40z = '-' + str(float(wizard.Detailpara.SubLong) - float(wizard.Detailpara.SUbArcWidth))
            N50x = str(float(wizard.Detailpara.SubDia) + 2 * float(wizard.Detailpara.SubArcRadius) * math.sin(90 - float(wizard.Detailpara.SubArcAngle)))
            N50z = '-' + wizard.Detailpara.SubLong
            N50cr = wizard.Detailpara.SubArcRadius
            with open('../templates/1crankpin.MPF', 'r', encoding='utf-8', errors="ignore") as f:
                s = f.read()
            self.MainText.setPlainText(s %(wizard.basicpara.cutter, wizard.basicpara.cuttercompen, wizard.basicpara.revolving, wizard.basicpara.feedspeed, wizard.basicpara.x, wizard.basicpara.y))

            with open('../templates/1crankpin_sub.SPF', 'r', encoding='utf-8', errors="ignore") as f:
                s = f.read()
            self.SubText.setPlainText(s %(N10x, N30x, N30z, N30cr, N40z, N50x, N50z, N50cr))

        elif wizard.choosetype.workpiece == 1:
            N10x = str(float(wizard.Detailpara.MainDia) + 10)
            N30x = wizard.Detailpara.MainDia
            N30z = '-' + wizard.Detailpara.MainArcWidth1
            N30cr = wizard.Detailpara.MainArcRadius1
            N40z = '-' + str(float(wizard.Detailpara.MainLong) - float(wizard.Detailpara.MainArcWidth1))
            N50x = str(float(wizard.Detailpara.MainDia) + 2 * float(wizard.Detailpara.MainArcRadius1) * math.sin(
                90 - float(wizard.Detailpara.MainArcAngle1)))
            N50z = '-' + wizard.Detailpara.MainLong
            N50cr = wizard.Detailpara.MainArcRadius1
            with open('../templates/1crankpin.MPF', 'r', encoding='utf-8', errors="ignore") as f:
                s = f.read()
            self.MainText.setPlainText(s %(wizard.basicpara.cutter, wizard.basicpara.cuttercompen, wizard.basicpara.revolving, wizard.basicpara.feedspeed, wizard.basicpara.x, wizard.basicpara.y))

            with open('../templates/1crankpin_sub.SPF', 'r', encoding='utf-8', errors="ignore") as f:
                s = f.read()
            self.SubText.setPlainText(s %(N10x, N30x, N30z, N30cr, N40z, N50x, N50z, N50cr))


        else:
            initalx = str(float(wizard.Detailpara.MainDia) + 10)
            G2x = wizard.Detailpara.MainDia
            arcw1 = wizard.Detailpara.MainArcWidth1
            G2z = '-' + wizard.Detailpara.MainArcWidth1
            G2cr = wizard.Detailpara.MainArcRadius1
            ml = wizard.Detailpara.MainLong
            cw1 = wizard.Detailpara.ChamferAngleWidth1
            G1z = '-' + str(float(ml) - float(cw1))
            N50x = str(float(G2x) - 2 * float(cw1) * math.tan(float(wizard.Detailpara.ChamferAngle1)))
            N50z = '-' + ml
            N60x = wizard.Detailpara.LongDia
            N60z = '-' + str(float(ml) + float(wizard.Detailpara.MainArcRadius2))
            N60cr = wizard.Detailpara.MainArcRadius2
            N70z = '-' + str(float(ml) + float(wizard.Detailpara.LongWidth) - float(wizard.Detailpara.ChamferAngleWidth2))
            N80x = str(float(wizard.Detailpara.LongDia) - 2 * float(wizard.Detailpara.ChamferAngleWidth2) * math.tan(float(wizard.Detailpara.ChamferAngle2)))
            N80z = '-' + str(float(ml) + float(wizard.Detailpara.LongWidth))
            with open('../templates/1main.MPF', 'r', encoding='utf-8', errors="ignore") as f:
                s = f.read()
            self.MainText.setPlainText(s %(wizard.basicpara.cutter, wizard.basicpara.cuttercompen, wizard.basicpara.revolving, wizard.basicpara.feedspeed, wizard.basicpara.x, wizard.basicpara.y))

            with open('../templates/1main_sub.SPF', 'r', encoding='utf-8', errors="ignore") as f:
                s = f.read()
            self.SubText.setPlainText(s %(initalx, G2x, G2z, G2cr, G1z, N50x, N50z, N60x, N60z
                                          , N60cr, N70z, N80x, N80z))







if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MyWindow = MainWindow()
    MyWindow.show()
    sys.exit(app.exec_())



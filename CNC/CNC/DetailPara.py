#!/usr/bin/env python
# encoding: utf-8
'''
@author: lizhyun
@license: 
@contact: 
@software: 
@file: DetailPara.py
@time: 19-1-2 上午10:46
@desc:
'''
from PyQt5 import QtCore, QtGui, QtWidgets
import CNC.choosetype
class DetailPara(QtWidgets.QWizardPage):
    MainDia = 0
    MainLong = 0
    LongDia = 0
    LongWidth = 0
    ChamferAngle1 = 0
    ChamferAngle2 = 0
    ChamferAngleWidth1 = 0
    ChamferAngleWidth2 = 0
    MainArcRadius1 = 0
    MainArcWidth1 = 0
    MainArcAngle1 = 0
    MainArcRadius2 = 0
    SubDia = 0
    SubLong = 0
    SubArcRadius = 0
    SUbArcWidth = 0
    SubArcAngle = 0


    def __init__(self):
        super(DetailPara, self).__init__()
        self.setup()

    def setup(self):
        self.setObjectName("Detailpara")
        self.widget1 = QtWidgets.QWidget(self)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 471, 291))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.SubBox = QtWidgets.QGroupBox(self.widget1)
        self.SubBox.setObjectName("SubBox")
        self.widget2 = QtWidgets.QWidget(self.SubBox)
        self.widget2.setGeometry(QtCore.QRect(10, 40, 440, 60))
        self.widget2.setObjectName("widget2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SubDiaLabel = QtWidgets.QLabel(self.widget2)
        self.SubDiaLabel.setObjectName("SubDiaLabel")
        self.horizontalLayout_2.addWidget(self.SubDiaLabel)
        self.SubDiaText = QtWidgets.QLineEdit(self.widget2)
        self.SubDiaText.setObjectName("SubDiaText")
        self.horizontalLayout_2.addWidget(self.SubDiaText)
        self.SubLongLabel = QtWidgets.QLabel(self.widget2)
        self.SubLongLabel.setObjectName("SubLongLabel")
        self.horizontalLayout_2.addWidget(self.SubLongLabel)
        self.SubLongText = QtWidgets.QLineEdit(self.widget2)
        self.SubLongText.setObjectName("SubLongText")
        self.horizontalLayout_2.addWidget(self.SubLongText)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.SubArcLabel = QtWidgets.QLabel(self.widget2)
        self.SubArcLabel.setObjectName("SubArcLabel")
        self.gridLayout_6.addWidget(self.SubArcLabel, 1, 0, 1, 1)
        self.SubArcText = QtWidgets.QLineEdit(self.widget2)
        self.SubArcText.setObjectName("SubArcText")
        self.gridLayout_6.addWidget(self.SubArcText, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.SubBox, 1, 0, 1, 1)
        self.MainBox = QtWidgets.QGroupBox(self.widget1)
        self.MainBox.setObjectName("MainBox")
        self.widget3 = QtWidgets.QWidget(self.MainBox)
        self.widget3.setGeometry(QtCore.QRect(10, 30, 440, 91))
        self.widget3.setObjectName("widget3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.MainLabel = QtWidgets.QLabel(self.widget3)
        self.MainLabel.setObjectName("MainLabel")
        self.gridLayout_4.addWidget(self.MainLabel, 0, 0, 1, 1)
        self.MainText = QtWidgets.QLineEdit(self.widget3)
        self.MainText.setObjectName("MainText")
        self.gridLayout_4.addWidget(self.MainText, 0, 1, 1, 1)
        self.LongLabel = QtWidgets.QLabel(self.widget3)
        self.LongLabel.setObjectName("LongLabel")
        self.gridLayout_4.addWidget(self.LongLabel, 0, 2, 1, 1)
        self.LongText = QtWidgets.QLineEdit(self.widget3)
        self.LongText.setObjectName("LongText")
        self.gridLayout_4.addWidget(self.LongText, 0, 3, 1, 1)
        self.ChamferLabel1 = QtWidgets.QLabel(self.widget3)
        self.ChamferLabel1.setObjectName("ChamferLabel1")
        self.gridLayout_4.addWidget(self.ChamferLabel1, 1, 0, 1, 1)
        self.ChamferText1 = QtWidgets.QLineEdit(self.widget3)
        self.ChamferText1.setObjectName("ChamferText1")
        self.gridLayout_4.addWidget(self.ChamferText1, 1, 1, 1, 1)
        self.ChamferLabel2 = QtWidgets.QLabel(self.widget3)
        self.ChamferLabel2.setObjectName("ChamferLabel2")
        self.gridLayout_4.addWidget(self.ChamferLabel2, 1, 2, 1, 1)
        self.ChamferText2 = QtWidgets.QLineEdit(self.widget3)
        self.ChamferText2.setObjectName("ChamferText2")
        self.gridLayout_4.addWidget(self.ChamferText2, 1, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 2)
        self.ArcLabel = QtWidgets.QLabel(self.widget3)
        self.ArcLabel.setObjectName("ArcLabel")
        self.gridLayout_5.addWidget(self.ArcLabel, 1, 0, 1, 1)
        self.ArcText = QtWidgets.QLineEdit(self.widget3)
        self.ArcText.setObjectName("ArcText")
        self.gridLayout_5.addWidget(self.ArcText, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.MainBox, 0, 0, 1, 1)

        self.retranslateUI()

    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.SubBox.setTitle(_translate("Wizard", "连杆颈"))
        self.SubDiaLabel.setText(_translate("Wizard", "连杆颈直径*"))
        self.SubLongLabel.setText(_translate("Wizard", "连杆颈宽*"))
        self.SubArcLabel.setText(_translate("Wizard", "圆弧(半径 宽度 角度)*"))
        self.MainBox.setTitle(_translate("Wizard", "主轴颈*"))
        self.MainLabel.setText(_translate("Wizard", "主轴(直径 长度)*"))
        self.LongLabel.setText(_translate("Wizard", "长轴(直径 长度)*"))
        self.ChamferLabel1.setText(_translate("Wizard", "倒角一(角度 宽度)*"))
        self.ChamferLabel2.setText(_translate("Wizard", "倒角二(角度 宽度)*"))
        self.ArcLabel.setText(_translate("Wizard", "圆弧(半径1 宽度 角度  半径2)*"))

    def initializePage(self):
        self.SubBox.setDisabled(False)
        self.MainBox.setDisabled(False)
        self.SubBox.setDisabled(False)
        self.LongText.setDisabled(False)
        self.ChamferText1.setDisabled(False)
        self.ChamferText2.setDisabled(False)
        self.ArcLabel.setText("圆弧(半径1 宽度 角度 半径2)")
        if CNC.choosetype.ChooseType.workpiece == 2:
            self.MainBox.setDisabled(True)
            self.registerField("SubDia*", self.SubDiaText)
            self.registerField("SubWidth*", self.SubLongText)
            self.registerField("SubArc*", self.SubArcText)

        elif CNC.choosetype.ChooseType.workpiece == 1:
            self.SubBox.setDisabled(True)
            self.LongText.setDisabled(True)
            self.ChamferText1.setDisabled(True)
            self.ChamferText2.setDisabled(True)
            self.ArcLabel.setText("圆弧(半径 宽度 角度)")
            self.registerField("Main*", self.MainText)
            self.registerField("MainArc*", self.ArcText)
        else:
            self.SubBox.setDisabled(True)
            self.registerField("Main*", self.MainText)
            self.registerField("MainArc*", self.ArcText)
            self.registerField("Long*", self.LongText)
            self.registerField("Chamfer1*", self.ChamferText1)
            self.registerField("Chamfer2*", self.ChamferText2)

    def validatePage(self):
        if CNC.choosetype.ChooseType.workpiece == 0:
            DetailPara.MainDia, DetailPara.MainLong = self.MainText.text().split(" ")
            DetailPara.LongDia, DetailPara.LongWidth = self.LongText.text().split(" ")
            DetailPara.ChamferAngle1, DetailPara.ChamferAngleWidth1 = self.ChamferText1.text().split(" ")
            DetailPara.ChamferAngle2, DetailPara.ChamferAngleWidth2 = self.ChamferText2.text().split(" ")
            DetailPara.MainArcRadius1, DetailPara.MainArcWidth1, DetailPara.MainArcAngle1, DetailPara.MainArcRadius2 = self.ArcText.text().split(" ")

        elif CNC.choosetype.ChooseType.workpiece == 1:
            DetailPara.MainDia, DetailPara.MainLong = self.MainText.text().split(" ")
            DetailPara.MainArcRadius1, DetailPara.MainArcWidth1, DetailPara.MainArcAngle1 = self.ArcText.text().split(" ")

        else:
            DetailPara.SubDia = self.SubDiaText.text()
            DetailPara.SubLong = self.SubLongText.text()
            DetailPara.SubArcRadius, DetailPara.SUbArcWidth, DetailPara.SubArcAngle = self.SubArcText.text().split(" ")

        return True

        # print("主轴直径 长度：" + DetailPara.MainDia, DetailPara.MainLong)
        # print("长轴直径 长度：" + DetailPara.LongDia, DetailPara.LongWidth)
        # print("倒角1角度 宽度：" + DetailPara.ChamferAngle1, DetailPara.ChamferAngleWidth1)
        # print("倒角2角度 宽度：" + DetailPara.ChamferAngle2, DetailPara.ChamferAngleWidth2)
        # print("主轴圆弧1半径 宽度 角度 圆弧2半径：" + DetailPara.MainArcRadius1, DetailPara.MainArcWidth1, DetailPara.MainArcAngle1, DetailPara.MainArcRadius2)
        # print("连杆颈直径 长度：" + DetailPara.SubDia, DetailPara.SubLong)
        # print("连杆颈圆弧半径 宽度 角度：" + DetailPara.SubArcRadius, DetailPara.SUbArcWidth, DetailPara.SubArcAngle)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = DetailPara()
    ui.setup()
    ui.show()
    sys.exit(app.exec_())
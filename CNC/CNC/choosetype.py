#!/usr/bin/env python
# encoding: utf-8
'''
@author: lizhyun
@license: 
@contact: 
@software: 
@file: choosetype.py
@time: 19-1-1 下午4:50
@desc:
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class ChooseType(QtWidgets.QWizardPage):

    workpiece = 0

    def __init__(self):
        super(ChooseType, self).__init__()
        self.setup()

    def setup(self):
        #self.setObjectName("choosetype")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(-10, 70, 401, 51))
        self.widget.setObjectName("widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.TypeLabel = QtWidgets.QLabel(self.widget)
        self.TypeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TypeLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TypeLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TypeLabel.setMidLineWidth(0)
        self.TypeLabel.setObjectName("TypeLabel")
        self.gridLayout_7.addWidget(self.TypeLabel, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_7.addWidget(self.comboBox, 0, 1, 1, 1)

        self.retranslateUI()

    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.setTitle(_translate("Wizard", "请选择加工工件"))
        self.setSubTitle(_translate("Wizard", "主轴颈 | 连杆颈"))
        self.TypeLabel.setText(_translate("Wizard", "<html><head/><body><p align=\"right\">工件类型：</p></body></html>"))
        self.comboBox.setItemText(0, _translate("Wizard", "主轴颈一"))
        self.comboBox.setItemText(1, _translate("Wizard", "主轴颈二"))
        self.comboBox.setItemText(2, _translate("Wizard", "连杆颈"))

    def validatePage(self):
        ChooseType.workpiece = self.comboBox.currentIndex()

        #print(ChooseType.workpiece)
        return True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ChooseType()
    ui.setup()
    ui.show()
    sys.exit(app.exec_())
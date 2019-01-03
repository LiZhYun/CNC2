#!/usr/bin/env python
# encoding: utf-8
'''
@author: lizhyun
@license: 
@contact: 
@software: 
@file: BasicPara.py
@time: 19-1-2 上午10:38
@desc:
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class BasicPara(QtWidgets.QWizardPage):
    cutter = 0
    cuttercompen = 0
    x = 0
    y = 0
    feedspeed = 0
    revolving = 0

    def __init__(self):
        super(BasicPara, self).__init__()
        self.setup()

    def setup(self):
        self.setEnabled(True)
        self.setMinimumSize(QtCore.QSize(0, 121))
        self.setObjectName("basicpara")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.CompenSpin = QtWidgets.QSpinBox(self)
        self.CompenSpin.setObjectName("CompenSpin")
        self.gridLayout.addWidget(self.CompenSpin, 1, 1, 1, 1)
        self.FeedLabel = QtWidgets.QLabel(self)
        self.FeedLabel.setObjectName("FeedLabel")
        self.gridLayout.addWidget(self.FeedLabel, 1, 3, 1, 1)
        self.FeedText = QtWidgets.QLineEdit(self)
        self.FeedText.setObjectName("FeedText")
        self.gridLayout.addWidget(self.FeedText, 1, 4, 1, 1)
        self.CoordinateText = QtWidgets.QLineEdit(self)
        self.CoordinateText.setObjectName("CoordinateText")
        self.gridLayout.addWidget(self.CoordinateText, 0, 4, 1, 1)
        self.CompenLabel = QtWidgets.QLabel(self)
        self.CompenLabel.setObjectName("CompenLabel")
        self.gridLayout.addWidget(self.CompenLabel, 1, 0, 1, 1)
        self.CutterSpin = QtWidgets.QSpinBox(self)
        self.CutterSpin.setWrapping(False)
        self.CutterSpin.setObjectName("CutterSpin")
        self.gridLayout.addWidget(self.CutterSpin, 0, 1, 1, 1)
        self.CutterLabel = QtWidgets.QLabel(self)
        self.CutterLabel.setObjectName("CutterLabel")
        self.gridLayout.addWidget(self.CutterLabel, 0, 0, 1, 1)
        self.CorrdinateLabel = QtWidgets.QLabel(self)
        self.CorrdinateLabel.setObjectName("CorrdinateLabel")
        self.gridLayout.addWidget(self.CorrdinateLabel, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.RevolvingLabel = QtWidgets.QLabel(self)
        self.RevolvingLabel.setObjectName("RevolvingLabel")
        self.gridLayout_2.addWidget(self.RevolvingLabel, 1, 0, 1, 1)
        self.RevolvingText = QtWidgets.QLineEdit(self)
        self.RevolvingText.setObjectName("RevolvingText")
        self.gridLayout_2.addWidget(self.RevolvingText, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.retranslateUI()
        self.registerField("Feed*", self.FeedText)
        self.registerField("Revolving*", self.RevolvingText)
        self.registerField("Coordinate*", self.CoordinateText)


    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.setTitle(_translate("Wizard", "基础参数"))
        self.setSubTitle(_translate("Wizard", "刀具选择 | 进给 | 转速"))
        self.FeedLabel.setText(_translate("Wizard", "进给(mm/r)*"))
        self.CompenLabel.setText(_translate("Wizard", "刀补"))
        self.CutterLabel.setText(_translate("Wizard", "刀具"))
        self.CorrdinateLabel.setText(_translate("Wizard", "起始坐标(x,y)*"))
        self.RevolvingLabel.setText(_translate("Wizard", "主轴转速（r/min)*"))


    def validatePage(self):
        BasicPara.cutter = self.CutterSpin.text()
        BasicPara.cuttercompen = self.CompenSpin.text()
        BasicPara.feedspeed = self.FeedText.text()
        BasicPara.revolving = self.RevolvingText.text()
        BasicPara.x, BasicPara. y = self.CoordinateText.text().split(",")

        #print(BasicPara.cutter, BasicPara.cuttercompen, BasicPara.feedspeed, BasicPara.revolving, BasicPara.x , BasicPara. y)

        return True
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = BasicPara()
    ui.setup()
    ui.show()
    sys.exit(app.exec_())
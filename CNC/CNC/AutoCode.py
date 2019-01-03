# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoCode.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyWindow(object):
    def setupUi(self, MyWindow):
        MyWindow.setObjectName("MyWindow")
        MyWindow.setWindowModality(QtCore.Qt.WindowModal)
        MyWindow.setEnabled(True)
        MyWindow.resize(611, 516)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MyWindow.sizePolicy().hasHeightForWidth())
        MyWindow.setSizePolicy(sizePolicy)
        MyWindow.setMinimumSize(QtCore.QSize(611, 516))
        MyWindow.setMaximumSize(QtCore.QSize(611, 516))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/bulb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MyWindow.setWindowIcon(icon)
        MyWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MyWindow.setAutoFillBackground(False)
        MyWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MyWindow.setAnimated(True)
        MyWindow.setDocumentMode(False)
        MyWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MyWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(0, 0, 611, 461))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.MainLabel = QtWidgets.QLabel(self.splitter)
        self.MainLabel.setObjectName("MainLabel")
        self.SubLabel = QtWidgets.QLabel(self.splitter)
        self.SubLabel.setLineWidth(1)
        self.SubLabel.setMidLineWidth(20)
        self.SubLabel.setScaledContents(False)
        self.SubLabel.setWordWrap(False)
        self.SubLabel.setIndent(-1)
        self.SubLabel.setOpenExternalLinks(False)
        self.SubLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.SubLabel.setObjectName("SubLabel")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.MainText = QtWidgets.QPlainTextEdit(self.splitter_2)
        self.MainText.setObjectName("MainText")
        self.SubText = QtWidgets.QPlainTextEdit(self.splitter_2)
        self.SubText.setMidLineWidth(0)
        self.SubText.setUndoRedoEnabled(True)
        self.SubText.setBackgroundVisible(False)
        self.SubText.setObjectName("SubText")
        MyWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MyWindow)
        self.statusbar.setObjectName("statusbar")
        MyWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MyWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(36, 36))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MyWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.Export = QtWidgets.QAction(MyWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Export.setIcon(icon1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Export.setFont(font)
        self.Export.setObjectName("Export")
        self.Open = QtWidgets.QAction(MyWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/file-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Open.setIcon(icon2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Open.setFont(font)
        self.Open.setObjectName("Open")
        self.Edit = QtWidgets.QAction(MyWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/edit-square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Edit.setIcon(icon3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Edit.setFont(font)
        self.Edit.setObjectName("Edit")
        self.toolBar.addAction(self.Export)
        self.toolBar.addAction(self.Open)
        self.toolBar.addAction(self.Edit)

        self.retranslateUi(MyWindow)

        QtCore.QMetaObject.connectSlotsByName(MyWindow)

    def retranslateUi(self, MyWindow):
        _translate = QtCore.QCoreApplication.translate
        MyWindow.setWindowTitle(_translate("MyWindow", "AutoCode"))
        self.MainLabel.setText(_translate("MyWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">主程序</span></p></body></html>"))
        self.SubLabel.setText(_translate("MyWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">子程序</span></p></body></html>"))
        self.toolBar.setWindowTitle(_translate("MyWindow", "toolBar"))
        self.Export.setText(_translate("MyWindow", "导出"))
        self.Export.setToolTip(_translate("MyWindow", "导出文件"))
        self.Open.setText(_translate("MyWindow", "打开"))
        self.Open.setToolTip(_translate("MyWindow", "打开文件"))
        self.Edit.setText(_translate("MyWindow", "编辑"))
        self.Edit.setToolTip(_translate("MyWindow", "编辑尺寸"))

import lizhyun_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyWindow = QtWidgets.QMainWindow()
    ui = Ui_MyWindow()
    ui.setupUi(MyWindow)
    MyWindow.show()
    sys.exit(app.exec_())

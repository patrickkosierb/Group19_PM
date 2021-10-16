# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aoo_mode.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(0, 85, 9, 255), stop:1 rgba(255, 147, 147, 255));}")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(420, 0, 481, 111))
        self.label.setStyleSheet("font: 24pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 100, 451, 111))
        self.label_2.setStyleSheet("font: 18pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label_2.setObjectName("label_2")
        self.connected = QtWidgets.QLabel(self.bgwidget)
        self.connected.setGeometry(QtCore.QRect(950, 30, 241, 51))
        self.connected.setStyleSheet("font: 14pt \"Arial\"; color:rgb(0, 255, 0)\n"
"")
        self.connected.setText("")
        self.connected.setObjectName("connected")
        self.disconnected = QtWidgets.QLabel(self.bgwidget)
        self.disconnected.setGeometry(QtCore.QRect(950, 30, 241, 51))
        self.disconnected.setStyleSheet("font: 14pt \"Arial\"; color:rgb(255, 0, 0)\n"
"")
        self.disconnected.setText("")
        self.disconnected.setObjectName("disconnected")
        self.pacemaker_number = QtWidgets.QLabel(self.bgwidget)
        self.pacemaker_number.setGeometry(QtCore.QRect(10, 40, 241, 51))
        self.pacemaker_number.setStyleSheet("font: 10pt \"Arial\"; color:rgb(255,255,255)\n"
"")
        self.pacemaker_number.setText("")
        self.pacemaker_number.setObjectName("pacemaker_number")
        self.label_6 = QtWidgets.QLabel(self.bgwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 200, 161, 41))
        self.label_6.setStyleSheet("font: 12pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.bgwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 275, 151, 51))
        self.label_7.setStyleSheet("font: 12pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.bgwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 350, 141, 41))
        self.label_8.setStyleSheet("font: 12pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.bgwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 425, 161, 41))
        self.label_9.setStyleSheet("font: 12pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(self.bgwidget)
        self.label_13.setGeometry(QtCore.QRect(810, 100, 451, 111))
        self.label_13.setStyleSheet("font: 14pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.bgwidget)
        self.label_14.setGeometry(QtCore.QRect(1040, 100, 451, 111))
        self.label_14.setStyleSheet("font: 14pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label_14.setObjectName("label_14")
        self.line = QtWidgets.QFrame(self.bgwidget)
        self.line.setGeometry(QtCore.QRect(-13, 90, 1321, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.bgwidget)
        self.line_2.setGeometry(QtCore.QRect(370, -10, 21, 861))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.ApplyChanges = QtWidgets.QPushButton(self.bgwidget)
        self.ApplyChanges.setGeometry(QtCore.QRect(970, 730, 211, 51))
        self.ApplyChanges.setStyleSheet("border-radius: 20px;\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(255, 255, 216);\n"
"font: 12pt \"Arial\";")
        self.ApplyChanges.setObjectName("ApplyChanges")
        self.ResetChanges = QtWidgets.QPushButton(self.bgwidget)
        self.ResetChanges.setGeometry(QtCore.QRect(730, 730, 211, 51))
        self.ResetChanges.setStyleSheet("border-radius: 20px;\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(255, 216, 216);\n"
"font: 12pt \"Arial\";")
        self.ResetChanges.setObjectName("ResetChanges")
        self.checkBox = QtWidgets.QCheckBox(self.bgwidget)
        self.checkBox.setGeometry(QtCore.QRect(420, 705, 191, 20))
        self.checkBox.setStyleSheet("color: rgb(255,255,255)")
        self.checkBox.setObjectName("checkBox")
        self.aai = QtWidgets.QPushButton(self.bgwidget)
        self.aai.setGeometry(QtCore.QRect(15, 240, 351, 51))
        self.aai.setStyleSheet("border-radius: 20px;\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(255, 255, 216);\n"
"font: 12pt \"Arial\";")
        self.aai.setObjectName("aai")
        self.LRL_Current = QtWidgets.QLabel(self.bgwidget)
        self.LRL_Current.setGeometry(QtCore.QRect(840, 210, 71, 21))
        self.LRL_Current.setStyleSheet("color: rgb(255,255,255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.LRL_Current.setObjectName("LRL_Current")
        self.URL_Current = QtWidgets.QLabel(self.bgwidget)
        self.URL_Current.setGeometry(QtCore.QRect(840, 285, 71, 21))
        self.URL_Current.setStyleSheet("color: rgb(255,255,255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.URL_Current.setObjectName("URL_Current")
        self.AA_Current = QtWidgets.QLabel(self.bgwidget)
        self.AA_Current.setGeometry(QtCore.QRect(840, 360, 71, 21))
        self.AA_Current.setStyleSheet("color: rgb(255,255,255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.AA_Current.setObjectName("AA_Current")
        self.APW_Current = QtWidgets.QLabel(self.bgwidget)
        self.APW_Current.setGeometry(QtCore.QRect(840, 435, 71, 21))
        self.APW_Current.setStyleSheet("color: rgb(255,255,255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.APW_Current.setObjectName("APW_Current")
        self.aoo = QtWidgets.QPushButton(self.bgwidget)
        self.aoo.setGeometry(QtCore.QRect(15, 140, 351, 51))
        self.aoo.setStyleSheet("border-radius: 20px;\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(255, 255, 216);\n"
"font: 12pt \"Arial\";")
        self.aoo.setObjectName("aoo")
        self.logout = QtWidgets.QPushButton(self.bgwidget)
        self.logout.setGeometry(QtCore.QRect(230, 55, 141, 41))
        self.logout.setStyleSheet("border-radius: 6px;\n"
"\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(155, 155, 155);\n"
"font: 75 12pt \"Arial\";")
        self.logout.setObjectName("logout")
        self.user_display = QtWidgets.QLabel(self.bgwidget)
        self.user_display.setGeometry(QtCore.QRect(10, 0, 161, 41))
        self.user_display.setStyleSheet("font: 12pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.user_display.setText("")
        self.user_display.setObjectName("user_display")
        self.account = QtWidgets.QPushButton(self.bgwidget)
        self.account.setGeometry(QtCore.QRect(230, 10, 141, 41))
        self.account.setStyleSheet("border-radius: 6px;\n"
"\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(0, 100, 255);\n"
"font: 75 12pt \"Arial\";")
        self.account.setObjectName("account")
        self.voo = QtWidgets.QPushButton(self.bgwidget)
        self.voo.setGeometry(QtCore.QRect(15, 340, 351, 51))
        self.voo.setStyleSheet("border-radius: 20px;\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(255, 255, 216);\n"
"font: 12pt \"Arial\";")
        self.voo.setObjectName("voo")
        self.vvi = QtWidgets.QPushButton(self.bgwidget)
        self.vvi.setGeometry(QtCore.QRect(15, 440, 351, 51))
        self.vvi.setStyleSheet("border-radius: 20px;\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(255, 255, 216);\n"
"font: 12pt \"Arial\";")
        self.vvi.setObjectName("vvi")
        self.LRL = QtWidgets.QLineEdit(self.bgwidget)
        self.LRL.setGeometry(QtCore.QRect(1050, 210, 51, 22))
        self.LRL.setObjectName("LRL")
        self.URL = QtWidgets.QLineEdit(self.bgwidget)
        self.URL.setGeometry(QtCore.QRect(1050, 285, 51, 22))
        self.URL.setObjectName("URL")
        self.AA = QtWidgets.QLineEdit(self.bgwidget)
        self.AA.setGeometry(QtCore.QRect(1050, 360, 51, 22))
        self.AA.setObjectName("AA")
        self.APW = QtWidgets.QLineEdit(self.bgwidget)
        self.APW.setGeometry(QtCore.QRect(1050, 435, 51, 22))
        self.APW.setObjectName("APW")
        self.INVALID = QtWidgets.QLabel(self.bgwidget)
        self.INVALID.setGeometry(QtCore.QRect(960, 210, 81, 31))
        self.INVALID.setStyleSheet("font: 8pt \"Arial\"; color:rgb(255, 0, 0)\n"
"")
        self.INVALID.setText("")
        self.INVALID.setObjectName("INVALID")
        self.INVALID_2 = QtWidgets.QLabel(self.bgwidget)
        self.INVALID_2.setGeometry(QtCore.QRect(960, 285, 81, 31))
        self.INVALID_2.setStyleSheet("font: 8pt \"Arial\"; color:rgb(255, 0, 0)\n"
"")
        self.INVALID_2.setText("")
        self.INVALID_2.setObjectName("INVALID_2")
        self.INVALID_3 = QtWidgets.QLabel(self.bgwidget)
        self.INVALID_3.setGeometry(QtCore.QRect(960, 360, 61, 31))
        self.INVALID_3.setStyleSheet("font: 8pt \"Arial\"; color:rgb(255, 0, 0)\n"
"")
        self.INVALID_3.setText("")
        self.INVALID_3.setObjectName("INVALID_3")
        self.INVALID_4 = QtWidgets.QLabel(self.bgwidget)
        self.INVALID_4.setGeometry(QtCore.QRect(960, 435, 81, 31))
        self.INVALID_4.setStyleSheet("font: 8pt \"Arial\"; color:rgb(255, 0, 0)\n"
"")
        self.INVALID_4.setText("")
        self.INVALID_4.setObjectName("INVALID_4")
        self.line_3 = QtWidgets.QFrame(self.bgwidget)
        self.line_3.setGeometry(QtCore.QRect(380, 690, 981, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.update_pm = QtWidgets.QPushButton(self.bgwidget)
        self.update_pm.setGeometry(QtCore.QRect(420, 730, 211, 51))
        self.update_pm.setStyleSheet("border-radius: 20px;\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(0, 155, 0);\n"
"font: 12pt \"Arial\";")
        self.update_pm.setObjectName("update_pm")
        self.INVALID_5 = QtWidgets.QLabel(self.bgwidget)
        self.INVALID_5.setGeometry(QtCore.QRect(610, 700, 241, 31))
        self.INVALID_5.setStyleSheet("font: 8pt \"Arial\"; color:rgb(255, 0, 0)\n"
"")
        self.INVALID_5.setText("")
        self.INVALID_5.setObjectName("INVALID_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Atrium Pacing Mode(AOO)"))
        self.label_2.setText(_translate("Dialog", "Mode Parameters:"))
        self.label_6.setText(_translate("Dialog", "Lower Rate Limit"))
        self.label_7.setText(_translate("Dialog", "Upper Rate Limit"))
        self.label_8.setText(_translate("Dialog", "Atrial Amplitude"))
        self.label_9.setText(_translate("Dialog", "Atrial Pulse Width"))
        self.label_13.setText(_translate("Dialog", "Current"))
        self.label_14.setText(_translate("Dialog", "Updated"))
        self.ApplyChanges.setText(_translate("Dialog", "Apply Changes"))
        self.ResetChanges.setText(_translate("Dialog", "Reset Changes"))
        self.checkBox.setText(_translate("Dialog", "I have reviewed my changes "))
        self.aai.setText(_translate("Dialog", "AAI Mode"))
        self.LRL_Current.setText(_translate("Dialog", "0"))
        self.URL_Current.setText(_translate("Dialog", "0"))
        self.AA_Current.setText(_translate("Dialog", "0"))
        self.APW_Current.setText(_translate("Dialog", "0"))
        self.aoo.setText(_translate("Dialog", "AOO Mode"))
        self.logout.setText(_translate("Dialog", "Logout"))
        self.account.setText(_translate("Dialog", "Account"))
        self.voo.setText(_translate("Dialog", "VOO Mode"))
        self.vvi.setText(_translate("Dialog", "VVI Mode"))
        self.update_pm.setText(_translate("Dialog", "Upload to Pacemaker"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

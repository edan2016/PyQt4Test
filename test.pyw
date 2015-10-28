# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8


	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(400, 300)
		self.pushButton = QtGui.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(160, 200, 75, 23))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.lineEdit = QtGui.QLineEdit(Form)
		self.lineEdit.setGeometry(QtCore.QRect(150, 90, 113, 20))
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.pushButton_2 = QtGui.QPushButton(Form)
		self.pushButton_2.setGeometry(QtCore.QRect(160, 240, 75, 23))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

		self.retranslateUi(Form)
		QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClick)
		QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClick1)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "Form1", None))
		self.pushButton.setText(_translate("Form", "Hello!", None))
		self.pushButton_2.setText(_translate("Form", "Привет!", None))

	def buttonClick(self):
		self.lineEdit.setText("Hello!")

	def buttonClick1(self):
		self.lineEdit.setText("Привет!")



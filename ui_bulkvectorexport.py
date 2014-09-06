# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_bulkvectorexport.ui'
#
# Created: Wed Aug 27 20:57:00 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BulkVectorExportDialog(object):
    def setupUi(self, BulkVectorExportDialog):
        BulkVectorExportDialog.setObjectName(_fromUtf8("BulkVectorExportDialog"))
        BulkVectorExportDialog.resize(392, 141)
        BulkVectorExportDialog.setWindowTitle(QtGui.QApplication.translate("BulkVectorExportDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(BulkVectorExportDialog)
        self.buttonBox.setGeometry(QtCore.QRect(220, 100, 161, 32))
        self.buttonBox.setWhatsThis(_fromUtf8(""))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.dirEdit = QtGui.QLineEdit(BulkVectorExportDialog)
        self.dirEdit.setGeometry(QtCore.QRect(120, 40, 231, 20))
        self.dirEdit.setObjectName(_fromUtf8("dirEdit"))
        self.label = QtGui.QLabel(BulkVectorExportDialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label.setText(QtGui.QApplication.translate("BulkVectorExportDialog", "Save to dir:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(BulkVectorExportDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_2.setText(QtGui.QApplication.translate("BulkVectorExportDialog", "Output format", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formatBox = QtGui.QComboBox(BulkVectorExportDialog)
        self.formatBox.setGeometry(QtCore.QRect(120, 10, 271, 22))
        self.formatBox.setObjectName(_fromUtf8("formatBox"))
        self.layerCrsButton = QtGui.QRadioButton(BulkVectorExportDialog)
        self.layerCrsButton.setGeometry(QtCore.QRect(140, 70, 101, 17))
        self.layerCrsButton.setText(QtGui.QApplication.translate("BulkVectorExportDialog", "Layer CRS", None, QtGui.QApplication.UnicodeUTF8))
        self.layerCrsButton.setChecked(True)
        self.layerCrsButton.setObjectName(_fromUtf8("layerCrsButton"))
        self.projectCrsButton = QtGui.QRadioButton(BulkVectorExportDialog)
        self.projectCrsButton.setGeometry(QtCore.QRect(260, 70, 121, 17))
        self.projectCrsButton.setText(QtGui.QApplication.translate("BulkVectorExportDialog", "Project CRS", None, QtGui.QApplication.UnicodeUTF8))
        self.projectCrsButton.setObjectName(_fromUtf8("projectCrsButton"))
        self.dirButton = QtGui.QPushButton(BulkVectorExportDialog)
        self.dirButton.setGeometry(QtCore.QRect(360, 40, 31, 21))
        self.dirButton.setText(QtGui.QApplication.translate("BulkVectorExportDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.dirButton.setObjectName(_fromUtf8("dirButton"))

        self.retranslateUi(BulkVectorExportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BulkVectorExportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BulkVectorExportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BulkVectorExportDialog)

    def retranslateUi(self, BulkVectorExportDialog):
        pass


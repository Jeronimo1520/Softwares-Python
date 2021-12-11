# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo_registrar_consumoLWTpPe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogRegistrarconsumo(object):
    def setupUi(self, DialogRegistrarconsumo):
        if not DialogRegistrarconsumo.objectName():
            DialogRegistrarconsumo.setObjectName(u"DialogRegistrarconsumo")
        DialogRegistrarconsumo.resize(400, 167)
        self.verticalLayout = QVBoxLayout(DialogRegistrarconsumo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogRegistrarconsumo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEditDetalle = QLineEdit(self.frame)
        self.lineEditDetalle.setObjectName(u"lineEditDetalle")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditDetalle)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_Valor = QLineEdit(self.frame)
        self.lineEdit_Valor.setObjectName(u"lineEdit_Valor")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_Valor)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_Autorizado = QLineEdit(self.frame)
        self.lineEdit_Autorizado.setObjectName(u"lineEdit_Autorizado")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_Autorizado)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(DialogRegistrarconsumo)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogRegistrarconsumo)
        self.buttonBox.accepted.connect(DialogRegistrarconsumo.accept)
        self.buttonBox.rejected.connect(DialogRegistrarconsumo.reject)

        QMetaObject.connectSlotsByName(DialogRegistrarconsumo)
    # setupUi

    def retranslateUi(self, DialogRegistrarconsumo):
        DialogRegistrarconsumo.setWindowTitle(QCoreApplication.translate("DialogRegistrarconsumo", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogRegistrarconsumo", u"Detalle consumo", None))
        self.lineEditDetalle.setPlaceholderText(QCoreApplication.translate("DialogRegistrarconsumo", u"Obligatorio", None))
        self.label_2.setText(QCoreApplication.translate("DialogRegistrarconsumo", u"Valor", None))
        self.lineEdit_Valor.setPlaceholderText(QCoreApplication.translate("DialogRegistrarconsumo", u"Obligatorio", None))
        self.label_3.setText(QCoreApplication.translate("DialogRegistrarconsumo", u"Autorizado", None))
#if QT_CONFIG(whatsthis)
        self.lineEdit_Autorizado.setWhatsThis(QCoreApplication.translate("DialogRegistrarconsumo", u"<html><head/><body><p>Este campo es opcional.</p><p><br/></p><p>Se debe llenar cuando el consumo fue hecho por un autorizado del socio.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_Autorizado.setPlaceholderText(QCoreApplication.translate("DialogRegistrarconsumo", u"Opcional", None))
    # retranslateUi


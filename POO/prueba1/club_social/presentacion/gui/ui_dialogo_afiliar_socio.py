# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo_afiliar_socioLDjSEy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogAfiliarSocio(object):
    def setupUi(self, DialogAfiliarSocio):
        if not DialogAfiliarSocio.objectName():
            DialogAfiliarSocio.setObjectName(u"DialogAfiliarSocio")
        DialogAfiliarSocio.resize(400, 136)
        self.verticalLayout = QVBoxLayout(DialogAfiliarSocio)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogAfiliarSocio)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEditCedula = QLineEdit(self.frame)
        self.lineEditCedula.setObjectName(u"lineEditCedula")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditCedula)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEditNombre = QLineEdit(self.frame)
        self.lineEditNombre.setObjectName(u"lineEditNombre")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditNombre)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(DialogAfiliarSocio)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogAfiliarSocio)
        self.buttonBox.accepted.connect(DialogAfiliarSocio.accept)
        self.buttonBox.rejected.connect(DialogAfiliarSocio.reject)

        QMetaObject.connectSlotsByName(DialogAfiliarSocio)
    # setupUi

    def retranslateUi(self, DialogAfiliarSocio):
        DialogAfiliarSocio.setWindowTitle(QCoreApplication.translate("DialogAfiliarSocio", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogAfiliarSocio", u"C\u00e9dula", None))
        self.lineEditCedula.setPlaceholderText(QCoreApplication.translate("DialogAfiliarSocio", u"Obligatorio", None))
        self.label_2.setText(QCoreApplication.translate("DialogAfiliarSocio", u"Nombre", None))
        self.lineEditNombre.setPlaceholderText(QCoreApplication.translate("DialogAfiliarSocio", u"Obligatorio", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_club_socialjVFBUL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1081, 849)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.label.setPixmap(QPixmap(u"img/banner_club.jpg"))

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listViewSocios = QListView(self.groupBox)
        self.listViewSocios.setObjectName(u"listViewSocios")

        self.verticalLayout_3.addWidget(self.listViewSocios)

        self.pbuttonAfiliarSocio = QPushButton(self.groupBox)
        self.pbuttonAfiliarSocio.setObjectName(u"pbuttonAfiliarSocio")

        self.verticalLayout_3.addWidget(self.pbuttonAfiliarSocio)


        self.horizontalLayout.addWidget(self.groupBox)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEditCedula = QLineEdit(self.groupBox_2)
        self.lineEditCedula.setObjectName(u"lineEditCedula")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditCedula)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_Nombre = QLineEdit(self.groupBox_2)
        self.lineEdit_Nombre.setObjectName(u"lineEdit_Nombre")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_Nombre)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.pbuttonRegistrarConsumo = QPushButton(self.frame_3)
        self.pbuttonRegistrarConsumo.setObjectName(u"pbuttonRegistrarConsumo")

        self.verticalLayout_4.addWidget(self.pbuttonRegistrarConsumo)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.listView_Facturas = QListView(self.groupBox_3)
        self.listView_Facturas.setObjectName(u"listView_Facturas")

        self.verticalLayout_5.addWidget(self.listView_Facturas)

        self.pbuttonPagarFactura = QPushButton(self.groupBox_3)
        self.pbuttonPagarFactura.setObjectName(u"pbuttonPagarFactura")

        self.verticalLayout_5.addWidget(self.pbuttonPagarFactura)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.listWidgetAutorizados = QListWidget(self.groupBox_4)
        self.listWidgetAutorizados.setObjectName(u"listWidgetAutorizados")

        self.verticalLayout_6.addWidget(self.listWidgetAutorizados)

        self.pbuttonAgregarAutorizado = QPushButton(self.groupBox_4)
        self.pbuttonAgregarAutorizado.setObjectName(u"pbuttonAgregarAutorizado")

        self.verticalLayout_6.addWidget(self.pbuttonAgregarAutorizado)


        self.verticalLayout_2.addWidget(self.groupBox_4)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Lista de socios", None))
        self.pbuttonAfiliarSocio.setText(QCoreApplication.translate("MainWindow", u"Afiliar Socio", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Datos del socio", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"C\u00e9dula", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.pbuttonRegistrarConsumo.setText(QCoreApplication.translate("MainWindow", u"Registrar consumo", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Facturas pendientes", None))
        self.pbuttonPagarFactura.setText(QCoreApplication.translate("MainWindow", u"Pagar factura", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Listado de autorizados", None))
        self.pbuttonAgregarAutorizado.setText(QCoreApplication.translate("MainWindow", u"Agregar autorizado", None))
    # retranslateUi


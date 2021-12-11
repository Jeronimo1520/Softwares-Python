import sys

from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator, QIntValidator, QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox

from club_social.mundo.errores import SocioExistenteError, SocioNoExistenteError
from club_social.mundo.mundo import Club
from club_social.presentacion.gui.ui_dialogo_afiliar_socio import Ui_DialogAfiliarSocio
from club_social.presentacion.gui.ui_dialogo_registrar_consumo import Ui_DialogRegistrarconsumo
from club_social.presentacion.gui.ui_main_window_club_social import Ui_MainWindow


class VentanaClubSocial(QMainWindow):
    def __init__(self, club: Club):
        QMainWindow.__init__(self)
        self.club = club
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._configurar()
        self.setFixedSize(1028, 600)
        self.show()

    def _configurar(self):
        self.ui.pbuttonAfiliarSocio.clicked.connect(self.abrir_dialogo_afiliar_socio)
        self.ui.pbuttonRegistrarConsumo.clicked.connect(self.abrir_dialogo_registrar_consumo)

        #self.ui.listViewSocios.selectionChanged = self.seleccionar_socio
        self.ui.listViewSocios.setModel(QStandardItemModel())
        self.ui.listView_Facturas.setModel(QStandardItemModel())
        sel_model = self.ui.listViewSocios.selectionModel()
        sel_model.selectionChanged.connect(self.seleccionar_socio)

        #TODO: Quitar este código
        for socio in self.club.socios.values():
            self.actualizar_lista_socios(socio)

    def abrir_dialogo_afiliar_socio(self):
        dialogo = DialogoAfiliarSocio(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            cedula = dialogo.ui.lineEditCedula.text()
            nombre = dialogo.ui.lineEditNombre.text()

            try:
                 socio = self.club.afiliar_socio_a_club(cedula,nombre)
            except SocioExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error al afiliar socio")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                self.actualizar_lista_socios(socio)

    def actualizar_lista_socios(self,socio):
        item = QStandardItem(str(socio))
        item.setEditable(False)
        item.socio = socio
        self.ui.listViewSocios.model().appendRow(item)

    def abrir_dialogo_registrar_consumo(self):
        indexes = self.ui.listViewSocios.selectionModel().selectedIndexes()
        if len(indexes) == 0:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe seleccionar un socio para registrarle un consumo")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            dialogo = DialogoRegistrartConsumo(self)
            resp = dialogo.exec_()
            if resp == QDialog.Accepted:
                item = self.ui.listViewSocios.model().itemFromIndex(indexes[0])
                cedula = item.socio.cedula
                concepto = dialogo.ui.lineEditDetalle.text()
                valor = float(dialogo.ui.lineEdit_Valor.text())
                autorizado = dialogo.ui.lineEdit_Autorizado.text()

                try:
                    self.club.registrar_consumo_a_la_cuenta_del_socio(cedula, concepto, valor, autorizado)
                except SocioNoExistenteError as err:
                    msg_box = QMessageBox(self)
                    msg_box.setWindowTitle("Error registrando consumo")
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setText(err.msg)
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec_()
                else:
                    self.actualizar_lista_de_facturas()

    def seleccionar_socio(self, selected, deselected):
        indexes = selected.indexes()
        if len(indexes) > 0:
            item = self.ui.listViewSocios.model().itemFromIndex(indexes[0])
            print(item.socio)

            self.actualizar_datos_socio(item.socio)
            self.actualizar_lista_de_facturas()
            self.actualizar_lista_autorizados()

    def actualizar_datos_socio(self, socio):
        self.ui.lineEditCedula.setText(socio.cedula)
        self.ui.lineEdit_Nombre.setText(socio.nombre)

    def actualizar_lista_de_facturas(self):
        self.ui.listView_Facturas.model().clear()
        indexes = self.ui.listViewSocios.selectionModel().selectedIndexes()
        if len(indexes) > 0:
            item = self.ui.listViewSocios.model().itemFromIndex(indexes[0])
            for factura in item.socio.facturas:
                item = QStandardItem(str(factura))
                item.setEditable(False)
                item.factura = factura
                self.ui.listView_Facturas.model().appendRow(item)

    def actualizar_lista_autorizados(self):
        self.ui.listWidgetAutorizados.clear()
        indexes = self.ui.listViewSocios.selectionModel().selectedIndexes()
        if len(indexes) > 0:
            item = self.ui.listViewSocios.model().itemFromIndex(indexes[0])
            for autorizado in item.socio.autorizados:
                self.ui.listWidgetAutorizados.addItem(autorizado)

class DialogoAfiliarSocio(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        self.ui = Ui_DialogAfiliarSocio()
        self.ui.setupUi(self)

        validator = QRegExpValidator(QRegExp('\\d{12}'))
        self.ui.lineEditCedula.setValidator(validator)

    def accept(self) -> None:
        if self.ui.lineEditCedula.text() != "" and self.ui.lineEditNombre.text() != "" :
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validacion")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

class DialogoRegistrartConsumo(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        self.ui = Ui_DialogRegistrarconsumo()
        self.ui.setupUi(self)

        validator = QIntValidator(0,100000000)
        self.ui.lineEdit_Valor.setValidator(validator)
    def accept(self) -> None:
        if self.ui.lineEdit_Valor.text() != "" and self.ui.lineEditDetalle.text() != "" :
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validacion")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    club = Club()
    window = VentanaClubSocial(club)
    sys.exit(app.exec_())
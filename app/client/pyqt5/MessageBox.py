from PyQt5.QtWidgets import QMessageBox


class MessageBox():
    def __init__(self, title, message):
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setWindowTitle(title)
        infoBox.setText(message)
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()
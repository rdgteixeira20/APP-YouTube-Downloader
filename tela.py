
from pytube import YouTube
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 132)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_logo = QtWidgets.QLabel(self.centralwidget)
        self.lb_logo.setGeometry(QtCore.QRect(0, 10, 81, 91))
        self.lb_logo.setObjectName("lb_logo")
        self.lb_link = QtWidgets.QLabel(self.centralwidget)
        self.lb_link.setGeometry(QtCore.QRect(100, 20, 58, 16))
        self.lb_link.setObjectName("lb_link")
        self.lb_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lb_titulo.setGeometry(QtCore.QRect(90, 50, 58, 16))
        self.lb_titulo.setObjectName("lb_titulo")
        self.ln_url = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_url.setGeometry(QtCore.QRect(140, 20, 481, 24))
        self.ln_url.setObjectName("ln_url")
        self.ln_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_nome.setGeometry(QtCore.QRect(140, 50, 481, 24))
        self.ln_nome.setObjectName("ln_nome")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(410, 90, 211, 24))
        self.bt_download.setObjectName("bt_download")
        self.rb_mp4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_mp4.setGeometry(QtCore.QRect(90, 90, 100, 22))
        self.rb_mp4.setObjectName("rb_mp4")
        self.rb_mp3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_mp3.setGeometry(QtCore.QRect(210, 90, 100, 22))
        self.rb_mp3.setObjectName("rb_mp3")
        self.lb_versao = QtWidgets.QLabel(self.centralwidget)
        self.lb_versao.setGeometry(QtCore.QRect(10, 110, 58, 16))
        self.lb_versao.setObjectName("lb_versao")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ######Botão#####
        self.bt_download.clicked.connect(self.download)
        ######Função de Download######
    def download(self):
        if self.rb_mp4.isChecked() == True:
            url = self.ln_url.text()
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            video.download()
            print(yt.title + " has been successfully downloaded.")
        elif self.rb_mp3.isChecked() == True:
            try:
                url = self.ln_url.text()
                yt = YouTube(url)
                audio = yt.streams.filter(only_audio=True).first()
                out_file = audio.download()
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                print(yt.title + " has been successfully downloaded.")
            except:
                pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ytlogo/ytlogo.png\"/></p></body></html>"))
        self.lb_link.setText(_translate("MainWindow", "Link : "))
        self.lb_titulo.setText(_translate("MainWindow", "Título :"))
        self.bt_download.setText(_translate("MainWindow", "DOWNLOAD"))
        self.rb_mp4.setText(_translate("MainWindow", "Video MP4"))
        self.rb_mp3.setText(_translate("MainWindow", "Audio MP3"))
        self.lb_versao.setText(_translate("MainWindow", "V1.0"))
# Logo do APP#
import ytlogo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

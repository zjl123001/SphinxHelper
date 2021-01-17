import sys, os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QDialog
from PyQt5.QtCore import QCoreApplication
import sphinx
import sphinx.builders.html.transforms

class Ui_mainWindow(object): # 主窗口

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("Sphinx Tool")
        mainWindow.resize(320, 308)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.pushButton_3.clicked.connect(self.popWindow)
        self.pushButton_2.clicked.connect(self.popWindow1)
        self.pushButton.clicked.connect(QCoreApplication.instance().quit)


    def popWindow(self): # 弹出新建项目窗口
        if self.pushButton_2.isEnabled():
            self.form2 = QWidget()
            self.ui2 = Ui_Form1()
            self.ui2.setupUi(self.form2)
            self.form2.show()


    def popWindow1(self): # 弹出管理项目窗口
        if self.pushButton_3.isEnabled():
            self.form2 = QWidget()
            self.ui2 = Ui_Form()
            self.ui2.setupUi(self.form2)
            self.form2.show()


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Sphinx 小助手"))
        self.pushButton_2.setText(_translate("mainWindow", "新建项目"))
        self.pushButton_3.setText(_translate("mainWindow", "管理项目"))
        self.pushButton.setText(_translate("mainWindow", "退出"))

class Ui_Form(object): # 新建项目窗口

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(435, 274)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignRight)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 5, 1, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.toolButton.clicked.connect(self.setpath)
        self.pushButton.clicked.connect(self.generate_pro)
        self.pushButton_2.clicked.connect(Form.close)

    def setpath(self):
        if self.toolButton.isEnabled():
            directory = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "./")
            self.lineEdit.setText(directory)


    def generate_pro(self):
        if self.pushButton.isEnabled():
            path = self.lineEdit.text()
            name = self.lineEdit_2.text()
            author = self.lineEdit_3.text()
            version = self.lineEdit_4.text()
            language = self.comboBox.currentText()
            if not path or not name or not author or not language:
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '请填写基本信息')
                msg_box.exec_()
            else:
                info = {'path': path , 'dot': '_', 'version': '', 'suffix': '.rst', 'master': 'index', 'epub': False,
                        'makefile': True, 'batchfile': True, 'make_mode': True, 'extensions': [], 'sep': True,
                        'project': name , 'author': author , 'release': version, 'language': language}
                from sphinx.cmd import quickstart
                try:
                    quickstart.generate(info)
                    msg_box = QMessageBox(QMessageBox.Warning, '提示', '创建成功')
                    msg_box.exec_()
                    record = path + ' ;'
                    with open("sphinx_program.txt", "a") as f:
                        f.write(record)
                except:
                    msg_box = QMessageBox(QMessageBox.Warning, '提示', '创建成功')
                    msg_box.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "新建项目"))
        self.label_4.setText(_translate("Form", "版本"))
        self.label_3.setText(_translate("Form", "作者"))
        self.label_2.setText(_translate("Form", "项目名称"))
        self.label_5.setText(_translate("Form", "语言"))
        self.comboBox.setItemText(0, _translate("Form", "en"))
        self.comboBox.setItemText(1, _translate("Form", "zh_CN"))
        self.label.setText(_translate("Form", "项目目录"))
        self.toolButton.setText(_translate("Form", "..."))
        self.pushButton.setText(_translate("Form", "创建项目"))
        self.pushButton_2.setText(_translate("Form", "返回"))


class Ui_Form1(object): # 管理项目窗口

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(502, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(self.setpath)
        self.pushButton_4.clicked.connect(self.generate)
        self.pushButton_3.clicked.connect(self.extensions)
        self.pushButton_5.clicked.connect(Form.close)

    def setpath(self):
        if self.pushButton_2.isEnabled():
            directory = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "./")
            self.lineEdit.setText(directory)

    def generate(self):
        if self.pushButton_4.isEnabled():
            if self.comboBox_2.currentText().strip() == "HTML":
                filetype = 'html'
            elif self.comboBox_2.currentText().strip() == "latex":
                filetype = 'latex'
            else:
                filetype = 'pdf'
            path = self.lineEdit.text().strip()
            if path:
                if filetype == 'pdf':
                    try:
                        with open(path + '/source/conf.py', 'r+', encoding='utf-8') as f:
                            for line in f.readlines():
                                if 'extensions = [' in line:
                                    if 'rst2pdf.pdfbuilder' not in line:
                                        msg_box = QMessageBox(QMessageBox.Warning, '提示', '检测未安装pdf生成插件！')
                                        msg_box.exec_()
                                        return
                    except:
                        msg_box = QMessageBox(QMessageBox.Warning, '提示', '无法生成，请检查conf文件！')
                        msg_box.exec_()
                print(filetype)
                argv = ['-M', filetype, path.strip()+'/source', path.strip()+'/build']
                import sphinx.cmd.build
                if os.path.exists(path + '/source/conf.py'):
                    try:
                        sphinx.cmd.build.main(argv)
                        msg_box = QMessageBox(QMessageBox.Warning, '提示', '生成成功')
                        msg_box.exec_()
                        f = open("sphinx_program.txt", "r")
                        records = f.readline()
                        if path not in records: # 如果路径不在记录里，自动储存路径
                            f.close()
                            records = records + path +';'
                            f = open("sphinx_program.txt", "w")
                            f.write(records)
                        f.close()
                    except:
                        msg_box = QMessageBox(QMessageBox.Warning, '提示', '生成失败')
                        msg_box.exec_()
                else:
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '目录下没有找到conf.py文件')
                    msg_box.exec_()

    def extensions(self):
        if self.pushButton_3.isEnabled():
            path = self.lineEdit.text().strip()
            extension = self.comboBox.currentText().strip()
            if path:
                if os.path.exists(path + '/source/conf.py'):
                    lines = []
                    if extension == "rst2pdf（不支持中文":
                        try:
                            with open(path + '/source/conf.py','r+',encoding='utf-8') as f:
                                for line in f.readlines():
                                    if 'extensions = [' in line:
                                        if 'rst2pdf.pdfbuilder' in line:
                                            msg_box = QMessageBox(QMessageBox.Warning, '提示', '检测到已经安装！')
                                            msg_box.exec_()
                                            return
                                        thisline = list(line.split('['))
                                        thisline.insert(1,'''['sphinx.ext.autodoc','rst2pdf.pdfbuilder',''')
                                        newline = ''.join(thisline)
                                        lines.append(newline)
                                        continue
                                    lines.append(line)
                            with open(path + '/source/conf.py', 'w',encoding='utf-8') as f:
                                f.writelines(lines)
                            msg_box = QMessageBox(QMessageBox.Warning, '提示', '安装成功')
                            msg_box.exec_()
                            f = open("sphinx_program.txt", "r")
                            records = f.readline()
                            if path not in records:  # 如果路径不在记录里，自动储存路径
                                f.close()
                                records = records + path + ';'
                                f = open("sphinx_program.txt", "w")
                                f.write(records)
                            f.close()
                        except:
                                msg_box = QMessageBox(QMessageBox.Warning, '提示', '安装失败')
                                msg_box.exec_()
                    if extension == 'githubpages':
                        try:
                            with open(path + '/source/conf.py', 'r',encoding='utf-8') as f:
                                for line in f.readlines():
                                    if 'extensions = [' in line:
                                        if 'rst2pdf.githubpages' in line:
                                            msg_box = QMessageBox(QMessageBox.Warning, '提示', '检测到已经安装！')
                                            msg_box.exec_()
                                            return
                                        thisline = list(line.split('['))
                                        thisline.insert(1, '''['sphinx.ext.githubpages',''')
                                        newline = ''.join(thisline)
                                        lines.append(newline)
                                        continue
                                    lines.append(line)
                            with open(path + '/source/conf.py', 'w',encoding='utf-8') as f:
                                f.writelines(lines)
                            msg_box = QMessageBox(QMessageBox.Warning, '提示', '安装成功')
                            msg_box.exec_()
                        except:
                            msg_box = QMessageBox(QMessageBox.Warning, '提示', '安装失败')
                            msg_box.exec_()
                else:
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '目录下没有找到conf.py文件')
                    msg_box.exec_()

    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理项目"))
        self.pushButton.setText(_translate("Form", "选择已有项目"))
        self.pushButton_2.setText(_translate("Form", "其他目录"))
        self.label_2.setText(_translate("Form", "安装插件"))
        self.comboBox.setItemText(0, _translate("Form", "rst2pdf（不支持中文"))
        self.comboBox.addItem("githubpages")
        self.pushButton_3.setText(_translate("Form", "安装"))
        self.label_3.setText(_translate("Form", "生成文件"))
        self.comboBox_2.setItemText(0, _translate("Form", "HTML"))
        self.comboBox_2.setItemText(1, _translate("Form", "latex"))
        self.comboBox_2.setItemText(2, _translate("Form", "PDF"))
        self.pushButton_4.setText(_translate("Form", "生成"))
        self.pushButton_5.setText(_translate("Form", "返回"))

        self.pushButton.clicked.connect(self.popdialog)
        self.dialog = QDialog()
        self.dia = Ui_Dialog()
        self.dia.setupUi(self.dialog)
        self.dialog.accepted.connect(self.update)

    def popdialog(self):
        if self.pushButton.isEnabled():
            self.dialog.show()

    def update(self):
        self.lineEdit.setText(self.dia.comboBox.currentText())

class Ui_Dialog(object): # 选择以前的项目窗口

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(272, 91)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 256, 72))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        if os.path.exists("sphinx_program.txt"):
            with open("sphinx_program.txt", 'r') as f:
                records = list(f.readline().strip().split(';'))
                if records:
                    for n, record in enumerate(records):
                        if record != '':
                            self.comboBox.addItem(record)

def main(): # 主函数
    app = QApplication(sys.argv)
    w = QMainWindow()
    window = Ui_mainWindow()
    window.setupUi(w)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__': # 主函数
    app = QApplication(sys.argv)
    w = QMainWindow()
    window = Ui_mainWindow()
    window.setupUi(w)
    w.show()
    sys.exit(app.exec_())
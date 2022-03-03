import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

objects = ["Menu", "LineEdit", "Box", "MenuBar"]


class TextEditor(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.resize(500, 500)
		self.setObjectName(objects[0])
		self.txt_editor = QPlainTextEdit(self)
		self.txt_layout = QVBoxLayout(self)
		self.txt_widget = QWidget(self)
		self.menu = QMenuBar(self)
		self.setMenuBar(self.menu)
		self.MenuBar()
		self.Actions()
		self.TxtField()
		self.Rightclick()

	def MenuBar(self):
		self.file = QMenu("&File", self)
		self.edit = QMenu("&Edit", self)
		self.style = QMenu("&Style", self)
		self.menu.addMenu(self.file)
		self.menu.addMenu(self.edit)
		self.menu.addMenu(self.style)
		self.menu.setObjectName(objects[3])

		#  File button setting
		self.new_file = QAction("&New", self)
		self.open_file = QAction("&Open", self)
		self.save_file = QAction("&Save", self)
		self.quit = QAction("&Quit", self)
		self.file.addAction(self.new_file)
		self.file.addAction(self.open_file)
		self.file.addAction(self.save_file)
		self.file.addSeparator()
		self.file.addAction(self.quit)

		#  Edit button setting
		self.edit.addAction(QAction("&Copy", self))
		self.edit.addAction(QAction("&Paste", self))
		self.edit.addAction(QAction("&Cut", self))

		#  Style button setting
		self.style.addAction(QAction("&BatStyle", self))
		self.style.addAction(QAction("&Photony", self))

	def Actions(Self):
		self.new_file.triggered.connect(self.newFile)
		self.open_file.triggered.connect(self.openFile)
		self.save_file.triggered.connect(self.saveFile)
		self.quit.triggered.connect(self.quitEditor)

	def newFile(self):
		pass

	def openFile(self):
		pass

	def saveFile(self):
		pass

	def quitEditor(self):
		pass


	def TxtField(self):
		self.txt_editor.setObjectName(objects[1])
		self.txt_layout.setObjectName(objects[2])
		self.txt_layout.addWidget(self.txt_editor)
		self.txt_widget.setLayout(self.txt_layout)
		self.setCentralWidget(self.txt_widget)

	def Rightclick(self):
		self.txt_editor.setContextMenuPolicy(Qt.ActionsContextMenu)
		self.txt_editor.addAction(QAction("&Copy", self))
		self.txt_editor.addAction(QAction("&Paste", self))
		self.txt_editor.addAction(QAction("&Cut", self))


def display():
	import sys
	w = QApplication(sys.argv)
	w.setApplicationName("Chiropter")
	BatStyle = open("BatStyle.qss", "r")
	with BatStyle:
		qss = BatStyle.read()
		w.setStyleSheet(qss)
	w.setStyle("Breeze")
	ui = TextEditor()
	ui.show()
	w.exec()


display()

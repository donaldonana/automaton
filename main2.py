from PyQt5.QtWidgets import QMainWindow, QApplication
from automaton import *
from thompson import*
import sys




class Main(QMainWindow):
	"""docstring for Main"""
	def __init__(self, *args, **kwargs):
		super(Main, self).__init__(*args, **kwargs)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.generer.clicked.connect(self.apply)


	def apply(self):
		if len(self.ui.regex.text()) != 0 :
			etat = ""
			chaine = self.ui.regex.text()

			analyseur = AnalyseurSyntaxique()

			lexemes = analyseur.analyse(chaine)
			lexemes = analyse_infixe(lexemes)

			C = eval_suffixe(lexemes)
			alphabet = C.alphabet
			
			for x in C.state:
				if x == C.init:
					x = x + " initial state"
				if x in C.final:
					x = x + " final state"
				self.ui.listWidget.addItem(str(x))
			self.ui.alphabet.setText(alphabet)			




	@staticmethod
	def main():
		app =  QApplication(sys.argv)

		m = Main()
		m.show()

		sys.exit(app.exec_())



if __name__ == '__main__':
	Main.main()
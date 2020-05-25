import os

from arbre import*
from automate import*

# -*- coding: utf-8 -*-
import os
import re
import math


n = 0

class Lexeme(object):
	"""docstring for Lexeme"""
	def __init__(self, type, valeur):
		self.type = type
		self.valeur = valeur


class Alphabet(Lexeme):
	"""docstring for Nombre"""
	def __init__(self, valeur):
		Lexeme.__init__(self,"n",valeur)
	def suffixe(self, pile):
		global n
		# print(n)
		pile.append(base(self.valeur,n))
		n = n + 1


class Operateur(Lexeme):
	"""docstring for Operateur"""
	def __init__(self, valeur):
		Lexeme.__init__(self,"op",valeur)
		if valeur == "+":
			self.suffixe = self.unions
			self.priorite = 1
			self.associativite = "g"


		if valeur == ".":
			self.suffixe = self.concats
			self.priorite = 2
			self.associativite = "g"


		if valeur == "*":
			self.suffixe = self.etoiles
			self.priorite = 3
			self.associativite = "d"


	def unions(self,pile):
		b = pile.pop()
		a = pile.pop()
		global n
		pile.append(union(a,b,n))
		n = n + 1
	def concats(self,pile):
		b = pile.pop()
		a = pile.pop()
		pile.append(concat(a,b))
	def etoiles(self,pile):
		a = pile.pop()
		global n
		pile.append(etoile(a,n))
		n = n + 1
		

class Parenthese(Lexeme):
	def __init__(self,valeur):
		Lexeme.__init__(self,"par",valeur)
		self.priorite = 0




class AnalyseurSyntaxique:
	def __init__(self):
		self.fonctions_lecture = {"[+*\.]":self.lecture_operateur,\
								  "[a-z]+":self.lecture_alphabet,\
								  "[\(\)]":self.lecture_parenthese,\
								  "[\s]+":self.lecture_espace}
		self.lexemes = []
		self.chaine = ""

	def analyse(self,chaine):
		self.lexemes = []
		longueur = len(chaine)
		while longueur > 0:
			for exp in self.fonctions_lecture.keys():
				m = re.match(exp,chaine)
				if m:
					valeur = chaine[0:m.end()]
					chaine = chaine[m.end():longueur]
					longueur -= m.end()-m.start()
					self.fonctions_lecture[exp](valeur)
					break	
		return self.lexemes
	def lecture_operateur(self,valeur):
		self.lexemes.append(Operateur(valeur))
	def lecture_parenthese(self,valeur):
		self.lexemes.append(Parenthese(valeur))
	def lecture_alphabet(self,valeur):
		self.lexemes.append(Alphabet(valeur))
	def lecture_espace(self,valeur):
		pass


		
def eval_suffixe(lexemes):
	pile_nombres = []
	for lex in lexemes:
		lex.suffixe(pile_nombres)
	if len(pile_nombres)!=1:
		raise SystemExit("Erreur dans l'expression")
	else:
		global n
		n = 0
		return pile_nombres[0]






def analyse_infixe(lexemes):
	lexemes_sortie = []
	pile_operateurs = []
	for lex in lexemes:
		if lex.type=="n":
			lexemes_sortie.append(lex)
		elif lex.type=="op":
			if len(pile_operateurs)==0:
				pile_operateurs.append(lex)
			else:
				if lex.associativite=="g":
					while pile_operateurs[-1].priorite >= lex.priorite:
						lexemes_sortie.append(pile_operateurs.pop())
						if len(pile_operateurs)==0:
							break
				else:
					while pile_operateurs[-1].priorite > lex.priorite:
						lexemes_sortie.append(pile_operateurs.pop())
						if len(pile_operateurs)==0:
							break
				pile_operateurs.append(lex)
		elif lex.type=="par":
			if lex.valeur=="(":
				pile_operateurs.append(lex)
			elif lex.valeur==")":
				while pile_operateurs[-1].valeur!="(":
					lexemes_sortie.append(pile_operateurs.pop())
				pile_operateurs.pop()

	while len(pile_operateurs)!=0:
		lexemes_sortie.append(pile_operateurs.pop())

	return lexemes_sortie



def union(A, B, n):
	C = DFA(A.alphabet+B.alphabet+"€")
	C.state = A.state + B.state
	C.add_state("qi" + "'"*n)
	C.add_state("qf" + "'"*n)
	C.init = "qi" + "'"*n
	C.final.append("qf" + "'"*n)
	for i in C.state:
		if i in A.state:
			C.transition[i] = A.transition[i]
		if i in B.state:
			C.transition[i] = B.transition[i]
	C.add_transition("qi"+ "'"*n, "€", A.init)
	C.add_transition("qi"+ "'"*n, "€", B.init)
	C.transition[B.final[0]] = [("€","qf"+ "'"*n)]
	C.transition[A.final[0]] = [("€","qf"+ "'"*n)]


	return C


def concat(A, B):
	C = DFA(A.alphabet+B.alphabet+"€")
	print(B.transition)
	C.state = A.state + B.state
	C.init = A.init
	C.final = B.final
	for i in C.state:
		if i in A.state:
			C.transition[i] = A.transition[i]
		if i in B.state:
			C.transition[i] = B.transition[i]
	C.transition[A.final[0]] = [("€", B.init)]
	return C



def etoile(A, n):
	C = DFA(A.alphabet+"€")
	C.state = A.state + []
	C.add_state("qi"+ "'"*n)
	C.add_state("qf"+ "'"*n)
	C.init = "qi"+ "'"*n
	C.final.append("qf"+ "'"*n)
	for i in C.state:
		if i in A.state:
			C.transition[i] = A.transition[i]
	C.transition[A.final[0]] = [("€", A.init)]
	C.transit[A.final[0]] = []
	C.add_transition("qi"+ "'"*n, "€", A.init)
	C.add_transition(A.final[0], "€", "qf"+ "'"*n) 
	C.add_transition("qi"+ "'"*n, "€", "qf"+ "'"*n)

	return C


def base(char, n):
	a = DFA(char)
	a.add_state("0"+ "'"*n)
	a.add_state("1"+ "'"*n, True)
	a.add_transition("0"+ "'"*n, char, "1"+ "'"*n)
	a.init = "0"+ "'"*n
	return a



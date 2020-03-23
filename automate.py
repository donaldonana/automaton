# -*- coding: utf-8 -*-
import os

class DFA():
	"""docstring for DFA"""
	def __init__(self, alphabet):

		self.state = []

		self.init = None

		self.transition = {}

		self.final = []

		self.alphabet = ""

		self.transit = {}

		for s in alphabet:
			if s not in self.alphabet:
				self.alphabet += s


	def add_state(self, state, final=False):
		if state in self.state:
			print("Erreur l'etat" + state + "existe deja")
			return
		self.transition[state] = []
		self.transit[state] = []
		self.state.append(state)
		if final:
			self.final.append(state)


	def valid_symbol(self, symbol):
		if symbol not in self.alphabet:
			return False
		return True

	def dst_state(self, src_state, symbol):
		if src_state not in self.state:
			print("Erreur0")
			return
		for(s, dst_state) in self.transition[src_state]:
			if symbol == s:
				return None
		return None

	def transitions(self, src_state, symbol):
		if src_state not in self.state:
			pass
			return
		for(s, dst_state) in self.transition[src_state]:
			if symbol == s:
				return dst_state
		return None

	def add_transition(self,  src_state, symbol, dst_state ):
		if not self.valid_symbol(symbol):
			print("Erreur2")
			return
		if src_state not in self.state:
			print("Erreur3")
			return
		if dst_state not in self.state:
			print("Erreur4")
			return
		if self.dst_state(src_state, symbol) != None:
			print("Erreur5")
			return
		self.transition[src_state].append((symbol, dst_state))
		self.transit[src_state].append(symbol)

	def calcul(self, mot):
		Q = self.init
		print(type(Q))
		for x in mot:
			q = self.transitions(str(Q), x)
			Q = q
		if Q in self.final:
			return "CALCUL REUSSI"
		else:
			return "CALCUL NON REUSSI"



	def completage(self):
		qp = "qp"
		symbol = []
		element = []
		add = 1
		for state in self.state:
			for s in self.transit[state]:
				symbol.append(s)
			for x in self.alphabet:
				if x not in symbol:
					element.append(x)
					if add == 1:
						self.add_state(qp)
						add = 0
					self.add_transition(state, x, qp)
			symbol = []
		for x in self.alphabet:
			if (x not in element) and add == 0:
				self.add_transition(qp, x, qp)

		
		

	def __str__(self):
		ret = "\n"
		ret += "			AUTOMATE :\n"
		ret += "   - alphabet   : '" + self.alphabet + "'\n"
		ret += "   - etat initial       : " + str(self.init) + "\n"
		ret += "   - etat final     : " + str(self.final) + "\n"
		ret += "   - total etats (%d) :\n" % (len(self.state))
		ret += "\n"
		for state in self.state:
			ret += "		- (%s)" %(state)
			if len(self.transition[state]) == 0:
				ret += "AUCUNE TRANSITION SUR CET ETAT.\n"
			else:
				ret += ":\n"
				for(sym, dest) in self.transition[state]:
					ret +=  "			--(%s)----> (%s)\n" % (sym, dest)
		return ret	


	def exitTransition(self, state):
		entrante = {}
		for s in self.state:
			for (sym, dest) in self.transition[s]:
				if(dest == state):
					entrante[s] = [(sym,dest)]

		return (entrante)



def closure(A, T):
	epsilone_closure = set()
	for x in T:
		epsilone_closure.add(x)
	while T:
		for a in T:
			for (sym, dst) in A.transition[a]:
				if sym == "€" and dst not in epsilone_closure:
					epsilone_closure.add(dst)
					T.insert(0,dst)
			T.remove(a)

	return epsilone_closure



def transitions(A, src_state, symbol):
	V = []
	if src_state not in A.state:
		print("Erreur1")
		return
	for(s, dst_state) in A.transition[src_state]:
		if symbol == s:
			V.append(dst_state) 
	return V



def transiter(a, z, T):
	t = []
	for x in T:
		r = transitions(a, x, z)
		t = t + r
	return t



def non_epsilone(a):
	newalphabet = ""
	for x in a.alphabet:
		if x != "€":
			newalphabet = newalphabet + x
	A = DFA(newalphabet)
	A.init = closure(a,[a.init])
	A.add_state(str(closure(a,[a.init])))
	D = []
	D.append(closure(a,[a.init]))
	marque = []
	marque.append(closure(a,[a.init]))
	while([e for e in D if e in marque]):
		for p in D:
			if p in marque:
				for y in A.alphabet:
					U = closure(a, transiter(a, y, p))
					if U :
						if U not in D:
							f = False
							D.append(U)
							marque.append(U)
							for z in U:
								if z in a.final:
									f = True
									break
							A.add_state(str(U), f)
						A.transition[str(p)].append((y, str(U)))					
					
				marque.remove(p)

	if a.init in a.final:
		A.final.append(str(closure(a,[a.init])))

	return A




def complementation(A):
	A = non_epsilone(A)
	A.completage()
	newfinal = []
	for x in A.state:
		if x not in A.final:
			newfinal.append(x)
	A.final = newfinal
	return A

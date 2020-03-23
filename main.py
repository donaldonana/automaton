# -*- coding: utf-8 -*-
import os
from automate import*
from thompson import*




# a = DFA("ba")
# a.add_state("1")
# a.add_state("2")
# a.add_state("3")
# a.add_state("4", True)
# a.init = "1"
# a.add_transition("1", "a", "3")

# a.add_transition("1", "a", "2")

# a.add_transition("3", "a", "3")
# a.add_transition("3", "b", "4")
# a.add_transition("4", "b", "2")
# a.add_transition("2", "a", "4")

# mot = input("SAISIR LE MOT : ")
# a = non_epsilone(a)
# resultat = a.calcul(mot)
# print(resultat)

boucle = 1

while boucle:


	print("\n")

	print("				1)-ENTRER UN AUTOMATE")
	print("				2)-ENTRER UNE EXPRESSION REGULIERE ( la concatenation sera l'operateur <<.>> )")

	print("\n")

	choix2 = input("CHOISIR L'OPERATION SELON LE CHIFFRE CORRESPONDANT : ")

	print("\n")

	if choix2 == "2":
		ex = 1
		while ex:
			print("\n")
			chaine = input("ENTRER L'EXPRESSION REGULIERE : ")

			analyseur = AnalyseurSyntaxique()

			lexemes = analyseur.analyse(chaine)
			lexemes = analyse_infixe(lexemes)
			valeurs = []
			for lex in lexemes:
				valeurs.append(lex.valeur)
				
			print(valeurs)

			C = eval_suffixe(lexemes)
			print(C)


			c = non_epsilone(C)
			print(c.calcul("bcaaaaaaaa"))
				
			print("\n")
			boucle1 = input("VOULEZ-VOUS ENTER UNE AUTRE EXPRESSION REGULIERE ?  tapez 'n' pour non ou 'o' pour oui : ")

			if boucle1 == "n":
				ex = 0
		


	if choix2 == "1":


		alphabet = input("ENTRER L'ALPHABET( exemple: abc où a, b, et c fairons parti de l'alphabet ) : ")
		a = DFA(alphabet)
		print("\n")

		pr = 0
		p = True

		while p:
			if pr == 0:
				etat = input("ENTRER LES ETATS DE L'AUTOMATES ( UNE FOIS QUE VOUS N'AUREZ PLUS D'ETATS A ENREGISTRES TAPEZ JUSTE SUR <<ENTRER>> ) : ")
				pr = 1
			else:
				etat = input("ENTRER UN AUTRE ETAT( UNE FOIS QUE VOUS N'AUREZ PLUS D'ETATS A ENREGISTRES TAPEZ JUSTE SUR <<ENTRER>> ) : ")
			
			if etat:
				final = input("Est il un etat final ? tapez 'n' pour non ou 'o' pour oui : ")
				if final == "o":
					final = True
				else:
					final = False
				a.add_state(etat, final)
			else:
				p = False

		init = input("QUEL EST L'ETAT INITIAL : ")
		while init not in a.state:
			init = input("ENTRER UN ETAT VALIDE : ")


		a.init = init
		print(type(init))


		print("\n")


		i = 1
		p2 = True
		while p2:
			print("SAISIE DE LA TRANSITION N¨",i)
			src = input("		ENTRER L'ETAT SOURCE : ")
			sym = input("		ENTRER LE SYMNOLE : ")
			dst = input("		ENTRER L'ETAT CIBLE : ")
			if src and sym and dst:
				a.add_transition(src, sym, dst)
				i = i + 1
			else:
				p2 = False



		print("						*******PRESENTATION DE L'AUTOMATE**********")
		print(a)

		print("\n")
		p1 = 1

		while p1:
			

			print("			1)- Reconnaissance d'un mot ")
			print("			2)- complementaire de l'automate ")
			print("			3)- completer l'automate")
			print("			4)- Determiniser l'automate ")
			print("			5)- Elimination des €-transition")
			print("\n")


			choix = input(				"CHOISIR L'OPERATION SELON LE CHIFFRE CORRESPONDANT : ")



			if choix == "1":
				p3 = 1
				while p3:
					mot = input("SAISIR LE MOT : ")
					A = non_epsilone(a)
					resultat = A.calcul(mot)
					print(resultat)
					print("\n")
					retry = input("VOULEZ VOUS SAISIR UN AUTRE MOT ? tapez 'n' pour non ou 'o' pour oui : ")
					if retry != "o":
						p3 = 0

			if choix == "2":
				b = complementation(a)
				print("\n")
				print("						*******PRESENTATION DE L'AUTOMATE COMPLEMENTAIRE**********")
				print(b)
				mot = input("Entrer le mot a calculer : ")
				resultat = b.calcul(mot)
				print(resultat)

			if choix == "3":
				a.completage()
				print("\n")
				print("						*******PRESENTATION DE L'AUTOMATE COMPLET**********")
				print(a)

			if choix == "4":
				print("\n")
				d = non_epsilone(a)
				print("						*******PRESENTATION DE L'AUTOMATE DETERMINISE**********")
				print(d)

			if choix == "5":
				print("\n")
				d = non_epsilone(a)
				print("					**********PRESENTATION DE L'AUTOMATE  DETERMINISE SANS  €-transition **********")
				print(d)

			print("\n")	
			p4 = input("VOULEZ-VOUS REPRENDRE UNE OPERATION ? : tapez 'n' pour non ou 'o' pour oui : ")

			if p4 == "n":
				p1 = 0

	print("\n")
	boucle1 = input("VOULEZ-VOUS REPRENDRE AU MENU PRINCIPAL ?  tapez 'n' pour non ou 'o' pour oui : ")

	if boucle1 == "n":
		boucle = 0
		











os.system("pause")
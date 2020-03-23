class arbre:
	"""docstring for arbre"""
	def __init__(self, arg):
		self.left = None
		self.right = None
		self.arg = arg

	def insert(self, val):
		if self.arg:
			if self.arg > val:
				if self.left is None:
					self.left = arbre(val)
				else:
					self.left.insert(val)
			elif self.arg < val:
				if self.right is None:
					self.right = arbre(val)
				else:
					self.right.insert(val)
		else:
			self.arg = val


	def printInfix(self):
		if self.left:
			self.left.printInfix()
		print(self.arg)
		if self.right:
			self.right.printInfix()

	def printPrefix(self):
		print(self.arg)
		if self.left:
			self.left.printPrefix()
		if self.right:
			self.right.printPrefix()

	def printPostfix(self):
		if self.left:
			self.left.printPostfix()
		if self.right:
			self.right.printPostfix()
		print(self.arg)

	def vide(self):
		if self.arg == None:
			return True
		else:
			return False


	def recherche(self, v):
		if v < self.arg:
			if self.left is None:
				return "Element Absent"
			return self.left.recherche(v)
		elif v > self.arg:
			if self.right is None:
				return "Element Absent"
			return self.right.recherche(v)
		else:
			return "Element Present"


def inverser(chaine):
	nchaine = []
	l = len(chaine) - 1
	i = 0
	while l >= 0:
		nchaine.insert(i, chaine[l])
		l = l-1
		i = i + 1
	return nchaine


def supp(chaine):
	nchaine = ""
	l = 0
	while l < len(chaine):
		if chaine[l] != "(" and chaine[l] != ")":
			nchaine = nchaine + chaine[l]
		l = l + 1
	return nchaine

def isOperator(c): 
    if (c == '+' or c == '.' or c == '/' or c == '^'): 
        return True
    else: 
        return False

def tranformation(ch): 
    stack = [] 
  
    for char in ch : 

        if not isOperator(char) and char != "(" and char !=  "*": 

            A = arbre(char) 
            stack.append(A) 
   
        elif char != "(" and char !=  "*": 
  
            A = arbre(char) 
            A1 = stack.pop() 
            A2 = stack.pop() 
                
            A.right = A1 
            A.left = A2
              
            stack.append(A) 

        elif char == "*":
            A = arbre(char) 
            A1 = stack.pop()
            A.left = A1
              
            stack.append(A) 
  
    A = stack.pop() 
     
    return A 
  


def minValueNode( nod): 
    current = nod
    # loop down to find the leftmost leaf 
    while(current.left is not None): 

        current = current.left  
  
    return current  


def Successeur(node):
	curent = node
	if curent.right is not None:
		curent = curent.right
		while curent.left is not None:
			curent = curent.left
		return curent
	else:
		return node

		


def suppression(root, key): 
  
    # Base Case 
    key = int(key)
    if root.vide(): 
        return root  
  
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    if key < root.arg and root.left:  
        root.left = suppression(root.left, key) 
  
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    elif key > root.arg and root.right:  
        root.right = suppression(root.right, key) 
  
    # If key is same as root's key, then this is the node 
    # to be deleted 
    elif key == root.arg: 
          
        # Node with only one child or no child 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
        temp = Successeur(root.right) 
  
        # Copy the inorder successor's content to this node 
        root.arg = temp.arg
  
        # Delete the inorder successor 
        root.right = suppression(root.right , temp.arg) 
  
  
    return root  
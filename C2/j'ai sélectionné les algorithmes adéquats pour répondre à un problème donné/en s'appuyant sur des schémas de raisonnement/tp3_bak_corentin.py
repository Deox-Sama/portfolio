class Node:
    #fonction qui initialise un arbre binaire de recherche avec uniquement la racine
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        
    
    def __str__(self) -> str:
        return str(self.data)
    
    #fonction permettant d'ajouter un noeud à un arbre binaire de recherche
    def inserNoeud(self, data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
                self.left.parent = self
            else:
                self.left.inserNoeud(data)
        elif data > self.data:
            if self.right == None:
                self.right = Node(data)
                self.right.parent = self
            else:
                self.right.inserNoeud(data)
    
    #fonction qui affiche le parcours en infix de l'arbre binaire de recherche
    def infix(self):
        if self.left != None:
            self.left.infix()


        print(self)
         
        if self.right != None:
            self.right.infix()
            
    #fonction qui recherche si une valeur donnée est déjà présente dans l'arbre       
    def search(self, data):
        if data < self.data:
            return self.left.search(data) if self.left else print("value not exist")
        elif data > self.data:
            return self.right.search(data) if self.right else print("value not exist")
        return "La valeur existe"
    
    


    
    


if __name__ == '__main__':
    

    condition=""

    print("Bienvenue, veuillez entrer un numéro pour choisir l'une des actions suivantes \n 1. Créer un arbre \n 2. Ajouter un noeud \n 3. Afficher l'arbre en Infixe \n 4. Recherche si la valeur fournis existe \n 5. Arrêt du programme")
    option = int(input("Entrez votre option : "))
    
    while option >=1 and option <5:
        if option == 1:
            n = int(input("Donnez la valeur de la racine de l'arbre : "))
            arbre = Node(n)
            print("1. Créer un arbre \n 2. Ajouter un noeud \n 3. Afficher l'arbre en Infixe \n 4. Recherche si la valeur fournis existe \n 5. Arrêt du programme")
            option = int(input("Entrez votre option : "))
        elif option == 2:
            while condition!= "non":
                m = int(input("Donnez la valeur d'un noeud : "))
                arbre.inserNoeud(m)
                condition = input("Voulez vous encore ajouter un noeud : ")
            print("1. Créer un arbre \n 2. Ajouter un noeud \n 3. Afficher l'arbre en Infixe \n 4. Recherche si la valeur fournis existe \n 5. Arrêt du programme")
            option = int(input("Entrez votre option : "))
        elif option == 3:
            print("Voici le parcours de l'arbre en Infixe : ")
            arbre.infix()
            print("1. Créer un arbre \n 2. Ajouter un noeud \n 3. Afficher l'arbre en Infixe \n 4. Recherche si la valeur fournis existe \n 5. Arrêt du programme")
            option = int(input("Entrez votre option : "))
        elif option == 4:
            value = int(input("Donnez la valeur à rechercher dans l'arbre : "))
            print(arbre.search(value))
            print("1. Créer un arbre \n 2. Ajouter un noeud \n 3. Afficher l'arbre en Infixe \n 4. Recherche si la valeur fournis existe \n 5. Arrêt du programme")
            option = int(input("\nEntrez votre option : "))

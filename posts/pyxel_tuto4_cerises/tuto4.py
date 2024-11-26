import pyxel

LARGEUR = 256
HAUTEUR = 128

class Cerise:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vitesse = 1  # Vitesse de chute de la cerise

    def update(self):
        self.y += self.vitesse # La cerise tombe

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 0, 16, 16, 12) #Affichage de la cerise

class Nuage:
    def __init__(self, x = LARGEUR, y = HAUTEUR//4):
        self.x = x
        self.y = y
        self.replaced = False

    def update(self):
        if pyxel.frame_count % 10 == 0:
            self.x = self.x -1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 24, 160, 16, 12)


class Personnage:
    def __init__(self):
        self.x_personnage = 0
        self.vitesse = 2
        self.personnage_marche = False
        self.direction = 1
    
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.x_personnage > 0:
            self.x_personnage = max(self.x_personnage - self.vitesse, 0)
            self.direction = -1
            self.personnage_marche = True
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x_personnage < pyxel.width - 16:
            self.x_personnage = min(self.x_personnage + self.vitesse, pyxel.width - 16)
            self.direction = 1
            self.personnage_marche = True
    
    def draw(self):
        if self.personnage_marche:
            if pyxel.frame_count % 6 < 3:
                pyxel.blt(self.x_personnage, pyxel.height - 16, 0, 0, 0, self.direction*16, 16, 12)
            else:
                pyxel.blt(self.x_personnage, pyxel.height - 16, 0, 16, 0, self.direction*16, 16, 12)
            self.personnage_marche = False
        else:
            pyxel.blt(self.x_personnage, pyxel.height - 16, 0, 0, 0, self.direction*16, 16, 12)


class Foret:
    def __init__(self):
        self.x = 0
        self.vitesse = 1
        self.direction = 1

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = self.x + self.vitesse
            self.direction = 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = self.x - self.vitesse
            self.direction = -1
    
    def draw(self):
        k = 0
        while self.x - k*160 > -160 :
            pyxel.blt(self.x - k*160,pyxel.height-16, 0, 0, 48, 160, 16, 12)
            k = k + 1
        k = 1
        while self.x + k*160 < pyxel.width :
            pyxel.blt(self.x + k*160,pyxel.height-16, 0, 0, 48, 160, 16, 12)
            k = k + 1


class App:
    def __init__(self):
        pyxel.init(LARGEUR, HAUTEUR, title="Tuto 4", quit_key=pyxel.KEY_Q, fps=30)
        # on charge le fichier de ressources
        pyxel.load("jump_game.pyxres")
        self.personnage = Personnage()
        # liste des nuages visibles
        self.nuages = []
        premier_nuage = Nuage(x = pyxel.width//2-80, y = pyxel.height//4)
        self.nuages.append(premier_nuage)
        self.foret = Foret()
        self.cerises = [] # liste des cerises
        self.score = 0
        # on lance l'application
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.personnage.update()
        for nuage in self.nuages:
            nuage.update()
            if nuage.x < 10 and not nuage.replaced:
                nouveau_nuage = Nuage()
                self.nuages.append(nouveau_nuage)
                nuage.replaced = True
            if nuage.x < -160:
                self.nuages.remove(nuage)
        self.foret.update()
        if pyxel.frame_count % pyxel.rndi(30, 60) == 0:  # Générer une cerise toutes les 1 à 2 secondes (à 30 fps)
            self.cerises.append(Cerise(pyxel.rndi(0, pyxel.width - 16), -16))  # Position aléatoire en x
            
        for cerise in self.cerises:
            cerise.update()
            if cerise.y > pyxel.height:
                self.cerises.remove(cerise)
            if (
                abs(cerise.x - self.personnage.x_personnage) < 16 and abs(cerise.y - (pyxel.height - 16)) < 16
            ):  # Collision détectée !
                self.cerises.remove(cerise)
                self.score += 1


    def draw(self):
        # on efface l'écran et on remplit la fenêtre de bleu
        pyxel.cls(12)
        # Tracé de la montagne
        pyxel.blt(pyxel.width//2 - 80, pyxel.height-50, 0, 0, 64, 160, 24)
        # Tracé du ciel dégradé
        pyxel.blt(0,pyxel.height-32, 0, 0, 88, 160, 32, 12)
        pyxel.blt(160,pyxel.height-32, 0, 0, 88, 160, 32, 12)
        # tracé des forêts
        self.foret.draw()
        # Tracé des nuages
        for nuage in self.nuages:
            nuage.draw()
        self.personnage.draw()
        for cerise in self.cerises:
            cerise.draw()
        self.personnage.draw()
        pyxel.text(5, 5, f"Score: {self.score}", pyxel.COLOR_WHITE) # Affichage du score

App()
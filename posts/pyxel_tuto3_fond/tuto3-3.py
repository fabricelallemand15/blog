import pyxel

LARGEUR = 256
HAUTEUR = 128

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


class App:
    def __init__(self):
        pyxel.init(LARGEUR, HAUTEUR, title="Tuto 2", quit_key=pyxel.KEY_Q, fps=30)
        # on charge le fichier de ressources
        pyxel.load("jump_game.pyxres")
        # variable définissant l'abscisse initiale du personnage
        self.x_personnage = 0
        # variable définissant la vitesse du personnage
        self.vitesse = 2
        # variable indiquant si un déplacement est en cours
        self.personnage_marche = False
        # variable indiquant la direction du personnage
        self.direction = 1
        # liste des nuages visibles
        self.nuages = []
        premier_nuage = Nuage(x = pyxel.width//2-80, y = pyxel.height//4)
        self.nuages.append(premier_nuage)
        # on lance l'application
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x_personnage = max(self.x_personnage - self.vitesse, 0)
            self.direction = -1
            self.personnage_marche = True
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x_personnage = min(self.x_personnage + self.vitesse, pyxel.width - 16)
            self.direction = 1
            self.personnage_marche = True
        for nuage in self.nuages:
            nuage.update()
            if nuage.x < 10 and not nuage.replaced:
                nouveau_nuage = Nuage()
                self.nuages.append(nouveau_nuage)
                nuage.replaced = True
            if nuage.x < -160:
                self.nuages.remove(nuage)

    def draw(self):
        # on efface l'écran et on remplit la fenêtre de bleu
        pyxel.cls(12)
        # Tracé de la montagne
        pyxel.blt(pyxel.width//2 - 80, pyxel.height-50, 0, 0, 64, 160, 24)
        # Tracé du ciel dégradé
        pyxel.blt(0,pyxel.height-32, 0, 0, 88, 160, 32, 12)
        pyxel.blt(160,pyxel.height-32, 0, 0, 88, 160, 32, 12)
        # Tracé de la forêt
        pyxel.blt(0,pyxel.height-16, 0, 0, 48, 160, 16, 12)
        pyxel.blt(160,pyxel.height-16, 0, 0, 48, 160, 16, 12)
        # Tracé des nuages
        for nuage in self.nuages:
            nuage.draw()
        # on affiche le personnage à l'abscisse x_personnage et à l'ordonnée 128 - 16
        if self.personnage_marche:
            if pyxel.frame_count % 6 < 3:
                pyxel.blt(self.x_personnage, pyxel.height - 16, 0, 0, 0, self.direction*16, 16, 12)
            else:
                pyxel.blt(self.x_personnage, pyxel.height - 16, 0, 16, 0, self.direction*16, 16, 12)
            self.personnage_marche = False
        else:
            pyxel.blt(self.x_personnage, pyxel.height - 16, 0, 0, 0, self.direction*16, 16, 12)

App()
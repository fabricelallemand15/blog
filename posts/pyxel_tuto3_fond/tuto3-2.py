import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 128, title="Tuto 2", quit_key=pyxel.KEY_Q, fps=30)
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
        pyxel.blt(pyxel.width//2 - 80, pyxel.height//4, 0, 0, 24, 160, 16, 12)
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
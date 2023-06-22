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
        # on lance l'application
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x_personnage = max(self.x_personnage - self.vitesse, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x_personnage = min(self.x_personnage + self.vitesse, pyxel.width - 16)

    def draw(self):
        # on efface l'écran et on remplit la fenêtre de bleu
        pyxel.cls(12)
        # on affiche le personnage à l'abscisse x_personnage et à l'ordonnée 128 - 16
        pyxel.blt(self.x_personnage, pyxel.height - 16, 0, 0, 0, 16, 16)

App()
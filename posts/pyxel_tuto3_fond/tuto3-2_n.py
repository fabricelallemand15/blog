import pyxel

class Personnage:

    def __init__(self):
        self.x = 0
        self.y = pyxel.height - 16
        self.direction = 1
        self.marche = False
        self.vitesse = 2
        self.personnage_marche = False

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(self.x - self.vitesse, 0)
            self.direction = -1
            self.personnage_marche = True
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(self.x + self.vitesse, pyxel.width - 16)
            self.direction = 1
            self.personnage_marche = True
    
    def draw(self):
        if self.personnage_marche:
            if pyxel.frame_count % 6 < 3:
                pyxel.blt(self.x, pyxel.height-16, 0, 0, 0, self.direction*16, 16, 12)
            else:
                pyxel.blt(self.x, pyxel.height-16, 0, 16, 0, self.direction*16, 16, 12)
            self.personnage_marche = False
        else:
            pyxel.blt(self.x, pyxel.height-16, 0, 0, 0, self.direction*16, 16, 12)
    

class App:
    def __init__(self):
        pyxel.init(256, 128, fps=30)
        pyxel.load("jump_game.pyxres")
        self.personnage = Personnage()
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.personnage.update()

    def draw(self):
        pyxel.cls(12)
         # Tracé de la montagne
        pyxel.blt(pyxel.width//2 - 80, pyxel.height-50, 0, 0, 64, 160, 24)
        # Tracé du ciel dégradé
        pyxel.blt(0,pyxel.height-32, 0, 0, 88, 160, 32, 12)
        pyxel.blt(160,pyxel.height-32, 0, 0, 88, 160, 32, 12)
        self.personnage.draw()

App()
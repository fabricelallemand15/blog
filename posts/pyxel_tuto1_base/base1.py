import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 256, title="Exemple de base", quit_key=pyxel.KEY_Q, fps=30)
        pyxel.run(self.update, self.draw)
        
    def update(self):
        pass

    def draw(self):
        pass

App()
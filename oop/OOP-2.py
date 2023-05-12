# Наследование
class Geom:     # ---> Главный класс
    name = 'Geom'
    def set_coord(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.draw()
    def draw(self):
        print('Построение фигуры')

class Line(Geom):     # ---> Дочерний класс
#          ----
    name = 'Line'
    def draw(self):
        print('Построение линии')

class Reqt(Geom):
    pass

l = Line()
r = Reqt()
g = Geom()
# l.set_coord(1,1,2,2)
# r.set_coord(3,3,4,4)
# print(l.__dict__)
# print(r.__dict__)
print(l.name)
print(r.name)
l.draw()
r.draw()
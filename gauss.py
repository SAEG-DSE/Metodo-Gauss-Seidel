class Gauss(object):

    def __init__(self,matriz):
        self.matriz = matriz

    def convergencia_d1(self):
        d1 = ( abs(self.matriz[0][1]) + abs(self.matriz[0][2]) ) / float(abs(self.matriz[0][0]))
        return d1

    def convergencia_d2(self):
        d2 = ( (abs(self.matriz[1][0]) * self.convergencia_d1() + abs(self.matriz[1][2])) / float(abs(self.matriz[1][1])) )
        return d2

    def convergencia_d3(self):
        d3 = ( (abs(self.matriz[2][0]) * self.convergencia_d1() + abs(self.matriz[2][1]) * self.convergencia_d2() ) / float(abs(self.matriz[2][2])) )
        return round(d3, 3)

    def iteraX(self,variavel_y,variavel_z):
        valor_x = abs((7 -2*variavel_y - variavel_z)/10.0)
        return valor_x

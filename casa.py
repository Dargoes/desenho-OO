import time
import turtle


class Forma:
    '''Classe base de todas as formas geométricas.
    
    Reúne atributos e métodos comuns a todas.
    '''
    def __init__(self, nome, cor, x, y):
        self.nome = nome
        self.cor = cor
        self.x = x
        self.y = y
    
    def desenhar(self):
        '''Desenha a forma.
        
        Esse método implementa o comportamento padrão para desenhar qualquer forma.
        As subclasses se preocupam apenas com as especificidades delas próprias.
        '''
        t = turtle.Turtle()
        t.up()
        t.hideturtle()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)  # Escolhe a cor do preenchimento
        t.begin_fill()   # Inicia o preenchimento
        self.desenhar_forma(t)
        t.end_fill()  # Encerra o preenchimento
    
    def desenhar_forma(self, t: turtle.Turtle):
        '''Desenha uma forma específica.
        
        Esse método é abstrato, ou seja, deve ser sobrescrito pelas subclasses.
        Isso acontece porque a classe Forma é genérica, não corresponde a nenhuma forma geométrica específica.
        Logo, não pode implementar um comportamento de desenho de nenhuma forma específica.
        '''
        raise Exception('Método abstrado. Sobrescreva-o nas subclasses.')


class Retangulo(Forma):
    '''Um retângulo.'''
    def __init__(self, largura, altura, cor, x, y):
        super().__init__('Retângulo', cor, x, y)
        self.largura = largura
        self.altura = altura

    def desenhar_forma(self, t: turtle.Turtle):
        '''Desenha o retângulo.

        Implementa o comportamento específico do retângulo, que a Forma não poderia implementar.
        '''
        for _ in range(2):
            for tam in [self.largura, self.altura]:
                t.forward(tam)
                t.right(90)

class Circulo(Forma):
    '''Um círculo.'''
    def __init__(self, raio, cor, x, y):
        super().__init__('Círculo', cor, x, y)
        self.raio = raio
    
    def desenhar_forma(self, t: turtle.Turtle):
        '''Desenha o retângulo.

        Implementa o comportamento específico do círculo, que a Forma não poderia implementar.
        '''
        t.left(180)  # Desenha o círculo para baixo
        t.circle(self.raio)

class Estrela(Forma):
    '''Uma estrela.'''
    def __init__(self, lado, cor, x, y):
        super().__init__('estrela', cor, x, y)
        self.lado = lado
    
    def desenhar_forma(self, t: turtle.Turtle):
        for side in range(5):
            t.forward(self.lado)
            t.right(120)
            t.forward(self.lado)
            t.right(72 - 120)


class Triangulo(Forma):
    '''Um losangulo.'''
    def __init__(self, lado, cor, x, y):
        super().__init__('estrela', cor, x, y)
        self.lado = lado
    def desenhar_forma(self, t: turtle.Turtle):
            t.forward(self.lado)
            t.left(120)
            t.forward(self.lado)
            t.left(60)
    

# Instancia os objetos para poder usar
triangulo = Triangulo(300, 'green', -175, 0)
ret = Retangulo(300, 300, 'red', -175, 0)
ret2 = Retangulo(50, 150, 'blue', -140, -150)
ret3 = Retangulo(75, 75, 'white', -50, -150)
circ = Circulo(5, 'black', -100, -200)
estrela = Estrela(10, 'white', -125, 50)
formas = [ret, triangulo, ret2, circ, estrela, ret3]
for f in formas:
    f.desenhar()



# Aguarda 3 segundos antes de fechar
time.sleep(3)
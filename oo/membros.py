class contador:
    contador = 0  # atributo de classe (compartilhado por todos)

    def incmaluco(self):
        self.contador = self.contador + 1  
        # aqui cria/usa atributo do proprio obj (n mexe no da classe)
        return self.contador    
    
    def inst(self):
        return 'estou bem!'  # metodo normal (usa self)

    @classmethod
    def inc(cls):
        cls.contador += 1  # altera contador da classe (global pra todos objs)
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1  # diminui contador da classe
        return cls.contador

    @staticmethod
    def mais_um(n):
        return n + 1  # metodo independente (n usa self nem cls)
    

c1 = contador()

print(c1.inst())        # metodo de instancia
print(c1.incmaluco())   # contador do obj
print(c1.incmaluco())

print(contador.inc())   # contador da classe
print(contador.inc())
print(contador.inc())

print(contador.dec())
print(contador.dec())

print(contador.contador)  # valor final da classe
print(contador.mais_um(10))  # static method
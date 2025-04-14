class Polinomio:
    def __init__(self):
        self.terminos = {}

    def agregar_termino(self, coef, exp):
        if coef != 0:
            self.terminos[exp] = self.terminos.get(exp, 0) + coef

    def eliminar_termino(self, exp):
        if exp in self.terminos:
            del self.terminos[exp]

    def existe_termino(self, exp):
        return exp in self.terminos

    def mostrar(self):
        if not self.terminos:
            print("0")
            return
        expresion = []
        for exp in sorted(self.terminos.keys(), reverse=True):
            coef = self.terminos[exp]
            if coef == 0:
                continue
            if exp == 0:
                expresion.append(f"{coef}")
            elif exp == 1:
                expresion.append(f"{coef}x")
            else:
                expresion.append(f"{coef}x^{exp}")
        print(" + ".join(expresion).replace("+ -", "- "))

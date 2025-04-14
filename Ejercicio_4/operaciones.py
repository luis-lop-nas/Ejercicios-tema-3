from polinomio import Polinomio

def restar_polinomios(p1, p2):
    resultado = Polinomio()
    for exp, coef in p1.terminos.items():
        resultado.agregar_termino(coef, exp)
    for exp, coef in p2.terminos.items():
        resultado.agregar_termino(-coef, exp)
    return resultado

def dividir_polinomios(dividendo, divisor):
    cociente = Polinomio()
    resto = Polinomio()
    for exp, coef in dividendo.terminos.items():
        resto.agregar_termino(coef, exp)

    while resto.terminos and max(resto.terminos) >= max(divisor.terminos):
        exp_div = max(resto.terminos)
        exp_dvs = max(divisor.terminos)
        coef_div = resto.terminos[exp_div]
        coef_dvs = divisor.terminos[exp_dvs]

        nuevo_exp = exp_div - exp_dvs
        nuevo_coef = coef_div / coef_dvs
        cociente.agregar_termino(nuevo_coef, nuevo_exp)

        temp = Polinomio()
        for exp, coef in divisor.terminos.items():
            temp.agregar_termino(nuevo_coef * coef, exp + nuevo_exp)
        for exp, coef in temp.terminos.items():
            resto.agregar_termino(-coef, exp)

    return cociente, resto

def eliminar_termino(p, exp):
    p.eliminar_termino(exp)

def existe_termino(p, exp):
    return p.existe_termino(exp)

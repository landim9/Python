import calculadora

def test_processa_calculo_multiplicacao():
    num1 = 8 
    num2 = 2
    oper = "x"  
    resultado = calculadora.processa_calculo(num1, num2, oper)
    assert resultado == 16
def test_processa_calculo_adicao():
    num1 = 8 
    num2 = 2
    oper = "+"  
    resultado = calculadora.processa_calculo(num1, num2, oper)
    assert resultado == 10
def test_processa_calculo_substracao():
    num1 = 8 
    num2 = 2
    oper = "-"  
    resultado = calculadora.processa_calculo(num1, num2, oper)
    assert resultado == 6
def test_processa_calculo_divisao():
    num1 = 8 
    num2 = 2
    oper = "x"  
    resultado = calculadora.processa_calculo(num1, num2, oper)
    assert resultado == 16
def test_processa_calculo_porcentagem():
    num1 = 100 
    num2 = 50
    oper = "%"  
    resultado = calculadora.processa_calculo(num1, num2, oper)
    assert resultado == 50
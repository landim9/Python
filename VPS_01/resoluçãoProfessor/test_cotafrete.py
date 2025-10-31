import cotafrete

def test_recebe_destino_1():
    destino = 1
    distancia = cotafrete.tabela_distancia(destino)
    assert distancia == 102

def test_recebe_destino_2():
    destino = 2
    distancia = cotafrete.tabela_distancia(destino)
    assert distancia == 112

def test_recebe_destino_3():
    destino = 3
    distancia = cotafrete.tabela_distancia(destino)
    assert distancia == 98

def test_recebe_destino_4():
    destino = 4
    distancia = cotafrete.tabela_distancia(destino)
    assert distancia == 2922

def test_recebe_destino_5():
    destino = 5
    distancia = cotafrete.tabela_distancia(destino)
    assert distancia == 6294

def test_calcula_frete():
        destino = 1
        distancia = 102
        embalagem = 1
        altura = 1.0
        largura = 1.0
        profundidade = 1.0
        peso = 1.0
        fator = cotafrete.calcula_frete_frete(destino, distancia, embalagem, altura, largura, profundidade, peso)
        assert fator == ((altura * largura * profundidade * peso) * (1 + fator)) * (1+(distancia * 9.8))


# def test_mostra_cota_frete():
#         destino = 1
#         distancia = 102
#         embalagem = 1
#         altura = 1
#         largura = 1
#         profundidade = 1
#         peso = 1
#         fator = cotafrete.mostra_cotacao(destino, embalagem, altura, largura, profundidade, peso, distancia, valor_frete)

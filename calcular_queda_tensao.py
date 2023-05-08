# -*- coding: utf-8 -*-

tabela_queda_tensao_cobre_mono_bifasica = {
    1.5: 27.62,
    2.5: 16.93,
    4: 10.56,
    6: 7.07,
    10: 4.23,
    16: 2.68,
    25: 1.71,
    35: 1.25,
    50: 0.94,
    70: 0.67,
    95: 0.50,
    120: 0.41,
    150: 0.34,
    185: 0.28,
    240: 0.23
}

tabela_queda_tensao_cobre_trifasica = {
    1.5: 23.89,
    2.5: 14.64,
    4: 9.13,
    6: 6.12,
    10: 3.66,
    16: 2.32,
    25: 1.48,
    35: 1.08,
    50: 0.81,
    70: 0.58,
    95: 0.43,
    120: 0.35,
    150: 0.30,
    185: 0.25,
    240: 0.20
}


tabela_queda_tensao_aluminio_mono_bifasica = {
    16: 4.58,
    25: 2.95,
    35: 2.18,
    50: 1.66,
    70: 1.20,
    95: 0.91,
    120: 0.75,
    150: 0.64,
    185: 0.54,
    240: 0.44,
    300: 0.38,
    400: 0.33,
    500: 0.28
}

tabela_queda_tensao_aluminio_trifasica = {
    16: 3.82,
    25: 2.42,
    35: 1.77,
    50: 1.32,
    70: 0.92,
    95: 0.68,
    120: 0.55,
    150: 0.46,
    185: 0.37,
    240: 0.30,
    300: 0.25,
    400: 0.21,
    500: 0.17
}


def calcular_queda_tensao(tipo_ligacao, distancia, potencia, tensao, limite_queda_tensao, tipo_cabo):
    # Converter a tensão de entrada se for 127/220 ou 220/380
    if tensao == "127/220":
        tensao = 220
    elif tensao == "220/380":
        tensao = 380
    else:
        tensao = int(tensao)

    # Calcular corrente de linha do circuito
    if tipo_ligacao == 'monofasico':
        corrente = potencia / tensao
    elif tipo_ligacao == 'bifasico':
        corrente = potencia / (tensao * (3 ** 0.5))
    elif tipo_ligacao == 'trifasico':
        corrente = (potencia / 3) / (tensao / (3 ** 0.5))

    # Encontrar a bitola do cabo adequada
    if tipo_cabo == "cobre":
        tabela_queda_tensao = tabela_queda_tensao_cobre_mono_bifasica if tipo_ligacao != 'trifasico' else tabela_queda_tensao_cobre_trifasica
    elif tipo_cabo == "aluminio":
        tabela_queda_tensao = tabela_queda_tensao_aluminio_mono_bifasica if tipo_ligacao != 'trifasico' else tabela_queda_tensao_aluminio_trifasica

    for secao_nominal, queda_tensao_por_amp_km in tabela_queda_tensao.items():
        queda_tensao = (queda_tensao_por_amp_km *
                        (distancia / 1000) * corrente * 100) / tensao
        if queda_tensao <= limite_queda_tensao:
            bitola_cabo = secao_nominal
            break

    return bitola_cabo, round(queda_tensao, 2)


'''
# Exemplo de uso da função
cenarios = [
    ('monofasico', 100, 10000, 127, 5, 'cobre'),
    ('monofasico', 100, 10000, 127, 5, 'aluminio'),
    ('monofasico', 100, 10000, 220, 5, 'aluminio'),
    ('bifasico', 100, 10000, '127/220', 5, 'aluminio'),
    ('bifasico', 100, 10000, '220/380', 5, 'aluminio'),
    ('trifasico', 100, 10000, '127/220', 5, 'aluminio'),
    ('trifasico', 100, 10000, '220/380', 5, 'aluminio')
]

'''

"""Desafio Classificador de nível de Herói

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 6.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**"""


heroi = input("Digite o nome do herói: ")

xp = float(input("Digite a quantidade de XP: "))

niveis = {
    (0, 1000): "Ferro",
    (1001, 2000): "Bronze",
    (2001, 5000): "Prata",
    (6001, 7000): "Ouro",
    (7001, 8000): "Platina",
    (8001, 9000): "Ascendente",
    (9001, 10000): "Imortal",
    (10001, float('inf')): "Radiante"
    }

for xp_range, level in niveis.items():
    if xp_range[0] <= xp <= xp_range[1]:
        nivel = level
        break

print(f"O Herói de nome {heroi} está no nível de {nivel}")

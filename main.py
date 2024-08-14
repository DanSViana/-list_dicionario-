# tupla
chaves = ('Nome', 'Idade', 'Profissão')

# # lista de dicionário primeira opção
# usuário = [
#     {
#         'Nome': 'Fulano',
#         'Idade': 28,
#         'Profissão': 'Autônomo'
#     },
#     {
#         'Nome': 'Cicrano',
#         'Idade': 18,
#         'Profissão': 'Desempregado'
#     },
#     {
#         'Nome':'Beltrano',
#         'Idade': 33,
#         'Profissão': 'Empreendedor'
#     }
# ]


# lista de dicionário segunda opção (dessa forma o código fica mais integro)
usuarios = [
    {
        chaves[0]: 'Fulano',
        chaves[1]: 28,
        chaves[2]: 'Autônomo'
    },
    {
        chaves[0]: 'Cicrano',
        chaves[1]: 18,
        chaves[2]: 'Desempregado'
    },
    {
        chaves[0]:'Beltrano',
        chaves[1]: 33,
        chaves[2]: 'Empreendedor'
    }
]

# mostrar a lista de usuários
print(f'{'_'*10} LISTA DE USUÁRIOS {'_'*10}\n')

for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')

    print(f'\n{'_'*10}\n')

# adicionar um novo dicionário a lista
usuario = {}

for i in range(len(chaves)):
    usuario[chaves[i]] = input(f'Informe {chaves[i]}:')

usuarios.append(usuario)
print(f'\nUsuário cadastrado com sucesso!')

# reexibindo a nova lista de usuário
print(f'\n{'='*10} LISTA DE USUÁRIOS {'='*10}\n') 

for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')

    print(f'\n{'='*10}\n')

    
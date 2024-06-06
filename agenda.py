#uma agenda para salvar editar deletar e marcar contato como favorito

def salvar_contato (contatos, nome, numero):
    contatos_salvos = {"nome": nome, "numero": numero,"favoritado": False}
    contatos.append(contatos_salvos)
    print(f"O contato com o nome de {nome} foi adicionado com sucesso")
    return

def ver_contatos (contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favoritado"] else " "
        print(f"{indice}. [{status}] Contato: {contato['nome']} | Numero:{contato['numero']}")
    return

def editar_contato(contatos, indice_contato, novo_nome_contato, novo_numero_contato):
    novo_indice_contato = int(indice_contato) -1
    if novo_indice_contato >= 0 and novo_indice_contato < len(contatos):
        contatos[novo_indice_contato]["nome"] = novo_nome_contato
        contatos[novo_indice_contato]["numero"] = novo_numero_contato
        print(f"O contato {indice_contato} foi atualizado com novos dados que são {novo_nome_contato} e {novo_numero_contato} ")
    else:
        print("indice invalido")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) -1
    contatos[indice_contato_ajustado]["favoritado"] = True
    print(f"Contato com o indice {indice_contato} marcada como favorita")
    return

def deletar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) -1
    if 0 <= indice_contato_ajustado < len(contatos):
        contato_excluido = contatos.pop(indice_contato_ajustado)
        print(f"Contato '{contato_excluido['nome']}' foi deletado com sucesso") 
    else:
        print("indice de contato invalido")
    return
contatos =[]
while True:
    print("\nAgenda Virtual")
    print("1. Adicionar Novo contato")
    print("2. Ver Contatos")
    print("3. Editar contato existente")
    print("4. Marcar contato como Favorito")
    print("5. Deletar contato")
    print("6. Sair")



        
    escolha = input("Digite sua escolha: ")


    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        numero = input("Digite o numero do contato: ")
        salvar_contato(contatos, nome, numero)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o indice do contato que deseja alterar: ")
        novo_nome_contato = input("Digite o novo nome do contato: ")
        novo_numero_contato = input("Digite o novo numero do contato: ")
        editar_contato(contatos, indice_contato, novo_nome_contato, novo_numero_contato)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)

    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato= input("indice do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)
    
    elif escolha == "6":
        break


print("Programa Finalizado!")
# Lista de tarefas no terminal

tarefas = []
proximo_id = 1


def adicionar_tarefa():
    global proximo_id

    descricao = input("Digite a descrição da tarefa: ").strip()

    if not descricao:
        print("A descrição não pode ficar vazia!")
        return

    tarefa = {
        "id": proximo_id,
        "descricao": descricao,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    proximo_id += 1

    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n========== LISTA DE TAREFAS ==========")

    for tarefa in tarefas:
        print("--------------------------------------")
        print(f"ID: {tarefa['id']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Status: {tarefa['status']}")

    print("--------------------------------------")
    print(f"Total de tarefas: {len(tarefas)}")
    print("======================================")
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n===== LISTA DE TAREFAS =====")

    for tarefa in tarefas:
        print(f"\nID: {tarefa['id']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Status: {tarefa['status']}")


def concluir_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        id_tarefa = int(input("\nDigite o ID da tarefa: "))
    except ValueError:
        print("Digite um número válido!")
        return

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = "Concluída"
            print("Tarefa concluída com sucesso!")
            return

    print("Tarefa não encontrada!")


def remover_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        id_tarefa = int(input("\nDigite o ID da tarefa que deseja remover: "))
    except ValueError:
        print("Digite um número válido!")
        return

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
            return

    print("Tarefa não encontrada!")


def alterar_descricao():
    listar_tarefas()

    if not tarefas:
        return

    try:
        id_tarefa = int(input("\nDigite o ID da tarefa: "))
    except ValueError:
        print("Digite um número válido!")
        return

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            nova_descricao = input("Digite a nova descrição: ").strip()

            if not nova_descricao:
                print("A descrição não pode ficar vazia!")
                return

            tarefa["descricao"] = nova_descricao

            print("Descrição alterada com sucesso!")
            return

    print("Tarefa não encontrada!")


def menu():
    while True:
        print("\n========== SISTEMA DE TAREFAS ==========")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Alterar descrição")
        print("6 - Sair")
        print("========================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            concluir_tarefa()

        elif opcao == "4":
            remover_tarefa()

        elif opcao == "5":
            alterar_descricao()

        elif opcao == "6":
            print("Encerrando o sistema. Até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.")


# Iniciar o sistema
menu()
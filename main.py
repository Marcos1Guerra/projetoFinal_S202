from database import Database
from supermercado_database import SupermercadoDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.215.126.93:7687", "neo4j", "acres-sample-formulas")
db.drop_all()

# Criando uma instância para interagir com o banco de dados
supermercado = SupermercadoDatabase(db)


def main():
    valor_total_da_compra = 0
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    supermercado.create_pessoa(nome, cpf)

    print("Bem vindo ao supermercado " + nome + "!")

    while True:
        print("\n=== MENU ===")
        print("0. Sair")
        print("1. Criar Produto")
        print("2. Ler Produto")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Criar Relacionamento")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            tipo = input("Digite o tipo do produto: ")
            valor = input("Digite o valor do produto: ")
            supermercado.create(nome, tipo, valor)

        elif opcao == "2":
            nome = input("Digite o nome do produto: ")
            supermercado.read(nome)

        elif opcao == "3":
            nome = input("Digite o nome do produto: ")
            new_valor = input("Digite o novo valor do produto: ")
            supermercado.update(nome, new_valor)

        elif opcao == "4":
            nome = input("Digite o nome do produto: ")
            supermercado.delete(nome)

        elif opcao == "5":
            nome_pessoa = input("Digite o seu nome: ")
            nome_produto = input("Digite o nome do produto que comprou: ")

            supermercado.create_pessoa_produto(nome_pessoa, nome_produto)
            valor = supermercado.valor_produto(nome_produto)

            if valor is not None:  # Verifica se o valor não é None
                valor = int(valor[0])   # Converte o valor para um número inteiro
                valor_total_da_compra += int(valor)
            else:
                print("Valor do produto não encontrado.")

        elif opcao == "0":
            print("O valor total da compra foi de R$" + str(valor_total_da_compra))
            valor_total_da_compra = 0
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

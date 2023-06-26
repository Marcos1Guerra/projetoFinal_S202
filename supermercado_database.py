class SupermercadoDatabase:
    def __init__(self, database):
        self.db = database

    def create_pessoa(self, nome, cpf):
        query = "CREATE (:Pessoa {nome: $nome, cpf: $cpf})"
        parameters = {"nome": nome, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def create(self, nome, tipo, valor):
        query = "CREATE (:Produto {nome: $nome, tipo: $tipo, valor: $valor})"
        parameters = {"nome": nome, "tipo": tipo, "valor": valor}
        self.db.execute_query(query, parameters)

    def read(self, nome):
        query = "MATCH (p:Produto{nome: $nome}) RETURN p"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [result["p"] for result in results]

    def update(self, nome, new_valor):
        query = "MATCH (p:Produto {nome: $nome}) SET p.valor = $new_valor"
        parameters = {"nome": nome, "new_valor": new_valor}
        self.db.execute_query(query, parameters)

    def delete(self, nome):
        query = "MATCH (p:Produto {nome: $nome}) DETACH DELETE p"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def create_pessoa_produto(self, nome_pessoa, nome_produto):
        query = "MATCH (a:Pessoa {nome: $nome_pessoa}),(b:Produto {nome: $nome_produto}) CREATE (a)-[:COMPROU]->(b)"
        parameters = {"nome_pessoa": nome_pessoa, "nome_produto": nome_produto}
        self.db.execute_query(query, parameters)

    def valor_produto(self, nome):
        query = "MATCH (p:Produto {nome: $nome}) RETURN p.valor"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [result["p.valor"] for result in results]


import sqlite3 

conexao = sqlite3.connect('conexao_dados')
cursor =  conexao.cursor()

# 1-- Crie uma tabela chamado "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
result = cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(130), endereco VARCHAR(200), email VARCHAR(80));')


# 2-- Insira pelo menos 5 registros de alunos na tabela que você criou no execício anterior.
result = cursor.execute('insert into alunos (id, nome, idade, curso) values ( 1, 'Alice', 20, 'Odonto'), ( 2, 'Sophia', 27, 'Medicina' ), ( 3, 'Juliene', 24, 'Engenharia', ), ( 4, 'Suza', 33, 'Veterinária', ), ( 5, 'Chaislene', 32, 'Ciência',)')


# 3-- Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:
# A- Selecionar todos os registros da tabela "alunos".
result = cursor.execute('select * from alunos')


# B- Selecionar o nome e a idade dos alunos com mais de 20 anos.
result = cursor.execute('select nome, idade from alunos where idade > 20')

# C- Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
result = cursor.execute('select * from alunos where curso - 'Engenharia' order by nome')

# D- Contar o número total de alunos na tabela.
result = cursor.execute('select count(*) from alunos')


# 4-- Atualização e Remoção
# A- Atualize a idade de um aluno específico na tabela.
result = cursor.execute('update alunos set idade = 24 where id = 25')

# B- Remova um aluno pelo seu ID.
result = cursor.execute('delete from aunos where id = 2')


# 5-- Crie uma tabela e insira dados. Criar uma tabela chamada "clientes" com os campos:
# id (chave primária), nome (texto), idade (inteiro) e saldo (float).
# Insira alguns registros de cliente na tabela.
result = cursor.execute('create table cliente (id INTEGER primary key, nome VARCHAR(180), idade INTEGER, saldo FLOAT )')

result = cursor.execute('insert into clientes (id, nome, idade, saldo) values ( 1, 'Alice', 20, 900), ( 2, 'Sophia', 27, 600 ), ( 3, 'Juliene', 24, 200, ), ( 4, 'Suza', 33, 5500, ), ( 5, 'Chaislene', 32, 1000,)')


# 6-- Consultas e Funções Agragadas
# Escreva consultas SQL para realizar as seguintes tarefas:
# A- Selecione o nome e a idade dos clientes com idade superior a 30 anos.
result = cursor.execute('select nome, idade from clientes where >= 30')

# B-  Calcule o saldo médio dos clientes.
result = cursor.execute('select AVG(saldo) from clientes')

# C- Encontre o cliente com o saldo máximo.
result = cursor.execute('select nome from clientes where saldo = (select max(saldo) from clientes)') 

# D- Conte quantos clientes têm saldo acima de 1000.
result = cursor.execute('select count(*) from clientes where saldo >= 1000') 


# 7-- Atualização e remoção com condições.
# A- Atualize o saldo de u cliente específico.
result = cursor.execute('update clientes set saldo = 2000 where id = 1') 

# B- Remova um cliente pelo ID.
result = cursor.execute('delete from where id = 1')


# 8-- Junção de tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "cliente"), produto (texto) e valor (real).
#  Insira algumas compras associadas a clientes existentes na tabela "clientes".
result = cursor.execute('create table compras (id INTEGER primary key, cliente_id INTEGER, produto VARCHAR(150), valor FLOAT, CONSTRAINT fk_clientes FOREIGN  REFERENCES clientes (id))')

result = cursor.execute('insert into compras (id, cliente_id, produto, valor) values ( 1, 1, 'Livro', 25.0), ( 2, 1, 'Caderno', 15.0), ( 3, 1, 'Caneta', 5.0,)')

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
result = cursor.execute('select c.nome, co.produto, co.valor from compras as co inner join clientes as c on c.id = co.clientes_id')

for item in result:
    print(item)

conexao.commit()
conexao.close

#conexao.commit()
#conexao.close




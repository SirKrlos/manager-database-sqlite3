# Gerenciador de Banco de Dados sqlite3


## Instalar usando python3

```bash
python3 -m pip install git+https://github.com/JoseCarlosSkar/manager-database-sqlite3
```

---

## Importar

```python
import manager_database_sqlite3 as mds3
```
Recomendado importar com o nome mds3, mas é de preferencia do úsuario.

---

## Criar Banco de Dados Sqlite3

- **mds3.ManagerDatabase** Cria um banco de dados sqlite3.

<table style="border:1px solid black; margin-left:auto; margin-right:auto;">
	<tr>
		<th>Parámetro</th>
		<th>Descrição</th>
		<th>Valor padrão</th>
	</tr>
	<tr>
		<td>path_db</td>
		<td>Caminho completo do banco de dados.</td>
		<td>None</td>
	</tr>
</table>

```python
db = mds3.ManagerDatabase (
	path_db = "databases/testdb1.db"
)
```
Criará um banco de dados chamado 'testdb1.db'.

---

## Conectar um Banco de Dados Sqlite3

- **mds3.ManagerDatabase.Connect** Conecta um banco de dados sqlite3.

<table style="border:1px solid black; margin-left:auto; margin-right:auto;">
	<tr>
		<th>Parámetro</th>
		<th>Descrição</th>
		<th>Valor padrão</th>
	</tr>
	<tr>
		<td>path_db</td>
		<td>Caminho completo do banco de dados.</td>
		<td>None</td>
	</tr>
</table>

```python
db = mds3.ManagerDatabase ()
db.Connect (
	path_db = "databases/testdb1.db"
)
```
Conectará um banco de dados chamado 'testdb1.db'.

---

## Desconectar um Banco de Dados Sqlite3

- **mds3.ManagerDatabase.Disconnect** Desconecta um banco de dados sqlite3.

<table style="border:1px solid black; margin-left:auto; margin-right:auto;">
	<tr>
		<th>Parámetro</th>
		<th>Descrição</th>
		<th>Valor padrão</th>
	</tr>
</table>

```python
db = mds3.ManagerDatabase (
	path_db = "databases/testdb1.db"
)
db.Disconnect ()
```
Desconectará um banco de dados chamado 'testdb1.db'.

---

## Verificar se um Banco de Dados Sqlite3 está conectado

- **mds3.ManagerDatabase.IsConnected** Verifica se um banco de dados sqlite3 está conectado.

<table style="border:1px solid black; margin-left:auto; margin-right:auto;">
	<tr>
		<th>Parámetro</th>
		<th>Descrição</th>
		<th>Valor padrão</th>
	</tr>
</table>

```python
db = mds3.ManagerDatabase (
	path_db = "databases/testdb1.db"
)
db.IsConnected ()
```
Verificará se um banco de dados chamado 'testdb1.db' está conectado.

---


## Listar Tabelas

- **mds3.ManagerDatabase.ListTables** Lista tabelas.

<table style="border:1px solid black;margin-left:auto; margin-right:auto;">
	<tr>
		<th>Parámetro</th>
		<th>Descrição</th>
		<th>Valor padrão</th>
	</tr>
</table>


```python
db = mds3.ManagerDatabase (
	path_db = "databases/testdb1.db"
)

tables = db.ListTables ()

db.Disconnect ()
```
Listará as tabela do banco de dados 'testdb1.db'.

---

## Criar Tabela

- **mds3.ManagerDatabase.CreateTable** Cria tabela.

<table style="border:1px solid black;margin-left:auto; margin-right:auto;">
	<tr>
		<th>Parámetro</th>
		<th>Descrição</th>
		<th>Valor padrão</th>
	</tr>
	<tr>
		<td>name_table</td>
		<td>Nome para a tabela.</td>
		<td>None</td>
	</tr>
	<tr>
		<td>keysvalues</td>
		<td>Nome das colunas e seus tipos.</td>
		<td>None</td>
	</tr>
	<tr>
		<td>ifnoexist</td>
		<td>Se True a tabela só será criada se o mesmo não existir.<br>Se False e a tabela existir, será gerado um erro.</td>
		<td>False</td>
	</tr>
</table>


```python
db = mds3.ManagerDatabase (
	path_db = "databases/testdb1.db"
)

db.CreateTable (
	name_table = "Table_test",
	keysvalues = dict (
		id = mds3.keys.INTEGER,
		name = mds3.keys.TEXT
	),
	ifnoexist = True
)

db.Disconnect ()

```
Criará uma tabela chamada 'Table_test' no banco de dados 'testdb1.db'.

---

## Deletar Tabela

- **mds3.ManagerDatabase.DeleteTable** Deleta tabela.

<table style="border:1px solid black;margin-left:auto; margin-right:auto;">
	<tr>
		<th>Parámetro</th>
		<th>Descrição</th>
		<th>Valor padrão</th>
	</tr>
	<tr>
		<td>name_table</td>
		<td>Nome da tabela.</td>
		<td>None</td>
	</tr>
	<tr>
		<td>ifexist</td>
		<td>Se True a tabela só será deletada se o mesmo existir.<br>Se False e a tabela não existir, será gerado um erro.</td>
		<td>False</td>
	</tr>
</table>

```python
db = mds3.ManagerDatabase (
	path_db = "databases/testdb1.db"
)

db.DeleteTable (
	name_table = "Table_test",
	ifexist = True
)

db.Disconnect ()

```
Deletará uma tabela chamada 'Table_test' no banco de dados 'testdb1.db'.

---

## Renomear Tabela

- **mds3.ManagerDatabase.RenameTable** Renomeia tabela.

<table style="border:1px solid black; margin-left:auto; margin-right:auto;">
	<tr>
		<th>Parámetro</th>
		<th>Descrição</th>
		<th>Valor padrão</th>
	</tr>
	<tr>
		<td>name_table</td>
		<td>Nome da tabela original.</td>
		<td>None</td>
	</tr>
	<tr>
		<td>new_name_table</td>
		<td>Novo nome para a tabela.</td>
		<td>None</td>
	</tr>
	<tr>
		<td>ifexist_origin_table</td>
		<td>Se True a tabela original só será renomeda se o mesmo existir.</td>
		<td>False</td>
	</tr>
	<tr>
		<td>ifnoexist_new_table</td>
		<td>Se True a tabela original só será renomeda se não existir uma tabela com o novo nome.</td>
		<td>False</td>
	</tr>
</table>

```python
db = mds3.ManagerDatabase (
	path_db = "databases/testdb1.db"
)

db.RenameTable (
	name_table = "Table_test",
	new_name_table = "Table_test2"
	ifexist_origin_table = True,
	ifnoexist_new_table = False
)

db.Disconnect ()

```
Renomeará uma tabela chamada 'Table_test' para 'Table_test2' no banco de dados 'testdb1.db'.

---

## Verificar se existe Tabela

- **mds3.ManagerDatabase.IsExistTable** Verifica se existe tabela.

<table style="border:1px solid black; margin-left:auto; margin-right:auto;">
	<tr>
		<th>Parámetro</th>
		<th>Descrição</th>
		<th>Valor padrão</th>
	</tr>
	<tr>
		<td>name_table</td>
		<td>Nome da tabela.</td>
		<td>None</td>
	</tr>
</table>

```python
db = mds3.ManagerDatabase (
	path_db = "databases/testdb1.db"
)

isexist = db.IsExistTable (
	name_table = "Table_test"
)

db.Disconnect ()

```
Verificará se uma tabela chamada 'Table_test' existe no banco de dados 'testdb1.db'.

---

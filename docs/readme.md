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

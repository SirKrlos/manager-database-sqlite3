# -*- coding: utf-8 -*-

"""
Strings sql

"""

from manager_database_sqlite3 import factory


def list_tables () -> str :
	"""Retorna sql 'ListTables'"""

	sql = "SELECT name FROM sqlite_master WHERE type = 'table'"

	return sql

def create_table (
	name_table: str = None,
	keysvalues: dict = None
) -> str :
	"""Retorna sql 'CreateTable'"""

	sql = "CREATE TABLE"
	keysvalues_str = factory.keysvaluesToListStr (
		keysvalues = keysvalues
	)

	sql += " " + str ( f"`{name_table}`" ).strip ()
	sql += " " + str ( f"({keysvalues_str})" ).strip ()

	return sql

def delete_table (
	name_table: str = None
) -> str :
	"""Retorna sql 'DeleteTable'"""

	sql = "DROP TABLE"
	sql += " " + str ( f"`{name_table}`" )

	return sql

def rename_table (
	name_table: str = None,
	new_name_table: str = None
) -> str :
	"""Retorna sql 'RenameTable'"""

	sql = "ALTER TABLE"
	sql += " " + f"`{name_table}`"
	sql += " " + "RENAME TO"
	sql += " " + f"`{new_name_table}`"

	return sql

def get_content_table (
	name_table: str = None,
	keysvalues: dict = None
) -> str :
	"""Retorna sql 'GetContentTable'"""

	sql = "SELECT * FROM"
	sql += " " + f"`{name_table}`"

	if keysvalues:
		keysvaluesDictStr = factory.keysvaluesToDictStr ( keysvalues = keysvalues, sep = " AND " )
		sql += " " + "WHERE"
		sql += " " + f"{keysvaluesDictStr}"

	return sql

def add_content_table (
	name_table: str = None,
	keysvalues: dict = None,
) :
	"""Retorna sql 'AddContentTable'"""

	keys = []
	values = []

	for k,v in keysvalues.items ():
		keys.append ( k )
		values.append ( v )

	keys = factory.listToStrSqliteColumn (
		list_columns = keys
	)
	values = factory.listToStrSqliteColumnValue (
		list_columns_values = values
	)

	sql = "INSERT INTO"

	sql += " " + f"`{name_table}`"
	sql += " " + f"({keys})"
	sql += " " + f"VALUES({values})"

	return sql


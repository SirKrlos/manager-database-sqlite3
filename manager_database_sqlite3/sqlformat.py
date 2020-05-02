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


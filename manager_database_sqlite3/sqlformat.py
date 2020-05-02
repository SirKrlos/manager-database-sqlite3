# -*- coding: utf-8 -*-

"""
Strings sql

"""

from manager_database_sqlite3 import factory


def list_tables () -> str :
	"""Retorna sql 'ListTables'"""

	sql = "SELECT name FROM sqlite_master WHERE type = 'table'"

	return sql


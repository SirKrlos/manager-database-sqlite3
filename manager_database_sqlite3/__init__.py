# -*- coding: utf-8 -*-

"""
Gerenciador de Banco de Dados sqlite3

"""

__author__ = "JoseCarlosSkar"
__version__ = "0.1.0-alpha"


import sqlite3


class ManagerDatabase ( object ) :
	"""Gerenciador de Banco de Dados sqlite3"""

	def __init__ (
		self,
		path_db: str = None
	) -> None :
		"""Construtor"""

		self.__path_db = str ( path_db ).strip ()


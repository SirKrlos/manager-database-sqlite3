# -*- coding: utf-8 -*-

"""
Gerenciador de Banco de Dados sqlite3

"""

__author__ = "JoseCarlosSkar"
__version__ = "0.1.0-alpha"


import sqlite3
from . import keys
from . import exceptions


class ManagerDatabase ( object ) :
	"""Gerenciador de Banco de Dados sqlite3"""

	def __init__ (
		self,
		path_db: str = None
	) -> None :
		"""Construtor"""

		if isinstance ( path_db, str ):
			self.__path_db = str ( path_db ).strip ()

		elif path_db == None:
			raise ( exceptions.NotDefinePathDB (
				"O caminho para o banco de dados não foi informado."
			) )

		elif isinstance ( path_db, str ) == False:
			raise ( exceptions.ParamTypeError (
				"O parâmetro 'path_db' deve ser do tipo 'str'."
			) )


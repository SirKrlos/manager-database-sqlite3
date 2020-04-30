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

		self.__connnected = False

		if path_db is not None:
			self.Connect ( path_db = path_db )

	def Connect (
		self,
		path_db: str = None
	) -> None :

		if self.__connnected == True:
			return False

		if isinstance ( path_db, str ):
			self.__path_db = str ( path_db ).strip ()
			try:
				with sqlite3.connect ( self.__path_db ): pass
				return True
			except:
				return False

		elif path_db == None:
			raise ( exceptions.NotDefinePathDB (
				"O caminho para o banco de dados não foi informado."
			) )

		elif isinstance ( path_db, str ) == False:
			raise ( exceptions.ParamTypeError (
				"O parâmetro 'path_db' deve ser do tipo 'str'."
			) )

	def Disconnect (
		self
	) -> None :
		"""Disconectar banco de dados"""

		if self.__connnected == True:
			self.__connnected = False


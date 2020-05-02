# -*- coding: utf-8 -*-

"""
Gerenciador de Banco de Dados sqlite3

"""

__author__ = "JoseCarlosSkar"
__version__ = "0.1.0-alpha"


import sqlite3
from . import keys
from . import exceptions
from . import sqlformat


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
		"""Conectar banco de dados"""

		if self.__connnected == True:
			return False

		if isinstance ( path_db, str ):
			self.__path_db = str ( path_db ).strip ()
			try:
				with sqlite3.connect ( self.__path_db ): pass
				self.__connnected = True
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

	def IsConnected (
		self
	) -> bool :
		"""Verificar se o banco de dados está conectado"""

		if self.__connnected == True:
			return True
		elif self.__connnected == False:
			return False

	def __run (
		self,
		SQL: str = None,
		dicter: bool = False
	) -> None or list or dict :
		"""Executar string sql"""

		result = None

		try:
			with sqlite3.connect ( self.__path_db ) as conn:
				if dicter == True:
					conn.row_factory = lambda c, r: dict ( zip ( [ col [ 0 ] for col in c.description ], r ) )

				cs = conn.cursor ()
				cs.execute ( SQL )
				conn.commit ()
				result = cs.fetchall ()

		except:
			raise ( exceptions.ErrorInSystem (
				"Ocorreu um erro no sistema, por favor informe em 'https://github.com/JoseCarlosSkar/manager-database-sqlite3', se possível com o log."
			) )

		if result == [] and dicter == True:
			return {}
		else:
			return result

	def ListTables (
		self
	) -> list :
		"""Listar todas as tabelas"""

		SQL = sqlformat.list_tables ()

		result = self.__run ( SQL = SQL, dicter = True )
		tables = [ d [ "name" ] for d in result ]

		return tables

	def IsExistTable (
		self,
		name_table: str = None,
	) -> bool :
		"""Verificar se existe tabela"""

		if isinstance ( name_table, str ) == True:
			name_table = str ( name_table ).strip ()

		if name_table in self.ListTables ():
			return True
		else:
			return False


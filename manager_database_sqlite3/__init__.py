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

	def CreateTable (
		self,
		name_table: str = None,
		keysvalues: dict = None,
		ifnoexist: bool = False
	) -> None :
		"""Criar tabela"""

		if isinstance ( name_table, str ) == True:
			name_table = str ( name_table ).strip ()

		isexisttable = self.IsExistTable ( name_table = name_table )

		if ifnoexist == True and isexisttable == True:
			return None

		elif ifnoexist == False and isexisttable == True:
			raise ( exceptions.ErrorOnCreateTable (
				f"Erro ao tentar criar tabela `{name_table}`, pois ja existe esta tabela."
			) )

		else:
			SQL = sqlformat.create_table (
				name_table = name_table,
				keysvalues = keysvalues
			)

			self.__run ( SQL = SQL, dicter = False )

	def DeleteTable (
		self,
		name_table: str = None,
		ifexist: bool = False
	) -> None :
		"""Deletar tabela"""

		if isinstance ( name_table, str ) == True:
			name_table = str ( name_table ).strip ()

		isexisttable = self.IsExistTable ( name_table = name_table )

		if ifexist == True and isexisttable == False:
			return None

		elif ifexist == False and isexisttable == False:
			raise ( exceptions.ErrorOnDeleteTable (
				f"Erro ao tentar deletar tabela `{name_table}`, pois não existe esta tabela."
			) )

		else:
			SQL = sqlformat.delete_table (
				name_table = name_table
			)

			self.__run ( SQL = SQL, dicter = False )

	def RenameTable (
		self,
		name_table: str = None,
		new_name_table: str = None,
		ifexist_origin_table: bool = False,
		ifnoexist_new_table: bool = False
	) -> None :
		"""Renomear Tabela"""

		if isinstance ( name_table, str ) == True:
			name_table = str ( name_table ).strip ()

		if isinstance ( new_name_table, str ) == True:
			new_name_table = str ( new_name_table ).strip ()

		if ifexist_origin_table == True and self.IsExistTable ( name_table = name_table ) == False:
			return None

		if ifnoexist_new_table == True and self.IsExistTable ( name_table = new_name_table ) == True:
			return None

		if ifexist_origin_table == False and self.IsExistTable ( name_table = name_table ) == False:
			raise ( exceptions.ErrorOnRenameTable (
				f"A tabela original `{name_table}` não existe."
			) )

		if ifnoexist_new_table == False and self.IsExistTable ( name_table = new_name_table ) == True:
			raise ( exceptions.ErrorOnRenameTable (
				f"A nova tabela `{new_name_table}` já existe."
			) )

		else:

			SQL = sqlformat.rename_table (
				name_table = name_table,
				new_name_table = new_name_table
			)

			self.__run ( SQL = SQL, dicter = False )

	def GetContentTable (
		self,
		name_table: str = None,
		keysvalues: dict = None,
		dicter: bool = False,
		ifexist: bool = False
	) -> None or list or dict :
		"""Listar conteúdo"""

		if isinstance ( name_table, str ) == True:
			name_table = str ( name_table ).strip ()

		if ifexist == True and self.IsExistTable ( name_table = name_table ) == False:
			return None

		if ifexist == False and self.IsExistTable ( name_table = name_table ) == False:
			raise ( exceptions.ErrorOnGetContentTable (
				f"A tabela `{name_table}` não existe."
			) )

		else:

			SQL = sqlformat.get_content_table (
				name_table = name_table,
				keysvalues = keysvalues
			)

			return self.__run ( SQL = SQL, dicter = dicter )


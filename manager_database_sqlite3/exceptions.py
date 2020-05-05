# -*- coding: utf-8 -*-

"""
Classes para tratamento de erros

"""


class NotDefinePathDB ( Exception ) :

	pass


class ParamTypeError ( Exception ) :

	pass


class ErrorInSystem ( Exception ) :

	pass


class ErrorOnCreateTable ( Exception ) :

	pass


class ErrorOnDeleteTable ( Exception ) :

	pass


class ErrorOnRenameTable ( Exception ) :

	pass


class ErrorOnGetContentTable ( Exception ) :

	pass


class ErrorOnAddContentTable ( Exception ) :

	pass


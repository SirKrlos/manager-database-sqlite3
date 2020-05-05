# -*- coding: utf-8 -*-


def keysvaluesToListStr (
	keysvalues: dict = None,
	sep: str = ","
) -> str :
	"""Keysvalues to list str 'key value, key2 value2'"""

	result = ""

	for k,v in keysvalues.items ():
		if result != "": result += f"{sep}"
		result += str ( f"`{k}`" ) + " " + str ( v )

	return result

def keysvaluesToDictStr (
	keysvalues: dict = None,
	sep: str = ","
) -> str :
	"""Keysvalues to dict str 'key = value, key2 = value2'"""

	result = ""

	for k,v in keysvalues.items ():
		if result != "": result += f"{sep}"
		result += str(k) if type(k) == int else "`"+str(k)+"`"
		result += "="
		result += str(v) if type(v) == int else "'"+str(v)+"'"

	return result

def listToStrSqliteColumn (
	list_columns: list = None,
	sep: str = ","
) -> str :
	"""list_to_str"""

	result = ""
	for i in list_columns:
		if result != "": result += f"{sep}"
		result += f"`{i}`"

	return result


# -*- coding: utf-8 -*-


def keysvaluesToListStr (
	keysvalues: dict = None
) -> str :
	"""Keysvalues to list str 'key value, key2 value2'"""

	result = ""

	for k,v in keysvalues.items ():
		if result != "":
			result += ", "
		result += str ( f"`{k}`" ) + " " + str ( v )

	return result

def keysvaluesToDictStr (
	keysvalues: dict = None,
	sep: str = ","
) -> str :
	"""Keysvalues to dict str 'key = value, key2 = value2'"""

	sets = ""
	for k, v in keysvalues.items():
		if sets != "": sets += f"{sep}"
		sets += str(k) if type(k) == int else "`"+str(k)+"`"
		sets += "="
		sets += str(v) if type(v) == int else "'"+str(v)+"'"

	return sets


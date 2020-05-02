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


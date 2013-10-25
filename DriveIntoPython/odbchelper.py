def buildConnectionString(params):
	"""Build a connection string from a dictionary of parameters.
	Returns string."""
	print ["%s=%s" % (k, v) for k, v in params.items()]
	print ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
	myParams = {"server":"mpilgrim", \
		"database":"master", \
		"uid":"sa", \
		"pwd":"secret" \
		}
buildConnectionString(myParams)

import os

PG_CONNECTION_STRING = 'PG_CONNECTION_STRING'
def checkForRequiredEnvironmentVariables():
    requiredVariables = []
    requiredVariables.append(PG_CONNECTION_STRING)

    for variable in requiredVariables:
        if variable not in os.environ:
            raise Exception("Required variable not defined: " + variable)

def getPgConnectionString():
    return os.environ[PG_CONNECTION_STRING]
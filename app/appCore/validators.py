class StoreDocumentCommandValidator:
    def validate(self, command):

        results = []

        if(command.collection == ''):
            results.append("collection should not be empty")

        if(command.name == ''):
            results.append("name should not be empty")

        if(command.userId == ''):
            results.append("userId should not be empty")

        return results

class GetDocumentsQueryValidator:
    def validate(self, command):

        results = []

        if(command.collection == ''):
            results.append("collection should not be empty")

        if(command.userId == ''):
            results.append("userId should not be empty")

        return results

class GetDocumentQueryValidator:
    def validate(self, command):

        results = []

        if(command.userId == ''):
            results.append("userId should not be empty")

        if(command.id == ''):
            results.append("id should not be empty")


        return results
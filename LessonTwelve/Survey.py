class AnonimSurvey():
    '''Собирает ответы, какой язык хочет учить первым'''

    def __init__(self, question):
        """Содержит вопрос и подготавливает список для ответов"""
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Результаты: ")
        for response in self.responses:
            print(f"-{response}")

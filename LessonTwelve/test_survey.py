import unittest
from Survey import AnonimSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Тест для класса AnonimSurvey"""
    def setUp(self):
        """
        Создать опрос и проверить его методы
        """
        question = "На каком языке вы хотите заговорить"
        self.my_survey = AnonimSurvey(question)
        self.responses = ['Prolog', 'Spanish', "Mandarin"]

    def test_store_single_response(self):
        """Проверяет что одиночный ответ был сохранен правильно"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Проверяет, чтобы каждый отдельный ответ был сохранен правильно """
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()

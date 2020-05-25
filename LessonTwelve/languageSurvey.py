from Survey import AnonimSurvey

question = "Какой язык вы хотите изучать первым? "
my_survey = AnonimSurvey(question)

my_survey.show_question()
print("Enter 'q' for exit \n")
while True:
    response = input('Язык: \n')
    if response == 'q':
        break
    my_survey.store_response(response)
print('Thanks for answer ')


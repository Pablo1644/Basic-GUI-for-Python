import base

questions, anwsers = base.questions, base.anwsers
user_anwsers = []
correct_anwsers = 0
nr_of_question_wrong = []
i = 0
nr = 40  # nr = int(input('Give number of questions:'))
while i < nr:
    print(questions[i])
    anw = input('Your anwser:')
    user_anwsers.append(anw)
    print(f'Correct anwser: {anwsers[i]}')
    if user_anwsers[i] == anwsers[i]:
        correct_anwsers = correct_anwsers + 1
    else:
        nr_of_question_wrong.append((i, user_anwsers[i], 'powinno byc', anwsers[i]))
    i = i + 1

print(f'Twój wynik to:{correct_anwsers} na {nr} możliwych')
print(f'Bledne odpowiedzi to {nr_of_question_wrong}')

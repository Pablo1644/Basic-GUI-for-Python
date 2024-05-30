


# function for creating list with question and list with anwsers
def possible_signs(input_sign):
    signs = ['a', 'b', 'c','d', 'A', 'B', 'C','D']
    if input_sign not in signs:
        return False
    else:
        return True


# In Python > 3.9 just use removesuffix method
def remove_suffix_from_str(input_string, suffix):
    if suffix and input_string.startswith(suffix):
        return input_string[:-len(suffix)]
    return input_string


nr = 10  # number of questions (changed from 40)


def question_anwsers():
    with open(file='anwsers2.txt') as f:
        anw = f.readline().split(',')
    with open(file='questions2.txt', encoding='UTF-8') as f:
        que = []
        temp = ''
        for line in f.readlines():
            if line == '\n':
                que.append(temp)
                # que.append(remove_suffix_from_str(temp,'/n'))
                temp = ''
            temp += line
            if temp == '\n':
                temp = ''
    return que, anw

questions, anwsers = question_anwsers()
user_anwsers = []
correct_anwsers = 0
nr_of_question_wrong = []

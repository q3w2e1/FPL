from skfuzzy import control as ctrl
import numpy as np
import skfuzzy as fuzz

# # mimicking answers of the reader/user
# consultation = {
#     "experience" : (100, 100),
#     "OOP" : (100, 100),
#     "repos" : (90, 100),
#     "multi" : (13, 20),
#     "pointer" : (50, 15),
#     "highlev" : (80, 80)
# }

# alternative consulation (input from keyboard)
consultation = {}
answer = input("Are you searching for a language that does not require as much previous experience? (0-100)\n")
weight = input("How much weight do you want to add to that question and answer? (0-100)\n")
consultation["experience"] = (int(answer), int(weight))
answer = input("Do you need OOP (object oriented programming) support? (0-100)\n")
weight = input("How much weight do you want to add to that question and answer? (0-100)\n")
consultation["OOP"] = (int(answer), int(weight))
answer = input("Do you care about the number of programming repositories that the language has? (0-100)\n")
weight = input("How much weight do you want to add to that question and answer? (0-100)\n")
consultation["repos"] = (int(answer), int(weight))
answer = input("Do you need a language with multithread support? (0-100)\n")
weight = input("How much weight do you want to add to that question and answer? (0-100)\n")
consultation["multi"] = (int(answer), int(weight))
answer = input("Do you want the language to support pointer arithmetic? (0-100)\n")
weight = input("How much weight do you want to add to that question and answer? (0-100)\n")
consultation["pointer"] = (int(answer), int(weight))
answer = input("Is it advantageous for this language to be high level? (0-100)\n")
weight = input("How much weight do you want to add to that question and answer? (0-100)\n")
consultation["highlev"] = (int(answer), int(weight))



# consequents of this system
output_languages = ["C", "C++", "C#", "Fortran", "Java", "Pascal", "Python"]

# creation of consequents
def consequents():
    # creation of membership functions of consequents
    consequents = {}
    for lang in output_languages:
        consequents[lang] = ctrl.Consequent(np.arange(0, 100, 1), lang)

    # create 7 membership functions in each variable
    for key in consequents:
        consequents[key].automf(7)
    return consequents

# creation of antecedents
def antecedents():
    # creation of antecedents - 2 input characteristics (answer_yn, question_care)
    answer_yn = ctrl.Antecedent(np.arange(0, 100, 1), 'answer_yn')
    answer_yn.automf(3, names = ["No", "I do not know", "Yes"])

    question_care = ctrl.Antecedent(np.arange(0, 100, 1), 'question_care')
    question_care['I do care'] = fuzz.trimf(question_care.universe, [45, 100, 100])
    question_care['I do not care'] = fuzz.trimf(question_care.universe, [0, 0, 55])
    return (answer_yn, question_care)


# NOTE tips --- ignore
# mfs_dict["Python"]['average'].view()
# question_care.view()
# answer_yn.view()
# MFs stages of automf 7:
    #  |      * dismal
    #  |      * poor
    #  |      * mediocre
    #  |      * average (always middle)
    #  |      * decent
    #  |      * good
    #  |      * excellent

# print(question_experience_simulation.output)
# print(question_OOP_simulation.output)
# print(question_repos_simulation.output)
# print(question_multi_simulation.output)
# print(question_pointer_simulation.output)
# print(question_highlev_simulation.output)

# consequents["Python"].view(question_repos_simulation)
# consequents["Python"].view(question_OOP_simulation)
# consequents["Python"].view(question_multi_simulation)
# consequents["Python"].view(question_pointer_simulation)
# consequents["Python"].view(question_highlev_simulation)


# question_care.view(question_OOP_simulation)
# answer_yn.view(question_OOP_simulation)

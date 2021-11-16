from skfuzzy import control as ctrl
import numpy as np
import skfuzzy as fuzz

# these are answers of the reader/user
consultation = {
    "experience" : (100, 100),
    "OOP" : (10, 70),
    "repos" : (100, 40),
    "multi" : (70, 80),
    "pointer" : (12, 15),
    "highlev" : (20, 80)
}

# consequents of this system
output_languages = ["c_lang", "cpp_lang", "csharp_lang", "fortran_lang", "java_lang", "pascal_lang", "python_lang"]

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
# mfs_dict["python_lang"]['average'].view()
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

# consequents["python_lang"].view(question_repos_simulation)
# consequents["python_lang"].view(question_OOP_simulation)
# consequents["python_lang"].view(question_multi_simulation)
# consequents["python_lang"].view(question_pointer_simulation)
# consequents["python_lang"].view(question_highlev_simulation)


# question_care.view(question_OOP_simulation)
# answer_yn.view(question_OOP_simulation)

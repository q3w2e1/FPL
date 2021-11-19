from skfuzzy import control as ctrl
import numpy as np
import skfuzzy as fuzz

# creation of consequents
def consequents(output_languages):
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

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pprint

from constants import consultation
from constants import output_languages

from rules_experience import rules_experience
from rules_OOP import rules_OOP
from rules_repos import rules_repos
from rules_multi import rules_multi
from rules_pointer import rules_pointer
from rules_highlev import rules_highlev

def main():
    # creation of membership functions of consequents
    consequents = {}
    for lang in output_languages:
        consequents[lang] = ctrl.Consequent(np.arange(0, 100, 1), lang)

    # create 7 membership functions in each variable
    for key in consequents:
        consequents[key].automf(7)

    # creation of antecedents - 2 input characteristics:
    # 1:   answer_yn (3 mfs) ---------- "No", "I do not know", "Yes"
    # 2:   question_care (2 mfs) ----- 'I do not care', 'I do not care'
    answer_yn = ctrl.Antecedent(np.arange(0, 100, 1), 'answer_yn')
    answer_yn.automf(3, names = ["No", "I do not know", "Yes"])

    question_care = ctrl.Antecedent(np.arange(0, 100, 1), 'question_care')
    question_care['I do care'] = fuzz.trimf(question_care.universe, [45, 100, 100])
    question_care['I do not care'] = fuzz.trimf(question_care.universe, [0, 0, 55])

    question_experience_simulation = rules_experience(answer_yn, question_care, consequents)
    question_OOP_simulation = rules_OOP(answer_yn, question_care, consequents)
    question_repos_simulation = rules_repos(answer_yn, question_care, consequents)
    question_multi_simulation = rules_multi(answer_yn, question_care, consequents)
    question_pointer_simulation = rules_pointer(answer_yn, question_care, consequents)
    question_highlev_simulation = rules_highlev(answer_yn, question_care, consequents)

    final_score = {}
    for lang in output_languages:
        final_score[lang] = question_experience_simulation.output[lang] + question_OOP_simulation.output[lang] + question_repos_simulation.output[lang] + question_multi_simulation.output[lang] + question_pointer_simulation.output[lang] + question_highlev_simulation.output[lang]

    final_score_normalised = {}
    for i in final_score:
        final_score_normalised[i] = final_score[i] / 6

    pprint.pprint(final_score_normalised, width=1)

    input("Press Enter to continue...")

if __name__ == '__main__':
    main()

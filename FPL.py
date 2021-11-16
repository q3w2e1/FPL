import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pprint

import constants

from rules_experience import rules_experience
from rules_OOP import rules_OOP
from rules_repos import rules_repos
from rules_multi import rules_multi
from rules_pointer import rules_pointer
from rules_highlev import rules_highlev

def main():
    # creation of membership functions of consequents (7) and antecedents (2)
    consequents = constants.consequents()
    answer_yn, question_care = constants.antecedents()

    # created simulations for each question and applied consultation answers
    question_experience_simulation = rules_experience(answer_yn, question_care, consequents)
    question_OOP_simulation = rules_OOP(answer_yn, question_care, consequents)
    question_repos_simulation = rules_repos(answer_yn, question_care, consequents)
    question_multi_simulation = rules_multi(answer_yn, question_care, consequents)
    question_pointer_simulation = rules_pointer(answer_yn, question_care, consequents)
    question_highlev_simulation = rules_highlev(answer_yn, question_care, consequents)

    final_score = {}
    for lang in constants.output_languages:
        final_score[lang] = question_experience_simulation.output[lang] \
                            + question_OOP_simulation.output[lang] \
                            + question_repos_simulation.output[lang] \
                            + question_multi_simulation.output[lang] \
                            + question_pointer_simulation.output[lang] \
                            + question_highlev_simulation.output[lang]

    final_score_normalised = {}
    for i in final_score:
        final_score_normalised[i] = final_score[i] / 6

    pprint.pprint(final_score_normalised, width=1)

if __name__ == '__main__':
    main()

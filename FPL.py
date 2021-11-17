import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pprint

from deps import constants_consul

from deps.rules.rules_experience import rules_experience
from deps.rules.rules_OOP import rules_OOP
from deps.rules.rules_repos import rules_repos
from deps.rules.rules_multi import rules_multi
from deps.rules.rules_pointer import rules_pointer
from deps.rules.rules_highlev import rules_highlev

def main():
    # creation of membership functions of consequents (7) and antecedents (2)
    consequents = constants_consul.consequents()
    answer_yn, question_care = constants_consul.antecedents()

    # created simulations for each question and applied consultation answers
    question_experience_simulation = rules_experience(answer_yn, question_care, consequents)
    question_OOP_simulation = rules_OOP(answer_yn, question_care, consequents)
    question_repos_simulation = rules_repos(answer_yn, question_care, consequents)
    question_multi_simulation = rules_multi(answer_yn, question_care, consequents)
    question_pointer_simulation = rules_pointer(answer_yn, question_care, consequents)
    question_highlev_simulation = rules_highlev(answer_yn, question_care, consequents)

    # summing of the results from each question
    final_score = {}
    for lang in constants_consul.output_languages:
        final_score[lang] = question_experience_simulation.output[lang] \
                            + question_OOP_simulation.output[lang] \
                            + question_repos_simulation.output[lang] \
                            + question_multi_simulation.output[lang] \
                            + question_pointer_simulation.output[lang] \
                            + question_highlev_simulation.output[lang]

    # averaging the results into 0-100 boundaries
    # len(constants_consul.consultation) represents number of questions asked
    final_score_normalised = {}
    for i in final_score:
        final_score_normalised[i] = final_score[i] / len(constants_consul.consultation)

    # # print the results of each consequent
    # pprint.pprint(final_score_normalised, width=1)

    # calculation descending order of dictionary by value and storing result in a list
    sorted_score = sorted(final_score_normalised.items(), key=lambda x: x[1], reverse=True)

    print(f"You might consider to start with {sorted_score[0][0]}.")


if __name__ == '__main__':
    main()

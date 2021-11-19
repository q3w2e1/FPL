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

def FPL(consul):
    # consequents of this system
    output_languages = ["C", "C++", "C#", "Fortran", "Java", "Pascal", "Python"]

    # creation of membership functions of consequents (7) and antecedents (2)
    conseqs = constants_consul.consequents(output_languages)
    answer_yn, question_care = constants_consul.antecedents()

    # creation of simulations for each question and application of consultation answers
    question_experience_simulation = rules_experience(answer_yn, question_care, conseqs, consul)
    question_OOP_simulation = rules_OOP(answer_yn, question_care, conseqs, consul)
    question_repos_simulation = rules_repos(answer_yn, question_care, conseqs, consul)
    question_multi_simulation = rules_multi(answer_yn, question_care, conseqs, consul)
    question_pointer_simulation = rules_pointer(answer_yn, question_care, conseqs, consul)
    question_highlev_simulation = rules_highlev(answer_yn, question_care, conseqs, consul)

    # summing of the results from each question
    final_score = {}
    for lang in output_languages:
        final_score[lang] = question_experience_simulation.output[lang] \
                            + question_OOP_simulation.output[lang] \
                            + question_repos_simulation.output[lang] \
                            + question_multi_simulation.output[lang] \
                            + question_pointer_simulation.output[lang] \
                            + question_highlev_simulation.output[lang]

    # averaging the results into 0-100 boundaries
    final_score_normalised = {}
    for i in final_score:
        final_score_normalised[i] = final_score[i] / len(consul)

    # calculation descending order of resulting consequents by value and storing result in a list
    sorted_score = sorted(final_score_normalised.items(), key=lambda x: x[1], reverse=True)
    resulting_highscore = sorted_score[0][0]
    return resulting_highscore


if __name__ == '__main__':
    choice = input("Press 'y' to resume with interactive consultation, or 'n' to generate consultation from pre-prepared script\n")

    if choice == 'y':
        # interactive consulation (input from the keyboard)
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
    else:
        # mimicking answers of the reader/user
        consultation = {
            "experience" : (0, 100),
            "OOP" : (0, 100),
            "repos" : (50, 50),
            "multi" : (50, 50),
            "pointer" : (0, 100),
            "highlev" : (100, 100)
        }

    print(f"You might consider to start with {FPL(consultation)}.")

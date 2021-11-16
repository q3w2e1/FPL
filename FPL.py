import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pprint

from constants import consultation
from constants import output_languages

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

    # Experience question --- "Hľadáte jazyk ktorého učenie nevyžaduje predchádzajúce skúsenosti?"
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["c_lang"]['decent'],
        consequents["cpp_lang"]['decent'],
        consequents["csharp_lang"]['good'],
        consequents["fortran_lang"]['mediocre'],
        consequents["java_lang"]['good'],
        consequents["pascal_lang"]['decent'],
        consequents["python_lang"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["c_lang"]['good'],
        consequents["cpp_lang"]['good'],
        consequents["csharp_lang"]['excellent'],
        consequents["fortran_lang"]['poor'],
        consequents["java_lang"]['excellent'],
        consequents["pascal_lang"]['good'],
        consequents["python_lang"]['dismal']))
    rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
        consequents["c_lang"]['average'],
        consequents["cpp_lang"]['average'],
        consequents["csharp_lang"]['average'],
        consequents["fortran_lang"]['average'],
        consequents["java_lang"]['average'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['average']))
    rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
        consequents["c_lang"]['mediocre'],
        consequents["cpp_lang"]['mediocre'],
        consequents["csharp_lang"]['poor'],
        consequents["fortran_lang"]['decent'],
        consequents["java_lang"]['poor'],
        consequents["pascal_lang"]['mediocre'],
        consequents["python_lang"]['good'],))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["c_lang"]['poor'],
        consequents["cpp_lang"]['poor'],
        consequents["csharp_lang"]['dismal'],
        consequents["fortran_lang"]['good'],
        consequents["java_lang"]['dismal'],
        consequents["pascal_lang"]['poor'],
        consequents["python_lang"]['excellent']))

    ctrl_experience = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_experience_simulation = ctrl.ControlSystemSimulation(ctrl_experience, flush_after_run=100)

    question_experience_simulation.input['answer_yn'] = consultation["experience"][0]
    question_experience_simulation.input['question_care'] = consultation["experience"][1]

    try:
        question_experience_simulation.compute()
        # consequents["python_lang"].view(sim=question_experience_simulation)
    except:
        print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

    # OOP question --- "Hľadáte support OOP?"
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["c_lang"]['good'],
        consequents["cpp_lang"]['poor'],
        consequents["csharp_lang"]['poor'],
        consequents["fortran_lang"]['poor'],
        consequents["java_lang"]['poor'],
        consequents["pascal_lang"]['good'],
        consequents["python_lang"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["c_lang"]['excellent'],
        consequents["cpp_lang"]['dismal'],
        consequents["csharp_lang"]['dismal'],
        consequents["fortran_lang"]['dismal'],
        consequents["java_lang"]['dismal'],
        consequents["pascal_lang"]['excellent'],
        consequents["python_lang"]['dismal']))
    rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
        consequents["c_lang"]['average'],
        consequents["cpp_lang"]['average'],
        consequents["csharp_lang"]['average'],
        consequents["fortran_lang"]['average'],
        consequents["java_lang"]['average'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['average']))
    rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
        consequents["c_lang"]['poor'],
        consequents["cpp_lang"]['good'],
        consequents["csharp_lang"]['good'],
        consequents["fortran_lang"]['good'],
        consequents["java_lang"]['good'],
        consequents["pascal_lang"]['poor'],
        consequents["python_lang"]['good']))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["c_lang"]['dismal'],
        consequents["cpp_lang"]['excellent'],
        consequents["csharp_lang"]['excellent'],
        consequents["fortran_lang"]['excellent'],
        consequents["java_lang"]['excellent'],
        consequents["pascal_lang"]['dismal'],
        consequents["python_lang"]['excellent']))

    ctrl_OOP = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_OOP_simulation = ctrl.ControlSystemSimulation(ctrl_OOP, clip_to_bounds=True, flush_after_run=100)

    question_OOP_simulation.input['answer_yn'] = consultation["OOP"][0]
    question_OOP_simulation.input['question_care'] = consultation["OOP"][1]

    # question_care.view(question_OOP_simulation)
    # answer_yn.view(question_OOP_simulation)

    try:
        question_OOP_simulation.compute()
        # consequents["python_lang"].view(sim=question_OOP_simulation)
    except:
        print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

    # repos question --- "Záleží vám na počte online repozitárov pod záštitom daného jazyka?"
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["c_lang"]['good'],
        consequents["cpp_lang"]['poor'],
        consequents["csharp_lang"]['decent'],
        consequents["fortran_lang"]['good'],
        consequents["java_lang"]['poor'],
        consequents["pascal_lang"]['good'],
        consequents["python_lang"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["c_lang"]['decent'],
        consequents["cpp_lang"]['dismal'],
        consequents["csharp_lang"]['good'],
        consequents["fortran_lang"]['excellent'],
        consequents["java_lang"]['dismal'],
        consequents["pascal_lang"]['excellent'],
        consequents["python_lang"]['mediocre']))
    rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
        consequents["c_lang"]['average'],
        consequents["cpp_lang"]['average'],
        consequents["csharp_lang"]['average'],
        consequents["fortran_lang"]['average'],
        consequents["java_lang"]['average'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['average']))
    rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
        consequents["c_lang"]['poor'],
        consequents["cpp_lang"]['good'],
        consequents["csharp_lang"]['mediocre'],
        consequents["fortran_lang"]['poor'],
        consequents["java_lang"]['good'],
        consequents["pascal_lang"]['poor'],
        consequents["python_lang"]['good']))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["c_lang"]['mediocre'],
        consequents["cpp_lang"]['excellent'],
        consequents["csharp_lang"]['poor'],
        consequents["fortran_lang"]['dismal'],
        consequents["java_lang"]['excellent'],
        consequents["pascal_lang"]['dismal'],
        consequents["python_lang"]['decent']))

    ctrl_repos = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_repos_simulation = ctrl.ControlSystemSimulation(ctrl_repos, clip_to_bounds=True, flush_after_run=100)

    question_repos_simulation.input['answer_yn'] = consultation["repos"][0]
    question_repos_simulation.input['question_care'] = consultation["repos"][1]
    try:
        question_repos_simulation.compute()
        # consequents["python_lang"].view(sim=question_repos_simulation)
    except:
        print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

    # multi question --- "Hľadáte jazyk ktorého učenie nevyžaduje predchádzajúce skúsenosti?"
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["c_lang"]['decent'],
        consequents["cpp_lang"]['decent'],
        consequents["csharp_lang"]['poor'],
        consequents["fortran_lang"]['decent'],
        consequents["java_lang"]['poor'],
        consequents["pascal_lang"]['decent'],
        consequents["python_lang"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["c_lang"]['good'],
        consequents["cpp_lang"]['good'],
        consequents["csharp_lang"]['dismal'],
        consequents["fortran_lang"]['good'],
        consequents["java_lang"]['dismal'],
        consequents["pascal_lang"]['good'],
        consequents["python_lang"]['mediocre']))
    rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
        consequents["c_lang"]['average'],
        consequents["cpp_lang"]['average'],
        consequents["csharp_lang"]['average'],
        consequents["fortran_lang"]['average'],
        consequents["java_lang"]['average'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['average']))
    rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
        consequents["c_lang"]['mediocre'],
        consequents["cpp_lang"]['mediocre'],
        consequents["csharp_lang"]['good'],
        consequents["fortran_lang"]['mediocre'],
        consequents["java_lang"]['good'],
        consequents["pascal_lang"]['mediocre'],
        consequents["python_lang"]['good'],))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["c_lang"]['poor'],
        consequents["cpp_lang"]['poor'],
        consequents["csharp_lang"]['good'],
        consequents["fortran_lang"]['poor'],
        consequents["java_lang"]['good'],
        consequents["pascal_lang"]['poor'],
        consequents["python_lang"]['decent']))

    ctrl_multi = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_multi_simulation = ctrl.ControlSystemSimulation(ctrl_multi, clip_to_bounds=True, flush_after_run=100)

    question_multi_simulation.input['answer_yn'] = consultation["multi"][0]
    question_multi_simulation.input['question_care'] = consultation["multi"][1]
    try:
        question_multi_simulation.compute()
        # consequents["python_lang"].view(sim=question_multi_simulation)
    except:
        print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

    # pointer question --- "Hľadáte jazyk ktorého učenie nevyžaduje predchádzajúce skúsenosti?"
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["c_lang"]['dismal'],
        consequents["cpp_lang"]['dismal'],
        consequents["csharp_lang"]['good'],
        consequents["fortran_lang"]['good'],
        consequents["java_lang"]['good'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['good']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["c_lang"]['dismal'],
        consequents["cpp_lang"]['dismal'],
        consequents["csharp_lang"]['excellent'],
        consequents["fortran_lang"]['poor'],
        consequents["java_lang"]['excellent'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['dismal']))
    rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
        consequents["c_lang"]['average'],
        consequents["cpp_lang"]['average'],
        consequents["csharp_lang"]['average'],
        consequents["fortran_lang"]['average'],
        consequents["java_lang"]['average'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['average']))
    rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
        consequents["c_lang"]['good'],
        consequents["cpp_lang"]['good'],
        consequents["csharp_lang"]['dismal'],
        consequents["fortran_lang"]['dismal'],
        consequents["java_lang"]['dismal'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['dismal'],))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["c_lang"]['poor'],
        consequents["cpp_lang"]['poor'],
        consequents["csharp_lang"]['dismal'],
        consequents["fortran_lang"]['dismal'],
        consequents["java_lang"]['dismal'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['dismal']))

    ctrl_pointer = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_pointer_simulation = ctrl.ControlSystemSimulation(ctrl_pointer, clip_to_bounds=True, flush_after_run=100)

    question_pointer_simulation.input['answer_yn'] = consultation["pointer"][0]
    question_pointer_simulation.input['question_care'] = consultation["pointer"][1]
    try:
        question_pointer_simulation.compute()
        # consequents["python_lang"].view(sim=question_pointer_simulation)
    except:
        print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

    # highlev question --- "Hľadáte jazyk ktorého učenie nevyžaduje predchádzajúce skúsenosti?"
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["c_lang"]['dismal'],
        consequents["cpp_lang"]['mediocre'],
        consequents["csharp_lang"]['mediocre'],
        consequents["fortran_lang"]['good'],
        consequents["java_lang"]['mediocre'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["c_lang"]['decent'],
        consequents["cpp_lang"]['poor'],
        consequents["csharp_lang"]['poor'],
        consequents["fortran_lang"]['mediocre'],
        consequents["java_lang"]['poor'],
        consequents["pascal_lang"]['mediocre'],
        consequents["python_lang"]['dismal']))
    rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
        consequents["c_lang"]['average'],
        consequents["cpp_lang"]['average'],
        consequents["csharp_lang"]['average'],
        consequents["fortran_lang"]['average'],
        consequents["java_lang"]['average'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['average']))
    rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
        consequents["c_lang"]['good'],
        consequents["cpp_lang"]['decent'],
        consequents["csharp_lang"]['decent'],
        consequents["fortran_lang"]['dismal'],
        consequents["java_lang"]['decent'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['good'],))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["c_lang"]['mediocre'],
        consequents["cpp_lang"]['good'],
        consequents["csharp_lang"]['good'],
        consequents["fortran_lang"]['decent'],
        consequents["java_lang"]['good'],
        consequents["pascal_lang"]['decent'],
        consequents["python_lang"]['excellent']))

    ctrl_highlev = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_highlev_simulation = ctrl.ControlSystemSimulation(ctrl_highlev, clip_to_bounds=True, flush_after_run=100)

    question_highlev_simulation.input['answer_yn'] = consultation["highlev"][0]
    question_highlev_simulation.input['question_care'] = consultation["highlev"][1]
    try:
        question_highlev_simulation.compute()
        # consequents["python_lang"].view(sim=question_highlev_simulation)
    except:
        print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

    # print(question_experience_simulation.output)
    # print(question_OOP_simulation.output)
    # print(question_repos_simulation.output)
    # print(question_multi_simulation.output)
    # print(question_pointer_simulation.output)
    # print(question_highlev_simulation.output)

    final_score = {}

    for lang in output_languages:
        final_score[lang] = question_experience_simulation.output[lang] + question_OOP_simulation.output[lang] + question_repos_simulation.output[lang] + question_multi_simulation.output[lang] + question_pointer_simulation.output[lang] + question_highlev_simulation.output[lang]

    final_score_normalised = {}
    for i in final_score:
        final_score_normalised[i] = final_score[i] / 6

    # consequents["python_lang"].view(question_repos_simulation)
    # consequents["python_lang"].view(question_OOP_simulation)
    # consequents["python_lang"].view(question_multi_simulation)
    # consequents["python_lang"].view(question_pointer_simulation)
    # consequents["python_lang"].view(question_highlev_simulation)

    pprint.pprint(final_score_normalised, width=1)

    input("Press Enter to continue...")

if __name__ == '__main__':
    main()

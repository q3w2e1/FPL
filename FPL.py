konzultace = {
    "experience" : (100, 100),
    "OOP" : (10, 70),
    "repos" : (100, 40),
    "multi" : (70, 80),
    "pointer" : (12, 15),
    "highlev" : (20, 80)
}
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import copy
import pprint

output_languages = ["c_lang", "cpp_lang", "csharp_lang", "fortran_lang", "java_lang", "pascal_lang", "python_lang"]

c_lang = ctrl.Consequent(np.arange(0, 100, 1), 'c_lang')
c_lang.automf(7)
cpp_lang = ctrl.Consequent(np.arange(0, 100, 1), 'cpp_lang')
cpp_lang.automf(7)
csharp_lang = ctrl.Consequent(np.arange(0, 100, 1), 'csharp_lang')
csharp_lang.automf(7)
fortran_lang = ctrl.Consequent(np.arange(0, 100, 1), 'fortran_lang')
fortran_lang.automf(7)
java_lang = ctrl.Consequent(np.arange(0, 100, 1), 'java_lang')
java_lang.automf(7)
pascal_lang = ctrl.Consequent(np.arange(0, 100, 1), 'pascal_lang')
pascal_lang.automf(7)
python_lang = ctrl.Consequent(np.arange(0, 100, 1), 'python_lang')
python_lang.automf(7)

# python_lang['average'].view()

question_care = ctrl.Antecedent(np.arange(0, 100, 1), 'question_care')
answer_yn = ctrl.Antecedent(np.arange(0, 100, 1), 'answer_yn')

question_care['I do care'] = fuzz.trimf(question_care.universe, [45, 100, 100])
question_care['I do not care'] = fuzz.trimf(question_care.universe, [0, 0, 55])

answer_yn.automf(3, names = ["No", "I do not know", "Yes"])

# question_care.view()
# answer_yn.view()

question_care['I do care']
question_care['I do not care']
answer_yn['No']
answer_yn['I do not know']
answer_yn['Yes']

# ["c_lang", "cpp_lang", "csharp_lang", "fortran_lang", "java_lang", "pascal_lang", "python_lang"]
#  |      * dismal
#  |      * poor
#  |      * mediocre
#  |      * average (always middle)
#  |      * decent
#  |      * good
#  |      * excellent

# Experience question --- "Hľadáte jazyk ktorého učenie nevyžaduje predchádzajúce skúsenosti?"
rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
    c_lang['decent'],
    cpp_lang['decent'],
    csharp_lang['good'],
    fortran_lang['mediocre'],
    java_lang['good'],
    pascal_lang['decent'],
    python_lang['poor']))
rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
    c_lang['good'],
    cpp_lang['good'],
    csharp_lang['excellent'],
    fortran_lang['poor'],
    java_lang['excellent'],
    pascal_lang['good'],
    python_lang['dismal']))
rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
    c_lang['average'],
    cpp_lang['average'],
    csharp_lang['average'],
    fortran_lang['average'],
    java_lang['average'],
    pascal_lang['average'],
    python_lang['average']))
rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
    c_lang['mediocre'],
    cpp_lang['mediocre'],
    csharp_lang['poor'],
    fortran_lang['decent'],
    java_lang['poor'],
    pascal_lang['mediocre'],
    python_lang['good'],))
rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
    c_lang['poor'],
    cpp_lang['poor'],
    csharp_lang['dismal'],
    fortran_lang['good'],
    java_lang['dismal'],
    pascal_lang['poor'],
    python_lang['excellent']))

ctrl_experience = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
question_experience_simulation = ctrl.ControlSystemSimulation(ctrl_experience, flush_after_run=100)

question_experience_simulation.input['answer_yn'] = konzultace["experience"][0]
question_experience_simulation.input['question_care'] = konzultace["experience"][1]

try:
    question_experience_simulation.compute()
    # python_lang.view(sim=question_experience_simulation)
except:
    print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

# OOP question --- "Hľadáte support OOP?"
rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
    c_lang['good'],
    cpp_lang['poor'],
    csharp_lang['poor'],
    fortran_lang['poor'],
    java_lang['poor'],
    pascal_lang['good'],
    python_lang['poor']))
rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
    c_lang['excellent'],
    cpp_lang['dismal'],
    csharp_lang['dismal'],
    fortran_lang['dismal'],
    java_lang['dismal'],
    pascal_lang['excellent'],
    python_lang['dismal']))
rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
    c_lang['average'],
    cpp_lang['average'],
    csharp_lang['average'],
    fortran_lang['average'],
    java_lang['average'],
    pascal_lang['average'],
    python_lang['average']))
rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
    c_lang['poor'],
    cpp_lang['good'],
    csharp_lang['good'],
    fortran_lang['good'],
    java_lang['good'],
    pascal_lang['poor'],
    python_lang['good']))
rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
    c_lang['dismal'],
    cpp_lang['excellent'],
    csharp_lang['excellent'],
    fortran_lang['excellent'],
    java_lang['excellent'],
    pascal_lang['dismal'],
    python_lang['excellent']))

ctrl_OOP = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
question_OOP_simulation = ctrl.ControlSystemSimulation(ctrl_OOP, clip_to_bounds=True, flush_after_run=100)

question_OOP_simulation.input['answer_yn'] = konzultace["OOP"][0]
question_OOP_simulation.input['question_care'] = konzultace["OOP"][1]

# question_care.view(question_OOP_simulation)
# answer_yn.view(question_OOP_simulation)

try:
    question_OOP_simulation.compute()
    # python_lang.view(sim=question_OOP_simulation)
except:
    print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

# repos question --- "Záleží vám na počte online repozitárov pod záštitom daného jazyka?"
rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
    c_lang['good'],
    cpp_lang['poor'],
    csharp_lang['decent'],
    fortran_lang['good'],
    java_lang['poor'],
    pascal_lang['good'],
    python_lang['poor']))
rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
    c_lang['decent'],
    cpp_lang['dismal'],
    csharp_lang['good'],
    fortran_lang['excellent'],
    java_lang['dismal'],
    pascal_lang['excellent'],
    python_lang['mediocre']))
rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
    c_lang['average'],
    cpp_lang['average'],
    csharp_lang['average'],
    fortran_lang['average'],
    java_lang['average'],
    pascal_lang['average'],
    python_lang['average']))
rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
    c_lang['poor'],
    cpp_lang['good'],
    csharp_lang['mediocre'],
    fortran_lang['poor'],
    java_lang['good'],
    pascal_lang['poor'],
    python_lang['good']))
rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
    c_lang['mediocre'],
    cpp_lang['excellent'],
    csharp_lang['poor'],
    fortran_lang['dismal'],
    java_lang['excellent'],
    pascal_lang['dismal'],
    python_lang['decent']))

ctrl_repos = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
question_repos_simulation = ctrl.ControlSystemSimulation(ctrl_repos, clip_to_bounds=True, flush_after_run=100)

question_repos_simulation.input['answer_yn'] = konzultace["repos"][0]
question_repos_simulation.input['question_care'] = konzultace["repos"][1]
try:
    question_repos_simulation.compute()
    # python_lang.view(sim=question_repos_simulation)
except:
    print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

# multi question --- "Hľadáte jazyk ktorého učenie nevyžaduje predchádzajúce skúsenosti?"
rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
    c_lang['decent'],
    cpp_lang['decent'],
    csharp_lang['poor'],
    fortran_lang['decent'],
    java_lang['poor'],
    pascal_lang['decent'],
    python_lang['poor']))
rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
    c_lang['good'],
    cpp_lang['good'],
    csharp_lang['dismal'],
    fortran_lang['good'],
    java_lang['dismal'],
    pascal_lang['good'],
    python_lang['mediocre']))
rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
    c_lang['average'],
    cpp_lang['average'],
    csharp_lang['average'],
    fortran_lang['average'],
    java_lang['average'],
    pascal_lang['average'],
    python_lang['average']))
rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
    c_lang['mediocre'],
    cpp_lang['mediocre'],
    csharp_lang['good'],
    fortran_lang['mediocre'],
    java_lang['good'],
    pascal_lang['mediocre'],
    python_lang['good'],))
rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
    c_lang['poor'],
    cpp_lang['poor'],
    csharp_lang['good'],
    fortran_lang['poor'],
    java_lang['good'],
    pascal_lang['poor'],
    python_lang['decent']))

ctrl_multi = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
question_multi_simulation = ctrl.ControlSystemSimulation(ctrl_multi, clip_to_bounds=True, flush_after_run=100)

question_multi_simulation.input['answer_yn'] = konzultace["multi"][0]
question_multi_simulation.input['question_care'] = konzultace["multi"][1]
try:
    question_multi_simulation.compute()
    # python_lang.view(sim=question_multi_simulation)
except:
    print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

# pointer question --- "Hľadáte jazyk ktorého učenie nevyžaduje predchádzajúce skúsenosti?"
rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
    c_lang['dismal'],
    cpp_lang['dismal'],
    csharp_lang['good'],
    fortran_lang['good'],
    java_lang['good'],
    pascal_lang['average'],
    python_lang['good']))
rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
    c_lang['dismal'],
    cpp_lang['dismal'],
    csharp_lang['excellent'],
    fortran_lang['poor'],
    java_lang['excellent'],
    pascal_lang['average'],
    python_lang['dismal']))
rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
    c_lang['average'],
    cpp_lang['average'],
    csharp_lang['average'],
    fortran_lang['average'],
    java_lang['average'],
    pascal_lang['average'],
    python_lang['average']))
rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
    c_lang['good'],
    cpp_lang['good'],
    csharp_lang['dismal'],
    fortran_lang['dismal'],
    java_lang['dismal'],
    pascal_lang['average'],
    python_lang['dismal'],))
rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
    c_lang['poor'],
    cpp_lang['poor'],
    csharp_lang['dismal'],
    fortran_lang['dismal'],
    java_lang['dismal'],
    pascal_lang['average'],
    python_lang['dismal']))

ctrl_pointer = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
question_pointer_simulation = ctrl.ControlSystemSimulation(ctrl_pointer, clip_to_bounds=True, flush_after_run=100)

question_pointer_simulation.input['answer_yn'] = konzultace["pointer"][0]
question_pointer_simulation.input['question_care'] = konzultace["pointer"][1]
try:
    question_pointer_simulation.compute()
    # python_lang.view(sim=question_pointer_simulation)
except:
    print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

# highlev question --- "Hľadáte jazyk ktorého učenie nevyžaduje predchádzajúce skúsenosti?"
rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
    c_lang['dismal'],
    cpp_lang['mediocre'],
    csharp_lang['mediocre'],
    fortran_lang['good'],
    java_lang['mediocre'],
    pascal_lang['average'],
    python_lang['poor']))
rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
    c_lang['decent'],
    cpp_lang['poor'],
    csharp_lang['poor'],
    fortran_lang['mediocre'],
    java_lang['poor'],
    pascal_lang['mediocre'],
    python_lang['dismal']))
rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
    c_lang['average'],
    cpp_lang['average'],
    csharp_lang['average'],
    fortran_lang['average'],
    java_lang['average'],
    pascal_lang['average'],
    python_lang['average']))
rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
    c_lang['good'],
    cpp_lang['decent'],
    csharp_lang['decent'],
    fortran_lang['dismal'],
    java_lang['decent'],
    pascal_lang['average'],
    python_lang['good'],))
rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
    c_lang['mediocre'],
    cpp_lang['good'],
    csharp_lang['good'],
    fortran_lang['decent'],
    java_lang['good'],
    pascal_lang['decent'],
    python_lang['excellent']))

ctrl_highlev = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
question_highlev_simulation = ctrl.ControlSystemSimulation(ctrl_highlev, clip_to_bounds=True, flush_after_run=100)

question_highlev_simulation.input['answer_yn'] = konzultace["highlev"][0]
question_highlev_simulation.input['question_care'] = konzultace["highlev"][1]
try:
    question_highlev_simulation.compute()
    # python_lang.view(sim=question_highlev_simulation)
except:
    print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

# print(question_experience_simulation.output)
# print(question_OOP_simulation.output)
# print(question_repos_simulation.output)
# print(question_multi_simulation.output)
# print(question_pointer_simulation.output)
# print(question_highlev_simulation.output)

output_languages = ["c_lang", "cpp_lang", "csharp_lang", "fortran_lang", "java_lang", "pascal_lang", "python_lang"]
final_score = {}

for lang in output_languages:
    final_score[lang] = question_experience_simulation.output[lang] + question_OOP_simulation.output[lang] + question_repos_simulation.output[lang] + question_multi_simulation.output[lang] + question_pointer_simulation.output[lang] + question_highlev_simulation.output[lang]

final_score_normalised = {}
for i in final_score:
    final_score_normalised[i] = final_score[i] / 6

# python_lang.view(question_repos_simulation)
# python_lang.view(question_OOP_simulation)
# python_lang.view(question_multi_simulation)
# python_lang.view(question_pointer_simulation)
# python_lang.view(question_highlev_simulation)

pprint.pprint(final_score_normalised, width=1)

input("Press Enter to continue...")

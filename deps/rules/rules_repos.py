from skfuzzy import control as ctrl
from deps.constants import consultation

def rules_repos(answer_yn, question_care, consequents):
    # repos question --- "Záleží vám na počte online repozitárov pod záštitom daného jazyka?"
    # Do you care about the number of programming repositories that the language has? 
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

    return question_repos_simulation

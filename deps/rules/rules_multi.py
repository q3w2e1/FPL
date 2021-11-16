from skfuzzy import control as ctrl
from deps.constants import consultation

def rules_multi(answer_yn, question_care, consequents):
    # multi question --- "Hľadáte jazyk s Multithread možnosťami? "
    # Do you need a language with multithread support?
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

    return question_multi_simulation

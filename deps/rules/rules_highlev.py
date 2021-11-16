from skfuzzy import control as ctrl
from deps.constants import consultation

def rules_highlev(answer_yn, question_care, consequents):
    # highlev question --- "Je pre vás výhodou viac high level jazyk? "
    # Is it advantageous for this language to be high level?
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

    return question_highlev_simulation

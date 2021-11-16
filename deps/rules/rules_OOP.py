from skfuzzy import control as ctrl
from deps.constants_consul import consultation

def rules_OOP(answer_yn, question_care, consequents):
    # OOP question --- "Hľadáte support OOP?"
    # Do you need OOP (object oriented programming) support?
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["C-language"]['good'],
        consequents["cpp_lang"]['poor'],
        consequents["csharp_lang"]['poor'],
        consequents["fortran_lang"]['poor'],
        consequents["java_lang"]['poor'],
        consequents["pascal_lang"]['good'],
        consequents["python_lang"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["C-language"]['excellent'],
        consequents["cpp_lang"]['dismal'],
        consequents["csharp_lang"]['dismal'],
        consequents["fortran_lang"]['dismal'],
        consequents["java_lang"]['dismal'],
        consequents["pascal_lang"]['excellent'],
        consequents["python_lang"]['dismal']))
    rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
        consequents["C-language"]['average'],
        consequents["cpp_lang"]['average'],
        consequents["csharp_lang"]['average'],
        consequents["fortran_lang"]['average'],
        consequents["java_lang"]['average'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['average']))
    rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
        consequents["C-language"]['poor'],
        consequents["cpp_lang"]['good'],
        consequents["csharp_lang"]['good'],
        consequents["fortran_lang"]['good'],
        consequents["java_lang"]['good'],
        consequents["pascal_lang"]['poor'],
        consequents["python_lang"]['good']))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["C-language"]['dismal'],
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

    try:
        question_OOP_simulation.compute()
        # consequents["python_lang"].view(sim=question_OOP_simulation)
    except:
        print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

    return question_OOP_simulation

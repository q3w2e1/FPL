from skfuzzy import control as ctrl
from deps.constants_consul import consultation

def rules_pointer(answer_yn, question_care, consequents):
    # pointer question --- "Hľadáte podporu pointerovej aritmetiky?"
    # Do you want the language to support pointer Arithmetic?
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["C-language"]['dismal'],
        consequents["cpp_lang"]['dismal'],
        consequents["csharp_lang"]['good'],
        consequents["fortran_lang"]['good'],
        consequents["java_lang"]['good'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['good']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["C-language"]['dismal'],
        consequents["cpp_lang"]['dismal'],
        consequents["csharp_lang"]['excellent'],
        consequents["fortran_lang"]['poor'],
        consequents["java_lang"]['excellent'],
        consequents["pascal_lang"]['average'],
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
        consequents["C-language"]['good'],
        consequents["cpp_lang"]['good'],
        consequents["csharp_lang"]['dismal'],
        consequents["fortran_lang"]['dismal'],
        consequents["java_lang"]['dismal'],
        consequents["pascal_lang"]['average'],
        consequents["python_lang"]['dismal'],))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["C-language"]['poor'],
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

    return question_pointer_simulation

from skfuzzy import control as ctrl
from deps.constants_consul import consultation

def rules_pointer(answer_yn, question_care, consequents):
    # pointer question --- "Hľadáte podporu pointerovej aritmetiky?"
    # Do you want the language to support pointer Arithmetic?
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["C"]['dismal'],
        consequents["C++"]['dismal'],
        consequents["C#"]['good'],
        consequents["Fortran"]['good'],
        consequents["Java"]['good'],
        consequents["Pascal"]['average'],
        consequents["Python"]['good']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["C"]['dismal'],
        consequents["C++"]['dismal'],
        consequents["C#"]['excellent'],
        consequents["Fortran"]['poor'],
        consequents["Java"]['excellent'],
        consequents["Pascal"]['average'],
        consequents["Python"]['dismal']))
    rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
        consequents["C"]['average'],
        consequents["C++"]['average'],
        consequents["C#"]['average'],
        consequents["Fortran"]['average'],
        consequents["Java"]['average'],
        consequents["Pascal"]['average'],
        consequents["Python"]['average']))
    rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
        consequents["C"]['good'],
        consequents["C++"]['good'],
        consequents["C#"]['dismal'],
        consequents["Fortran"]['dismal'],
        consequents["Java"]['dismal'],
        consequents["Pascal"]['average'],
        consequents["Python"]['dismal'],))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["C"]['poor'],
        consequents["C++"]['poor'],
        consequents["C#"]['dismal'],
        consequents["Fortran"]['dismal'],
        consequents["Java"]['dismal'],
        consequents["Pascal"]['average'],
        consequents["Python"]['dismal']))

    ctrl_pointer = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_pointer_simulation = ctrl.ControlSystemSimulation(ctrl_pointer, clip_to_bounds=True, flush_after_run=100)

    question_pointer_simulation.input['answer_yn'] = consultation["pointer"][0]
    question_pointer_simulation.input['question_care'] = consultation["pointer"][1]
    try:
        question_pointer_simulation.compute()
        # consequents["Python"].view(sim=question_pointer_simulation)
    except:
        print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

    return question_pointer_simulation

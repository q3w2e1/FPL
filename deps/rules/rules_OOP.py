from skfuzzy import control as ctrl

def rules_OOP(answer_yn, question_care, consequents, consultation):
    # OOP question --- "Hľadáte support OOP?"
    # Do you need OOP (object oriented programming) support?
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["C"]['good'],
        consequents["C++"]['poor'],
        consequents["C#"]['poor'],
        consequents["Fortran"]['poor'],
        consequents["Java"]['poor'],
        consequents["Pascal"]['good'],
        consequents["Python"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["C"]['excellent'],
        consequents["C++"]['dismal'],
        consequents["C#"]['dismal'],
        consequents["Fortran"]['dismal'],
        consequents["Java"]['dismal'],
        consequents["Pascal"]['excellent'],
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
        consequents["C"]['poor'],
        consequents["C++"]['good'],
        consequents["C#"]['good'],
        consequents["Fortran"]['good'],
        consequents["Java"]['good'],
        consequents["Pascal"]['poor'],
        consequents["Python"]['good']))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["C"]['dismal'],
        consequents["C++"]['excellent'],
        consequents["C#"]['excellent'],
        consequents["Fortran"]['excellent'],
        consequents["Java"]['excellent'],
        consequents["Pascal"]['dismal'],
        consequents["Python"]['excellent']))

    ctrl_OOP = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_OOP_simulation = ctrl.ControlSystemSimulation(ctrl_OOP, clip_to_bounds=True, flush_after_run=100)

    question_OOP_simulation.input['answer_yn'] = consultation["OOP"][0]
    question_OOP_simulation.input['question_care'] = consultation["OOP"][1]

    try:
        question_OOP_simulation.compute()
        # consequents["Python"].view(sim=question_OOP_simulation)
    except:
        print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

    return question_OOP_simulation

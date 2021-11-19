from skfuzzy import control as ctrl

def rules_multi(answer_yn, question_care, consequents, consultation):
    """ multi question ---
    Hľadáte jazyk s Multithread možnosťami?
    Do you need a language with multithread support?
    """
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["C"]['decent'],
        consequents["C++"]['decent'],
        consequents["C#"]['poor'],
        consequents["Fortran"]['decent'],
        consequents["Java"]['poor'],
        consequents["Pascal"]['decent'],
        consequents["Python"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["C"]['good'],
        consequents["C++"]['good'],
        consequents["C#"]['dismal'],
        consequents["Fortran"]['good'],
        consequents["Java"]['dismal'],
        consequents["Pascal"]['good'],
        consequents["Python"]['mediocre']))
    rule3 = ctrl.Rule(answer_yn['I do not know'] & question_care['I do care'], (
        consequents["C"]['average'],
        consequents["C++"]['average'],
        consequents["C#"]['average'],
        consequents["Fortran"]['average'],
        consequents["Java"]['average'],
        consequents["Pascal"]['average'],
        consequents["Python"]['average']))
    rule4 = ctrl.Rule(answer_yn['Yes'] & question_care['I do not care'], (
        consequents["C"]['mediocre'],
        consequents["C++"]['mediocre'],
        consequents["C#"]['good'],
        consequents["Fortran"]['mediocre'],
        consequents["Java"]['good'],
        consequents["Pascal"]['mediocre'],
        consequents["Python"]['good'],))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["C"]['poor'],
        consequents["C++"]['poor'],
        consequents["C#"]['good'],
        consequents["Fortran"]['poor'],
        consequents["Java"]['good'],
        consequents["Pascal"]['poor'],
        consequents["Python"]['decent']))

    ctrl_multi = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_multi_simulation = ctrl.ControlSystemSimulation(ctrl_multi, clip_to_bounds=True, flush_after_run=100)

    question_multi_simulation.input['answer_yn'] = consultation["multi"][0]
    question_multi_simulation.input['question_care'] = consultation["multi"][1]
    
    try:
        question_multi_simulation.compute()
    except:
        print("The system could not properly decide due to insufficient input decision data. In other words, you probably decided to answer 'I do not know', to everything.")

    return question_multi_simulation

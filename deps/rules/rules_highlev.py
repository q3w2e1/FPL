from skfuzzy import control as ctrl

def rules_highlev(answer_yn, question_care, consequents, consultation):
    """ highlev question ---
    Je pre vás výhodou viac high level jazyk?
    Is it advantageous for this language to be high level?
    """
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["C"]['dismal'],
        consequents["C++"]['mediocre'],
        consequents["C#"]['mediocre'],
        consequents["Fortran"]['good'],
        consequents["Java"]['mediocre'],
        consequents["Pascal"]['average'],
        consequents["Python"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["C"]['decent'],
        consequents["C++"]['poor'],
        consequents["C#"]['poor'],
        consequents["Fortran"]['mediocre'],
        consequents["Java"]['poor'],
        consequents["Pascal"]['mediocre'],
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
        consequents["C++"]['decent'],
        consequents["C#"]['decent'],
        consequents["Fortran"]['dismal'],
        consequents["Java"]['decent'],
        consequents["Pascal"]['average'],
        consequents["Python"]['good'],))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["C"]['mediocre'],
        consequents["C++"]['good'],
        consequents["C#"]['good'],
        consequents["Fortran"]['decent'],
        consequents["Java"]['good'],
        consequents["Pascal"]['decent'],
        consequents["Python"]['excellent']))

    ctrl_highlev = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_highlev_simulation = ctrl.ControlSystemSimulation(ctrl_highlev, clip_to_bounds=True, flush_after_run=100)

    question_highlev_simulation.input['answer_yn'] = consultation["highlev"][0]
    question_highlev_simulation.input['question_care'] = consultation["highlev"][1]
    
    try:
        question_highlev_simulation.compute()
    except:
        print("The system could not properly decide due to insufficient input decision data. In other words, you probably decided to answer 'I do not know', to everything.")

    return question_highlev_simulation

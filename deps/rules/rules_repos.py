from skfuzzy import control as ctrl

def rules_repos(answer_yn, question_care, consequents, consultation):
    # repos question --- "Záleží vám na počte online repozitárov pod záštitom daného jazyka?"
    # Do you care about the number of programming repositories that the language has?
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["C"]['good'],
        consequents["C++"]['poor'],
        consequents["C#"]['decent'],
        consequents["Fortran"]['good'],
        consequents["Java"]['poor'],
        consequents["Pascal"]['good'],
        consequents["Python"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["C"]['decent'],
        consequents["C++"]['dismal'],
        consequents["C#"]['good'],
        consequents["Fortran"]['excellent'],
        consequents["Java"]['dismal'],
        consequents["Pascal"]['excellent'],
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
        consequents["C"]['poor'],
        consequents["C++"]['good'],
        consequents["C#"]['mediocre'],
        consequents["Fortran"]['poor'],
        consequents["Java"]['good'],
        consequents["Pascal"]['poor'],
        consequents["Python"]['good']))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["C"]['mediocre'],
        consequents["C++"]['excellent'],
        consequents["C#"]['poor'],
        consequents["Fortran"]['dismal'],
        consequents["Java"]['excellent'],
        consequents["Pascal"]['dismal'],
        consequents["Python"]['decent']))

    ctrl_repos = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_repos_simulation = ctrl.ControlSystemSimulation(ctrl_repos, clip_to_bounds=True, flush_after_run=100)

    question_repos_simulation.input['answer_yn'] = consultation["repos"][0]
    question_repos_simulation.input['question_care'] = consultation["repos"][1]

    try:
        question_repos_simulation.compute()
        # consequents["Python"].view(sim=question_repos_simulation)
    except:
        print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

    return question_repos_simulation

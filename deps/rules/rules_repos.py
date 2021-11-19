from skfuzzy import control as ctrl
from ..constants_consul import simulation_by_question

def rules_repos(answer_yn, question_care, consequents, consultation):
    """ repos question ---
    Záleží vám na počte online repozitárov pod záštitom daného jazyka?
    Do you care about the number of programming repositories that the language has?
    """
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

    rules_list = [rule1, rule2, rule3, rule4, rule5]
    sim = simulation_by_question(rules_list, "repos", consultation)
    return sim

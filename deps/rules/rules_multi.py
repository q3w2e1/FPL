from skfuzzy import control as ctrl
from ..constants_consul import simulation_by_question

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

    rules_list = [rule1, rule2, rule3, rule4, rule5]
    sim = simulation_by_question(rules_list, "multi", consultation)
    return sim

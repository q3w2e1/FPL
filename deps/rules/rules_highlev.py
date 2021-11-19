from skfuzzy import control as ctrl
from ..constants_consul import simulation_by_question

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

    rules_list = [rule1, rule2, rule3, rule4, rule5]
    sim = simulation_by_question(rules_list, "highlev", consultation)
    return sim

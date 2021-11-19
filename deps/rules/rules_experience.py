from skfuzzy import control as ctrl
from ..constants_consul import simulation_by_question

def rules_experience(answer_yn, question_care, consequents, consultation):
    """ experience question ---
    Hľadáte jazyk ktorého učenie nevyžaduje predchádzajúce skúsenosti?
    Are you searching for a language that does not require as much previous experience?
    """
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["C"]['decent'],
        consequents["C++"]['decent'],
        consequents["C#"]['good'],
        consequents["Fortran"]['mediocre'],
        consequents["Java"]['good'],
        consequents["Pascal"]['decent'],
        consequents["Python"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["C"]['good'],
        consequents["C++"]['good'],
        consequents["C#"]['excellent'],
        consequents["Fortran"]['poor'],
        consequents["Java"]['excellent'],
        consequents["Pascal"]['good'],
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
        consequents["C"]['mediocre'],
        consequents["C++"]['mediocre'],
        consequents["C#"]['poor'],
        consequents["Fortran"]['decent'],
        consequents["Java"]['poor'],
        consequents["Pascal"]['mediocre'],
        consequents["Python"]['good'],))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["C"]['poor'],
        consequents["C++"]['poor'],
        consequents["C#"]['dismal'],
        consequents["Fortran"]['good'],
        consequents["Java"]['dismal'],
        consequents["Pascal"]['poor'],
        consequents["Python"]['excellent']))
        
    rules_list = [rule1, rule2, rule3, rule4, rule5]
    sim = simulation_by_question(rules_list, "experience", consultation)
    return sim

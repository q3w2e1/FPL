from skfuzzy import control as ctrl
from deps.constants_consul import consultation # as consultation

def rules_experience(answer_yn, question_care, consequents):
    # Experience question --- "Hľadáte jazyk ktorého učenie nevyžaduje predchádzajúce skúsenosti?"
    # Searching for a language that does not require as much previous experience?
    rule1 = ctrl.Rule(answer_yn['No'] & question_care['I do not care'], (
        consequents["C-language"]['decent'],
        consequents["cpp_lang"]['decent'],
        consequents["csharp_lang"]['good'],
        consequents["fortran_lang"]['mediocre'],
        consequents["java_lang"]['good'],
        consequents["pascal_lang"]['decent'],
        consequents["python_lang"]['poor']))
    rule2 = ctrl.Rule(answer_yn['No'] & question_care['I do care'], (
        consequents["C-language"]['good'],
        consequents["cpp_lang"]['good'],
        consequents["csharp_lang"]['excellent'],
        consequents["fortran_lang"]['poor'],
        consequents["java_lang"]['excellent'],
        consequents["pascal_lang"]['good'],
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
        consequents["C-language"]['mediocre'],
        consequents["cpp_lang"]['mediocre'],
        consequents["csharp_lang"]['poor'],
        consequents["fortran_lang"]['decent'],
        consequents["java_lang"]['poor'],
        consequents["pascal_lang"]['mediocre'],
        consequents["python_lang"]['good'],))
    rule5 = ctrl.Rule(answer_yn['Yes'] & question_care['I do care'], (
        consequents["C-language"]['poor'],
        consequents["cpp_lang"]['poor'],
        consequents["csharp_lang"]['dismal'],
        consequents["fortran_lang"]['good'],
        consequents["java_lang"]['dismal'],
        consequents["pascal_lang"]['poor'],
        consequents["python_lang"]['excellent']))

    ctrl_experience = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    question_experience_simulation = ctrl.ControlSystemSimulation(ctrl_experience, flush_after_run=100)

    question_experience_simulation.input['answer_yn'] = consultation["experience"][0]
    question_experience_simulation.input['question_care'] = consultation["experience"][1]

    try:
        question_experience_simulation.compute()
        # consequents["python_lang"].view(sim=question_experience_simulation)
    except:
        print("The system could not propely decide due to insufficient input decision data. In other words, you decided to answer 'I do not know', to everything.")

    return question_experience_simulation

consultation = {
    "experience" : (100, 100),
    "OOP" : (10, 70),
    "repos" : (100, 40),
    "multi" : (70, 80),
    "pointer" : (12, 15),
    "highlev" : (20, 80)
}

output_languages = ["c_lang", "cpp_lang", "csharp_lang", "fortran_lang", "java_lang", "pascal_lang", "python_lang"]

# NOTE tips
# mfs_dict["python_lang"]['average'].view()
# question_care.view()
# answer_yn.view()
# MFs stages of automf 7:
    #  |      * dismal
    #  |      * poor
    #  |      * mediocre
    #  |      * average (always middle)
    #  |      * decent
    #  |      * good
    #  |      * excellent

# print(question_experience_simulation.output)
# print(question_OOP_simulation.output)
# print(question_repos_simulation.output)
# print(question_multi_simulation.output)
# print(question_pointer_simulation.output)
# print(question_highlev_simulation.output)

# consequents["python_lang"].view(question_repos_simulation)
# consequents["python_lang"].view(question_OOP_simulation)
# consequents["python_lang"].view(question_multi_simulation)
# consequents["python_lang"].view(question_pointer_simulation)
# consequents["python_lang"].view(question_highlev_simulation)


# question_care.view(question_OOP_simulation)
# answer_yn.view(question_OOP_simulation)

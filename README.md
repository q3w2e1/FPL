# FPL (First Programming Language)

Project implements knowledge from an article (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3933420/) about the dilemma of choosing the first programming language. Even though it may be a fact that it generally does not matter that much (which language you choose first), nevertheless, people
sometimes need the feeling of heading the right direction. This system mimics reading through the FPL article and applying the reader's preference on the data. The point is - instead of reading 25 pages of research paper, take this test and extract the knowledge from the article in less than a few minutes.

Out of X characteristics, only 6 has been chosen to be a part of this deciding system.

Technically it is an expert system with 6 questions, 2 antecedent (input preferences based on a question) for each question and 7 final consequents (hypotheses/languages). It is implemented in fuzzy logic using the scikit-fuzzy package.

# How to run
FPL.py and gui_kivy.py are both ready to be run by Python. FPL.py proposes command-line interface, gui_kivy.py has its own GUI to the same functionality. In the "dist" folder, there is an executable if you don't have Python installed on your computer (please, run with the respective .kv file in the same directory).
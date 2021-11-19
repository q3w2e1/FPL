# FPL (First Programming Language)

Project implements knowledge from an article (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3933420/) about the dilemma of choosing the first programming language. 

This system mimicks reading through the FPL article and applies the reader's preference on the data. The point is - instead of reading 25 pages of research paper, take this test and extract the knowledge from the article in less than a few minutes.

Out of many characteristics, only 6 has been chosen to be a part of this deciding system. Technically it is an expert system with 6 questions, 2 antecedent (input preferences based on a question) for each question and 7 final consequents (hypotheses/languages). It is implemented in fuzzy logic using the scikit-fuzzy package.

# How to run
FPL.py and FPL_cmd.py are both ready to be run by Python and provide you with interactive consultation. 

FPL_cmd proposes command-line interface, FPL has its own GUI to the same functionality. 

In the distribution (dist/) folder, there is an executable if you don't have Python installed on your computer (please, run with the respective .kv file present in the same directory).
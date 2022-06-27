name = input("Please type your name.\n")
print(f"Welcome, {name}. Just press anything if you're ready to begin.")
ready = input()

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [ 
     "Question 1:\nIn Python 3, which functions are used to accept input from the user:\nA. input()\nB. raw_input()\nC. enter()\n\nAnswer:  ",
     "\nQuestion 2:\nWhatever you enter as input, the input() function converts it into a string.\nA. True\nB. False\nC. If\n\nAnswer:  ",
     "\nQuestion 3:\nWhat is the data type of print(type(10))?\nA: float\nB: integer\nC. int\n\nAnswer:  ",
     "\nQuestion 4:\nWhich of the following is not a type of computer code related to Program Execution?\nA: Source code\nB: Bytecode\nC. Hex code\n\nAnswer:  ",
     "\nQuestion 5:\nPython is _____ programming language.\nA: low-level\nB: mid-level\nC. high-level\n\nAnswer:  ",
     "\nQuestion 6:\nWhat does a compiler do?\nA: Translates computer code from machine level to byte code.\nB: Translates computer code from higher-level programming language to machine code.\nC. A compiler does nothing.\n\nAnswer:  ",
     "\nQuestion 7:\nWhich of the following is not a programming language?\nA: Python\nB: Anaconda\nC. Java\n\nAnswer:  ",
     "\nQuestion 8:\nWhat is output for:\na = ['he', 'she', 'we']' '.join(a)\n\nA: heshewe\nB: [he she we]\nC. 'he she we'n\n\nAnswer:  ",
     "\nQuestion 9:\nWhich of the following is more accurate for the following declaration?\nx = Circle()\n\nA: x contains a reference to a Circle object.\nB: Now you can assign int value to x.\nC. x contains an int value.\n\nAnswer:  ",
     "\nQuestion 10:\nWhich of the following is correct about Python?\nA: It provides very high-level dynamic data types and supports dynamic type checking.\nB: It can be used as a scripting language or can be compiled to byte-code for building large applications.\nC. All of the above.\n\nAnswer:  ",
     "\nQuestion 11:\nIs python a case sensitive language?\nA: True\nB: False\n\nAnswer:  ",
     "\nQuestion 12:\nWhich of the following data types is not supported in python?\nA: Strings\nB: Numbers\nC. Slice\n\nAnswer:  ",
     "\nQuestion 13:\nWhat is the output of: print str[2:5] if str = 'Hello World!'?\nA: llo\nB: H\nC. llo World!\n\nAnswer:  ",
     "\nQuestion 14:\nWhich of the following is correct about tuples?\nA: A tuple consists of a number of values separated by commas.\nB: Unlike lists, however, tuples are enclosed within parentheses.\nC. All of the above.\n\nAnswer:  ",
     "\nQuestion 15:\nWhat is the output of print list if:\nlist = [ 'abcd', 786 , 2.23, 'john', 70.2 ]?\n\nA: Error\nB: [ 'abcd', 786 , 2.23, 'john', 70.2 ]\nC. List\n\nAnswer:  ",
]

questions = [
     Question(question_prompts[0], "A"),
     Question(question_prompts[1], "A"),
     Question(question_prompts[2], "C"),
     Question(question_prompts[3], "C"),
     Question(question_prompts[4], "C"),
     Question(question_prompts[5], "B"),
     Question(question_prompts[6], "B"),
     Question(question_prompts[7], "A"),
     Question(question_prompts[8], "A"),
     Question(question_prompts[9], "C"),
     Question(question_prompts[10], "A"),
     Question(question_prompts[11], "C"),
     Question(question_prompts[12], "A"),
     Question(question_prompts[13], "C"),
     Question(question_prompts[14], "B"),
]

def quiz(questions):
    score = 0
    for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
    if (score < 15) and (score > 9):
        print(f"\n⭐  Excellent, {name}! You got {score} out of {len(questions)}! ⭐")
    elif (score < 10) and (score > 5):
        print(f"\nGreat, {name}! You got {score} out of {len(questions)}!")
    elif (score < 5) and (score > 0):
        print(f"\nYou only got {score} out of {len(questions)} You can do better, {name}!")
    elif score == 0:
        print(f"\nYou got {score} out of {len(questions)} Please study hard, {name}!")

quiz(questions)
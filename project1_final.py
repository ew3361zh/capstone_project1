""" 8/28/21 Niko Tomlinson edits to Clara James quiz program:
    Interactive quiz program giving user opportunity 
    to choose between multiple offered subject areas
    and then they are asked questions in that subject area
    and told whether they answered correctly or incorrectly.
    Program functions added, data structures added, user interaction
    improved including validation and allowing for user to enter
    answers in any case desired.
"""

# global variable of quiz questions and answers dictionary nested within a dictionary. Easy to add and remove topics and questions
question_bank = {
        'space': {
            'Which planet is closest to the sun? ': 'Mercury',
            'Which planet spins in the opposite direction to all the others in the solar system? ':'Venus',
            'How many moons does Mars have? ': '2',
            'Is Pluto a plant these days? ': 'Nobody knows',
            'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as a what? ': 'Meteor'
        },
        'art': {
            'Who painted the Mona Lisa? ': 'Leonardo Da Vinci',
            'What precious stone is used to make the artist\'s pigment ultramarine? ': 'Lapiz Lazuli',
            'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city? ': 'Chicago'
        },
        'geoint': {
            'In what year was the National Imagery and Mapping Agency established in the US? ': '1996',
            'Geospatial Intelligence seeks to anticipate patterns of life through ______ (fill in the blank): ': 'Time',
            'What is the term for the process by which people give meaning to their collective experiences? ' : 'Sensemaking',
            'What is the best two-word definition for this incredibly difficult to define area of research? ': 'Domestic spying'
        }
    }

def main():
    total_score = 0
    print('\n')
    print('Welcome to our quiz program!\n')
    print('You can choose to answer questions from the following categories:\n')
    for topic in question_bank: # loop through topic keys in question_bank library
        print(topic)
        print('-----')
    print('\n')
    topic_questions = validate_topic_choice() #input function called
    total_score = ask_questions(topic_questions, total_score) #processing function called
    score_output(total_score, len(topic_questions)) #output results to user, send down both updated total score from ask_questions 
                                                    #function return and the number of questions in their particular chosen topic area
    print('\n')
    print('Thank you for playing!\n')

def validate_topic_choice():
    topic_requested = input('On which of the above listed topics would you like to be quizzed? ')
    print('\n')
    while topic_requested.lower() not in question_bank.keys(): #validation based on keys and using .lower() to make sure case isn't a cause of user input being rejected
        print('Please only choose from one of the below listed categories\n')
        for topic in question_bank:
            print(topic)
        print('\n')
        topic_requested = input('Try again, in which of the above listed topics would you like to be quizzed? ')
    topic_questions = question_bank[topic_requested]
    return topic_questions #return chosen q/a sub dictionary to main for use in the ask_questions function

def ask_questions(topic_questions, total_score):
    for question in topic_questions:
        answer = input(question)
        print('\n')
        if answer.lower() == topic_questions[question].lower(): #checking if user answer matches and removing casing as possible reason for no match
            print('Correct!\n')
            total_score += 1
        else:
            print(f'Sorry, the correct answer is {topic_questions[question]}\n')
    return total_score #return updated total score to main for use in output function to user

def score_output(total_score, number_of_questions): #several forms of output based on number of questions correctly answered and accounts for variances in number of questions in question_bank
    if total_score == number_of_questions:
        print('You got all the answers correct!')
    else: #grammatical if/else block accounting for questions vs. question correctness
        if total_score != 1:
            print(f'You answered {total_score} questions correctly')
        else:
            print('You answered 1 question correctly')

main()
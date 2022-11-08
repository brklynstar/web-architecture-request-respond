from flask import Flask
import random

app = Flask(__name__)

#Favorite Animal Route
@app.route('/') 
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

#Favorite Animal Route
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

#Favorite Dessert route
@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

#Mad Libs Route
@app.route('/madlibs/<adjective>/<noun>')
def madlibs_result(adjective, noun):
    """Display a madlib that changes based on the users input of adjective and noun"""
    return f'''I can't stand the {adjective} {noun}!
    The {noun} doesn't even look {adjective} at all!
    I wish I had a {noun}. I think it would be {adjective}!
    '''

#Multiply 2 Numbers
@app.route('/multiply/<number1>/<number2>')   
def multiply_numbers(number1, number2):
    answer = int(number1) * int(number2)
    if answer.isdigit():
        return (f'{number1} * {number2} = {answer}')
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers'
    
 
# print("Invalid inputs. Please try again by entering 2 numbers!")
# ''' Displays the product of number1 and number2'''
        
#Say in times   
@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    result = str(word) * int(n)
    return result
'''Repeats a string a given number of times'''

#Dice Game
@app.route('/dicegame/')
def dicegame():
    number = random.randint(1,7)
    if number != 6:
        return f'You rolled a {number}. You lost!'
    else:
        return f'You rolled a {number}. You win!'



if __name__ == '__main__':
    app.run(debug=True)
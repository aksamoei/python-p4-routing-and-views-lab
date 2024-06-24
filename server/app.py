#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''map the / to return an h1 element'''
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    '''prints and returns a view'''
    print(f"{param}")
    return f'{param}'

@app.route('/count/<int:user_range>')
def count(user_range):
    resp_value = []
    for num in range(user_range):
        resp_value.append(str(num))
    return '\n'.join(resp_value) + "\n"

@app.route('/math/<int:num1>/<operation>/<int:num2>')  
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1/num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return('Enter a valid operator')

    
        
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)


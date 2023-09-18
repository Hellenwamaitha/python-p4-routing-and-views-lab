#!/usr/bin/env python3

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string_param>')
def print_string(string_param):
    print(string_param)
    return f'Printed: {string_param}'

@app.route('/count/<int_param>')
def count(int_param):
    numbers = '\n'.join(str(i) for i in range(int_param))
    return f'Counting from 0 to {int_param}:\n{numbers}'

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return str(result)
    else:
        return 'Invalid operation'



if __name__ == '__main__':
    app.run(port=5555, debug=True)

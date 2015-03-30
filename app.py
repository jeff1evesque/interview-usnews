## @app.py
# This file loads corresponding logic, and html template file(s), which
#     allows the presentation of (asynchronous) content.
import json
from flask import Flask, render_template, request
from package.calculator.calculate_result import Calculate_Result
from package.validator.validate_input import Validate_Input

# Initialize: create flask instance
app = Flask(__name__)

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(400)
def bad_request(e):
    return {'status': 'error', 'numbers': None, 'error': 'bad request'}

@app.errorhandler(404)
def page_not_found(e):
    return {'status': 'error', 'numbers': None, 'error': 'page not found'}

@app.errorhandler(410)
def page_gone(e):
    return {'status': 'error', 'numbers': None, 'error': 'requested resource no longer available'}

@app.errorhandler(500)
def internal_error(e):
    return {'status': 'error', 'numbers': None, 'error': 'internal server error'}

@app.route('/api', methods=['POST', 'GET'])
def api():
    if request.method == 'GET':
        # local variables
        list_error = []

        # query string
        word      = request.args.get('word')
        max_value = request.args.get('max_value')

        # validate 'word', and 'max_value'
        validate_input = Validate_Input(word, max_value)
        validate_input.validate()
        if validate_input.get_error():
            list_error.append(validate_input.get_error())

        # calculate result
        if validate_input.get_status():
          sent_data  = Calculate_Result(word, max_value)
          sent_data.calculate()
          if sent_data.get_error():
              list_error.append(sent_data.get_error())

        # return result
        if len(list_error) > 0:
            calculated = {'status': 'error', 'numbers': None, 'error': list_error}
        else:
            calculated = {'status': 'ok', 'result': sent_data.get_result(), 'error': None}
        return json.dumps(calculated)
    else:
        error = 'Must provide valid \'GET\' request with \'word\', and \'max_value\''
        return {'status': 'error', 'result': None, 'error': error}

# Execute: run application directly, instead of import
if __name__ == '__main__':
    app.run(
    debug=True
)

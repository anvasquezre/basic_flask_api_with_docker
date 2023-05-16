from flask import jsonify, render_template, request, Blueprint, json


router = Blueprint("app_router", __name__)

@router.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        data = "hello to my simple app"
        return render_template("index2.html", name="Andres")


@router.route('/sum', methods = ['GET', 'POST'])
def sum():
    """
    Function to sum two numbers, works through GET and POST methods. Numbers
    given by the user must by passed in variables `num1` and `num2`.

    Parameters
    ----------
        GET: get two numbers through query parameters.
             Example: curl -X GET "http://127.0.0.1:5000/sum?num1=1&num2=2"
        POST: get two numbers through a json file.
              Example: curl -X POST -H "Content-type: application/json" -d "{\"num1\" : 1, \"num2\" : 2}" "localhost:5000/sum"
    Returns
    -------
        Renders the template with the number
    """
    if request.method == 'GET':
        if (request.args.get('num1') and request.args.get('num2')):
            num1 = float(request.args.get('num1'))
            num2 = float(request.args.get('num2'))
            result = num1 + num2
            return render_template("index2.html", num1 = num1, num2 = num2, result = result)
        else:
            return jsonify({"Error": "Request Error please add then numbers to the query"})
    elif request.method == 'POST':
        if request.content_type == "application/json":
            data = request.get_json()
            num1 = data['num1']
            num2 = data['num2']
            result = num1 + num2
            return render_template("index2.html", num1 = num1, num2 = num2, result = result)
        else:
            return jsonify({"Error": "Request 'Error: Data must be sent in JSON format.'"})
    else:
        return jsonify({"Error": "Request Error"})

        

    
        

    # This code should run as a it is
    
    #return jsonify({"result" : result})
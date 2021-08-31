from flask import Flask, Response, request, Request
import json

import exceptions
from calc import calculate_exp


app = Flask(__name__, static_url_path='', static_folder='dist')


@app.route('/', methods=["POST"])
def analyze_request():
    try:
        data = request.get_json()
        operator = data["operator"]
        operand_l = data["left"]
        operand_r = data["right"]
        ans = calculate_exp(operand_l, operand_r, operator)
        return json.dumps(ans), 200

    except exceptions.ZeroDevision as e:
        return json.dumps(e.message), e.status_code

    except exceptions.InvalidOperand as e:
        return json.dumps(e.message), e.status_code  

    except ValueError as e:
        return json.dumps(e.message), 400

    except KeyError as e:
        return json.dumps(e.message), 500


if __name__ == '__main__':
    app.run(port=3000)
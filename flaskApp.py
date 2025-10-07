from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Arithmetic API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f4f8;
                color: #333;
                padding: 20px;
            }
            h2 {
                color: #007BFF;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                margin-bottom: 8px;
            }
            a {
                text-decoration: none;
                color: #28a745;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
            form {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                max-width: 400px;
            }
            input, select {
                width: 100%;
                padding: 8px;
                margin-top: 5px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            button {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 10px 19px;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 11px;
            }
            button:hover {
                background-color: #0056b3;
            }
            .result {
                margin-top: 20px;
                font-size: 1.2em;
                font-weight: bold;
                color: #17a2b8;
            }
        </style>
    </head>
    <body>
        <h2>Welcome to the Arithmetic API</h2>
        <p>Use the following endpoints in your browser or tools like Postman:</p>
        <ul>
            <li><a href="/add?a=10&b=5">/add?a=10&b=5</a></li>
            <li><a href="/sub?a=10&b=5">/sub?a=10&b=5</a></li>
            <li><a href="/mul?a=10&b=5">/mul?a=10&b=5</a></li>
            <li><a href="/div?a=10&b=5">/div?a=10&b=5</a></li>
        </ul>

        <h3>Try it here:</h3>
        <form action="/calc" method="get">
            <label>First number:
                <input type="number" name="a" step="any" required>
            </label><br><br>
            <label>Second number:
                <input type="number" name="b" step="any" required>
            </label><br><br>
            <label>Operation:
                <select name="op">
                    <option value="add">Add</option>
                    <option value="sub">Subtract</option>
                    <option value="mul">Multiply</option>
                    <option value="div">Divide</option>
                </select>
            </label><br><br>
            <button type="submit">Calculate</button>
        </form>
    </body>
    </html>
    """

# Routes d’API inchangées
@app.route('/add', methods=['GET'])
def add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({'result': a + b})

@app.route('/sub', methods=['GET'])
def sub():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({'result': a - b})

@app.route('/mul', methods=['GET'])
def mul():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({'result': a * b})

@app.route('/div', methods=['GET'])
def div():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    if b == 0:
        return jsonify({'error': 'Division by zero is not allowed'}), 400
    return jsonify({'result': a / b})

@app.route('/calc', methods=['GET'])
def calc():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        op = request.args.get('op')

        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            if b == 0:
                return "❌ Division by zero is not allowed", 400
            result = a / b
        else:
            return "❌ Invalid operation", 400

        return f"<div class='result'>✅ Result: {result}</div><a href='/'>Back</a>"

    except Exception as e:
        return f"❌ Error: {str(e)}", 400

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)


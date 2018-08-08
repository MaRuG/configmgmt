from flask import Flask, render_template, request
import get_config2
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/save', methods = ['POST', 'GET'])
def save():
   if request.method == 'POST':
     result = request.form
     # print(type(result['config']))
     get_config2.write_config(result["config"])
     
     return render_template('form.html', save="SAVE DONE")

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
   if request.method == 'POST':
     result = request.form
     config = get_config2.get_config(result['os'],result['addr'],result['name'],result['pass'],result['port'])
     # print(config) 
     return render_template("confirm.html", config=config)
   #    print(result)
   #    print(result['addr'])
   #    return render_template("confirm.html",result = result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

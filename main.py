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

@app.route('/add')
def add():
   return render_template('add.html')
   
@app.route('/save', methods = ['POST', 'GET'])
def save():
   if request.method == 'POST':
     result = request.form
     get_config2.write_config(result["config"])
     
     return render_template('form.html', save="SAVE DONE")

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
   if request.method == 'POST':
     result = request.form
     device = get_config2.device_load(result['os'],result['addr'],result['name'],result['pass'],result['port'])
     config = get_config2.get_config(device)
     return render_template("confirm.html", config=config)

@app.route('/compare', methods = ['POST', 'GET'])
def compare():
   if request.method == 'POST':
     result = request.form
     device = get_config2.device_load(result['os'],result['addr'],result['name'],result['pass'],result['port'])
     comp = get_config2.add_config(device, result['config'])
     
     return render_template("compare.html", comp=comp, result=result)

@app.route('/commit', methods = ['POST', 'GET'])
def commit():
   if request.method == 'POST':
        result = request.form
        device = get_config2.device_load(result['os'],result['addr'],result['name'],result['pass'],result['port'])
        get_config2.commit(device, result["commit"])
     
        return render_template('form.html', save="COMMIT DONE")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

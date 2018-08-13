from flask import Flask, render_template, request, send_file
import get_config2
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

# github webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        j = request.json

        if j.get('action') == "created":
            comment = j.get('comment').get('body')

        return'success', 200
    else:
        abort(400)

@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/add', methods = ['POST', 'GET'])
def add():
   if request.method == 'POST':
     result = request.form
     print(result)
   return render_template('add.html', result=result)
   
@app.route('/save', methods = ['POST', 'GET'])
def save():
   if request.method == 'POST':
     result = request.form
     get_config2.write_config(result["config"], result["file"])
     filename = result["file"] + ".config"
     f = "configs/" + filename
     return send_file(f, attachment_filename=filename, as_attachment=True)
     
     # return render_template('form.html', save="SAVE DONE")

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
   if request.method == 'POST':
     result = request.form
     device = get_config2.device_load(result['os'],result['addr'],result['name'],result['pass'],result['port'])
     config = get_config2.get_config(device)
     return render_template("confirm.html", config=config, result=result)

@app.route('/compare', methods = ['POST', 'GET'])
def compare():
   if request.method == 'POST':
     result = request.form
     print(result)
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

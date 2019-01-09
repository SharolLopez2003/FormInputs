from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", input_data=dropdown,
                           output="??? Why would you do that? well, that's a megga big oof chief %s, let's prey to our lord and savior, Pewdiepie, to repent our sins." % name)

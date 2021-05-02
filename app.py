# Virtual Enviroment: .\env\Scripts\activate
from flask import Flask, render_template, request
import json
from yamlPath import CustomYamlParse


app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/parse',methods=['POST'])
def parse():
    # Gets the data from the From specified within the home.html
    req=request.form
    query=req.get('input_query','Unable to retrieve query')
    input_data=req.get('input_info','Unable to retrieve input data')
    # Removes all tabs and spaces from the input data
    input_data=input_data.replace('\t','   ')
    # Parses the input data with the specified query
    parser = CustomYamlParse(query,str(input_data))

    return render_template('parse.html', output_data=json.dumps(parser.parse()))

    
if __name__ == "__main__":
    app.run(debug=True)

    
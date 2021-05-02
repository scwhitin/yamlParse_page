# Virtual Enviroment: .\env\Scripts\activate
from flask import Flask, render_template, request
import json
from yamlPath import CustomYamlParse
from yamlpath.exceptions import YAMLPathException
from ruamel.yaml.parser import ParserError

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    req = request.form
    query = req.get('input_query','')
    data = req.get('input_data','')
    rows = data.count("\n")+1
    if rows < 15:
        rows = 15 

    return render_template('home.html', rows=rows, input_query=query, input_data=data)

@app.route('/parse',methods=['POST'])
def parse():
    # Gets the data from the From specified within the home.html
    req = request.form
    query = req.get('input_query','Unable to retrieve query')
    data = req.get('input_data','Unable to retrieve input data')
    # Removes all tabs and spaces from the input data
    data = data.replace('\t','    ')
    # Parses the input data with the specified query
    output_data = None
    header = "Parsed Output:"
    try:
        parser = CustomYamlParse(query,str(data))
        output_data = json.dumps(parser.parse())
    except (YAMLPathException, ParserError) as e:
        output_data = str(e)
        header = "Error:"

    return render_template('parse.html', header=header, rows=output_data.count("\n")+1, output_data=output_data, input_query=query, input_data=data)

    
if __name__ == "__main__":
    app.run()

    
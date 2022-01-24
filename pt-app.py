import pickle
from flask import Flask, render_template, request, jsonify
from functions import *

import warnings
warnings.filterwarnings("ignore")

# Initialise the Flask object to run the flask app 
app = Flask(__name__)

# Deserialization
# Product Type
product_type_vectorizer = pickle.load(open('product_type_vectorizer.sav', 'rb'))
product_type_finalized_model = pickle.load(open('product_type_finalized_model.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  name = request.form['makeup-name']
  discription = request.form['makeup-discription']
  data = str(name) + ' ' + str(discription)

  # Apply nlp
  nlpdata = clean_text(data)
  nlpdata = [nlpdata]

  # Predicting the label for the features collected
  # Fit trained product type TfidfVectorizer for 'text'
  vectorised_product_type_documents = product_type_vectorizer.transform(nlpdata)

  #fit product type final model
  product_type_predict = product_type_finalized_model.predict(vectorised_product_type_documents)
  
  return render_template('index.html', prediction_text = 'Product Type: {}'.format(product_type_predict[0].capitalize()))


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

# It is the starting point of code
if __name__=='__main__':
  # We need to run the app to run the server
  app.run(debug = True)

  ## EC2
#   app.run(host = '0.0.0.0', port = 8080)
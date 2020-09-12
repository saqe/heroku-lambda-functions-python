from flask import Flask
from functions.filter_count_documents import count_filter_document
app = Flask(__name__)

@app.route('/')
def index():
   return 'Hello world'

@app.route('/count-filters-documents')
def filters_document():
   return count_filter_document()

if __name__ == '__main__':
   app.run(debug = True)
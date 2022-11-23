from flask import (
    Flask, 
    jsonify,
    request,
    Response
)

from handler import handleRequest
from article import extractTextFromUrl

# Function that create the app 
def create_app(test_config=None ):
    # create and configure the app
    app = Flask(__name__)

    # Simple route
    @app.route('/summarize', methods=['POST'])
    def summarize(): 
        data = request.get_json()
        algorithm = ''
        url = ''
        language = ''
        try:
            algorithm = data['algorithm']
        except:
            return (jsonify({
                "message": "Algorítmo não especificado"
            }), 400)
        if not (data.get('url') is None):
            url = data['url']

        if not (data.get('text') is None):
            text = data['text']

        if url == '' and text == '':
            return (jsonify({
                "message": "Nenhum texto ou url especificado"
            }), 400)
        if not(data.get('language') is None):
            language = data['language']

        textToSummarize = ''
        if url != '':
            textToSummarize = extractTextFromUrl(url)
        else:
            textToSummarize = text

        return jsonify({
           "summarizedText": handleRequest(textToSummarize, algorithm)
        }) 
     
    return app

APP = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=5000, debug=True)
    APP.run(debug=True)
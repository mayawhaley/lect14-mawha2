import os, flask

app = flask.Flask(__name__)

import models


@app.route('/')
def index():
    addresses = models.Usps.query.all()
    html = ['<li>'+ a.address + '</li>' for a in addresses]
    return '<ul>' + ''.join(html) + '</ul>'
    
if __name__ == '__main__':
    
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

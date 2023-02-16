from pod import create_app
import sys

app = create_app()
@app.before_request
def before_request(response):
    print(f'********************* {response}******************',file=sys.stderr)
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods','GET,PATCH,POST,DELETE,OPTIONS')
    return response
if __name__ == 'main':
    app.run(debug=True)
from flask import Flask
from flask import jsonify
app = Flask(__name__)

print('____________api started_______')

@app.route('/api/consultproduct', methods=['GET'])
def consulting_product():
    return jsonify({
        'status': 200,
        'message': 'Meu app nextjs com flask api no backend'
    })

if __name__ == '__main__':
    app.run( port=5000)
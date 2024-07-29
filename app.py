from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)  # Aktifkan CORS untuk seluruh aplikasi

def dummy_smartpy_check(customer_id, amount):
    # Simulasi panggilan kontrak SmartPy
    try:
        result = subprocess.run(['smartpy-cli', 'run-scenario', 'dummy_contract.py'], capture_output=True, text=True)
        if result.returncode != 0:
            return False, result.stderr
        # Mengurai hasil eksekusi untuk memeriksa kebenaran logika kontrak
        output = result.stdout
        # Misalnya, kita mencari string khusus dalam output untuk menentukan keberhasilan
        if 'Scenario executed successfully' in output:
            return True, {
                'customer_id': customer_id,
                'amount': amount,
                'status': 'valid'
            }
        else:
            return False, 'Scenario execution failed'
    except Exception as e:
        return False, str(e)

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    customer_id = data.get('customerId')
    amount = data.get('amount')

    # Kode sementara sebelum memanggil dummy_smartpy_check
    return jsonify({
        'success': True,
        'message': 'Dummy check successful',
        'data': {
            'customerId': customer_id,
            'amount': amount,
        }
    })

    # success, result = dummy_smartpy_check(customer_id, int(amount))

    # if success:
    #     return jsonify({
    #         'success': True,
    #         'message': 'Dummy check successful',
    #         'data': result
    #     })
    # else:
    #     return jsonify({
    #         'success': False,
    #         'message': 'Invalid request',
    #         'error': result
    #     }), 400

if __name__ == '__main__':
    app.run(port=4000)

from flask import Flask, jsonify, request
from safer import CompanySnapshot
from safer.exceptions import CompanySnapshotNotFoundException, SAFERUnreachableException
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/search', methods=['GET'])
def search_company():
    name = request.args.get('name', '')
    try:
        search_results = CompanySnapshot.search(name)
        return jsonify(search_results=search_results.to_dict()), 200
    except (ValueError, SAFERUnreachableException) as e:
        return jsonify(error=str(e)), 400

@app.route('/company/usdot/<int:number>', methods=['GET'])
def get_company_by_usdot(number):
    try:
        company = CompanySnapshot.get_by_usdot_number(number)
        return jsonify(company=company.to_dict()), 200
    except (ValueError, CompanySnapshotNotFoundException, SAFERUnreachableException) as e:
        return jsonify(error=str(e)), 400

@app.route('/company/mcmx/<int:number>', methods=['GET'])
def get_company_by_mcmx(number):
    try:
        company = CompanySnapshot.get_by_mc_mx_number(number)
        return jsonify(company=company.to_dict()), 200
    except (ValueError, CompanySnapshotNotFoundException, SAFERUnreachableException) as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)

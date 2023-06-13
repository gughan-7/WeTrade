from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

# db = firestore.client()

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@views.route('/market', methods=['GET', 'POST'])
def market():
    return render_template("market.html")

@views.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    return render_template("portfolio.html")

@views.route('/watchlist', methods=['GET', 'POST'])
def watchlist():
    return render_template("watchlist.html")
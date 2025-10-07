from flask import Blueprint, render_template
import pandas as pd
from .utils import read_csv

main = Blueprint('main', __name__)

@main.route('/')
def home():
    data = read_csv('database.csv')
    return render_template('index.html', data=data)
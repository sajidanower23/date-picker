#!/usr/bin/env python3

from flask import Flask

from typing import Optional
import random

app = Flask(__name__)

dates = [
    'Bowling',
    'Movies',
    'Archery',
    'Dinner (Takeaway)',
    'Dinner (Cheap)',
    'Dinner (Moderate)',
    'Dinner (Fancy)',
]

@app.route("/date/pick")
def pick_date():
    return random.choice(dates)

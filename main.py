#!/usr/bin/env python3

from typing import Optional

from fastapi import FastAPI

import random

app = FastAPI()

dates = [
    'Bowling',
    'Movies',
    'Archery',
    'Dinner (Takeaway)',
    'Dinner (Cheap)',
    'Dinner (Moderate)',
    'Dinner (Fancy)',
]

@app.get("/date/pick")
def pick_date():
    return random.choice(dates)

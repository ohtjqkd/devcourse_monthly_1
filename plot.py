import json
import os
from datetime import datetime

import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go

PATH = os.path.dirname(os.path.abspath(__file__))

def draw_strip():
    DF = pd.read_csv(os.path.join(PATH, '2021VAERSData', 'my_vaers.csv'))
    px.strip(DF, x='')
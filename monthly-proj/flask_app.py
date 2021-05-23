from flask import Flask, request, render_template
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# app = Flask(__name__)

template_path = "./templates/"

@app.route('/')
def get_index():
    
    return render_template(template_name_or_list=template_path+'index.html')

df = px.data.iris()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="scatter-plot"),
    html.P("Petal Width:"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=2.5, step=0.1,
        marks={0: '0', 2.5: '2.5'},
        value=[0.5, 2]
    ),
])

@app.callback(
    Output("scatter-plot", "figure"), 
    [Input("range-slider", "value")])
def update_bar_chart(slider_range):
    low, high = slider_range
    mask = (df['petal_width'] > low) & (df['petal_width'] < high)
    fig = px.scatter(
        df[mask], x="sepal_width", y="sepal_length", 
        color="species", size='petal_length', 
        hover_data=['petal_width'])
    return fig






if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
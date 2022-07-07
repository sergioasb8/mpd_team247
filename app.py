from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import os
# parts of the app
from pages import home

external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)
server = app.server


# styles
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#0C1821",
    "color": "white",
    "overflow": "scroll",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.Img(src="assets/images/logo.jpg", height="200px",width="200px"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(["Home  ",html.Img(src='https://api.iconify.design/fluent/home-20-regular.svg?color=white', style={'width': '10%', 'height': '10%','margin-bottom':'2%'})], href="/", active="exact"),
                dbc.NavLink(["Overview  ",html.Img(src='https://api.iconify.design/carbon/idea.svg?color=white', style={'width': '10%', 'height': '10%','margin-bottom':'2%'})], href="/overview", active="exact"),
                dbc.NavLink(["Dataset  ",html.Img(src='https://api.iconify.design/bx/data.svg?color=white', style={'width': '10%', 'height': '10%','margin-bottom':'2%'})], href="/dataset", active="exact"),
                dbc.NavLink(["EDA  ",html.Img(src='https://api.iconify.design/healthicons/magnifying-glass.svg?color=white', style={'width': '10%', 'height': '10%','margin-bottom':'2%'})], href="/EDA", active="exact"),
                dbc.NavLink(["Model  ",html.Img(src='https://api.iconify.design/emojione-monotone/nut-and-bolt.svg?color=white', style={'width': '10%', 'height': '10%','margin-bottom':'2%'})], href="/model", active="exact"),
                dbc.NavLink(["Report  ",html.Img(src='https://api.iconify.design/carbon/report.svg?color=white', style={'width': '10%', 'height': '10%','margin-bottom':'2%'})], href="/report", active="exact"),
                dbc.NavLink(["Contact us  ",html.Img(src='https://api.iconify.design/ant-design/phone-outlined.svg?color=white', style={'width': '10%', 'height': '10%','margin-bottom':'2%'})], href="/contact-us", active="exact"),   
            ],
            vertical=True,
            pills=True,
        ),
        html.Br(),html.Br(),
        html.Div([
            html.A([
                html.Img(src="assets/images/DS4A - C1.jpg", height="55px",width="195px"),
            ], href="https://www.correlation-one.com/data-science-for-all-colombia",target="_blank"),
        ]),
        html.Br(),
        html.Div([
            html.A([
                html.Img(src="assets/images//MinTic.jpg", height="45px",width="195px"),
            ], href="https://www.mintic.gov.co/micrositios/cienciadedatos/747/w3-channel.html",target="_blank"),
        ]),
               
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)


# ejecutando app layout
app.layout = html.Div([
    dcc.Location(id="url"), sidebar, content
])

# realizando el callback
@app.callback(Output('page-content', 'children'),
                [Input('url', 'value')])

def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    return f'You have selected'

if __name__ == '__main__':
    app.run_server(debug=True)
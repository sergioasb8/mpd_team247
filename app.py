from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import os
# parts of the app
from pages import home, overview, contact, dataset, eda

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

# realizando el callback - principal-
@app.callback(Output('page-content', 'children'),
                [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/overview":
        return overview.layout
    elif pathname == "/dataset":
        return dataset.layout
    elif pathname == "/EDA":
        return eda.layout
    elif pathname == "/contact-us":
        return contact.layout
    else:
        return f'You have selected'


# callback dataset
@app.callback(Output('dataset_details_md', 'children'),
              Output('feedback_dataset', 'children'),
              Input('dataset_selection', 'value'))
def dataset_info_display(dataset):
    if (not dataset):
        raise PreventUpdate

    if dataset == 'Tweets 2019':

        markdown = """

        ### Variables


        - **full_text** (string): *Full text of the tweet.*
        - **user** (string): *Username who posted the tweet.*
        - **location** (string): *Location where the tweet was post.*
        - **date** (datetime): *Time when the tweet was post.*
        - **tweet_id** (str): *Primary key, number id of the tweet.*
        - **number rt** (int): *Number of retweets of the tweet.*
        - **number likes** (int): *Number of likes of the tweet.*
        - **number reply** (int): *Number of likes in the reply.*
        - **conversation_id** (int): *Identification number of conversation.* 

        #### Size

        4.3 MB

        #### Shape

        Dataframe: (17700, 9)

        #### Creation

        This dataset was created by the search query in the API, which was performed by 
        putting ``Medellin" as a parameter in the search, and 01 January to 31 December 
        of the 2019 year as the beginning and end date points. The file size of this 
        dataset was 4.3 MB and contained a total of 17700 tweets.

        #### Purpose

        This dataset was created to make a first exploratory analysis in order 
        to obtain a first approach and data understanding about the most relevant 
        issues and concerns of the population about Medellin on Twitter. This was 
        done to verify if these issues are correlated or included in the projects 
        and strategic lines of work proposed in the MPD.

    """

    elif dataset == 'Medellin Development Plan':

        markdown = """

        ### Variables


        In this case, this dataset was formed only with the raw text from the 
        document Medellin Development Plan of Medellin 2020-2023 (DPM). Within 
        DMP document there is a chapter called “Líneas Estratégicas” which establishes 
        the different strategic lines of action that encompass the proposals of the 
        government plan and its execution in relation to the most important issues 
        for the city future. For this reason, it was performed a text analysis in 
        order to obtain the most relevant words (the words with higher frequency in 
        the text) for each PDM strategic line This dataset contains all the words 
        contained in the 5 strategic lines of this document.   

        #### Size

        966 KB

        #### Shape

        PDF File: 1543 pages (Full document)
        PDF FIle: 268 pages (Chapter of Strategic Lines)

        #### Creation

        This dataset was formed from the extraction of all the words contained in 
        the strategic lines of PDM document.

        #### Purpose

        Obtain the most relevant words (the words with the highest frequency 
        in the text) for each strategic line of the MDP. This dataset contains 
        all the words contained in the 5 strategic lines of this document. It also 
        helps us to answer our first hypothesis: Is the MDP aligned with the 
        expressed by the population?

        """
    elif dataset == 'Tweets keywords 2019 - 2022':

        markdown = """

        ### Variables


        - **full_text** (string): *Full text of the tweet.*
        - **user** (string): *Username who posted the tweet.*
        - **location** (string): *Location where the tweet was post.*
        - **date** (datetime): *Time when the tweet was post.*
        - **tweet_id** (str): *Primary key, number id of the tweet.*
        - **number_rt** (int): *Number of retweets of the tweet.*
        - **number_likes** (int): *Number of likes of the tweet.*
        - **number_reply** (int): *Number of likes in the reply.*
        - **conversation_id** (int): *Identification number of conversation.*
        - **id_key_word** (int): *Primary key*
        - **key_word** (string): *Key word used to search the tweet*

        #### Size

        90.9 MB

        #### Shape

        Dataframe: (303008, 11)

        #### Creation

        This second dataset was created after the data understanding was performed, 
        this stage included the exploratory data analysis of the Tweets 2019 and 
        the MDP document. In order to consolidate this first dataset, denominated 
        in this project such as **Tweets keywords 2019 - 2022**, various search 
        queries were done in the API for the years 2019, 2020, 2021, and so far 
        2022 taking search parameters a list of strategic keywords extracted 
        from the MDP document, oriented to the lines of the plan to be measured.

        #### Purpose

        This dataset was created in order to make the exploratory data analysis for the **Tweets 2019 - 2022**.

        """
    elif dataset == 'Dataset Model':

        markdown = """

        ### Variables


        - **full_text** (string): *Full text of the tweet.*
        - **user** (string): *Username who posted the tweet.*
        - **location** (string): *Location where the tweet was post.*
        - **date** (datetime): *Time when the tweet was post.*
        - **tweet_id** (str): *Primary key, number id of the tweet.*
        - **number_rt** (int): *Number of retweets of the tweet.*
        - **number_likes** (int): *Number of likes of the tweet.*
        - **number_reply** (int): *Number of likes in the reply.*
        - **conversation_id** (int): *Identification number of conversation.*
        - **id_key_word** (int): *Primary key.*
        - **key_word** (string): *Key word used to search the tweet.* 

        #### Size

        90.9 MB

        #### Shape

        Dataframe: (303008, 11)

        #### Creation

        This dataset was created as a result of the data preparation stage on  
        the **Tweets keywords 2019 - 2022** after a cleaning an preparing text process.

        #### Purpose

        This dataset was created as a result of the data preparation stage on  
        the **Tweets keywords 2019 - 2022** after a cleaning an preparing text process.

        """
    message = dbc.Alert(f"You have selected the dataset: {dataset}.",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True,)

    return markdown, message


# condition to execute the app
if __name__ == '__main__':
    app.run_server(debug=True)
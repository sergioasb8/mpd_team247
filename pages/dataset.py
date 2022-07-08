from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

#Create data description
data_description={
    'column_name':['full_text','user','location','date','tweet_id','number_rt','number_likes','id_key_word'],
    #'data_type':['string','string','string','datetime','int','int','int','int'],
    'description':['full text of the tweet','username who posted the tweet','location where the tweet was post','time when the tweet was post','primary key, number id of the tweet','number of retweets of the tweet','number of likes of the tweet','foreign key with the id that represent the key word']
    }


p = f"""
Welcome to the dataset, in this section you can  access to a description of the data 
used for this project,  the consolidation of the information in different datasets, 
the variables used, the size of the data, how the dataframes were created and the 
purpose of their creations within the execution of the project."
"""

layout = html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Dataset'),
        html.Br(),html.Br(),
        ], style={'textAlign': 'center'}),
    html.P(p),
    html.Br(), html.Br(),
    dbc.CardHeader(html.H2('Dataset selector')),
    html.Br(),
    html.Br(),
    dcc.Dropdown(id='dataset_selection',
                 placeholder='Select one dataset',
                 options=[{'label':'Tweets 2019', 'value':'Tweets 2019'},
                          {'label':'Medellin Development Plan', 'value':'Medellin Development Plan'},
                          {'label':'Tweets keywords 2019 - 2022', 'value':'Tweets keywords 2019 - 2022'},
                          {'label':'Dataset Model', 'value':'Dataset Model'}]),
    html.Br(),
    html.Div([
                dbc.Alert(f"Please choose a dataset from the dropdown to display its description.",
                         color='info',
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],

                id='feedback_dataset'),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(lg=2),
        dbc.Col([
            dcc.Markdown(id='dataset_details_md',
                         style={'backgroundColor': '#FFFFFF'}),
            ],lg=8)

        ]),
    ])



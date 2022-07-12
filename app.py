from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.express as px
import plotly.graph_objects as go
import os
# parts of the app
from pages import home, overview, contact, dataset, eda, model, report

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
    elif pathname == "/model":
        return model.layout
    elif pathname == "/report":
        return report.layout
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



# eda callback

# frequency histogram
@app.callback(Output('chars_freq_hist', 'figure'),
              Output('words_freq_hist', 'figure'),
              Output('feedback_1', 'children'),
              Input('button1', 'n_clicks'),
              State('hist_bins_slider', 'value'),
              )
def plot_freq_hist(nclicks, nbins):
    if (not nclicks):
        raise PreventUpdate

    fig1 = px.histogram(eda.df,
                        x='num_chars',
                        nbins=nbins,
                        color_discrete_sequence=['#5BC0BE'],
                        title='Histogram - Character tweets distribution by length.',
                        marginal="box",
                        height=500,
                        width=500,
                        labels={'num_chars':'Length of text in characters'})
    fig1.layout.paper_bgcolor = '#FFFFFF'
    fig1.layout.plot_bgcolor = '#FFFFFF'
    fig1.update_layout(title_font_size=15)
    
    fig2 = px.histogram(eda.df,
                        x='num_words',
                        nbins=nbins,
                        color_discrete_sequence=['#5BC0BE'],
                        title='Histogram - Words tweets distribution by length.',
                        marginal="box",
                        height=500,
                        width=500,
                        labels={'num_words':'Length of text in words'})
    fig2.layout.paper_bgcolor = '#FFFFFF'
    fig2.layout.plot_bgcolor = '#FFFFFF'
    fig2.update_layout(title_font_size=15)

    message = dbc.Alert(f"The number of bins has been modified to: {nbins} bins.",
                        color='success',
                         fade=True,
                         is_open=True,
                         duration=4000,
                         dismissable=True,)
    return fig1, fig2, message

# Explore the text content of the tweet 
@app.callback(Output('display_tweet_md', 'children'),
              Output('feedback_2', 'children'),
              Input('button2', 'n_clicks'),)

def gen_random_tweet(nclicks):
    if (not nclicks):
        raise PreventUpdate
    random_tweet = eda.df['full_text'].sample().values[0]
    markdown = f"{random_tweet}"
    message = dbc.Alert(f"Random tweet successfully generated.",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True,)
    return markdown, message


# Medellin Development Plan (Tab 2) 
@app.callback(Output('feedback_wc_mdp', 'children'),
              Output('mdp_details_md','children'),
              Output('word_cloud_linea','src'),
              Input('button_lestr', 'n_clicks'),
              State('lineas_estrategicas', 'value'))

def word_cloud_lin(nclicks, linea):
    if (not nclicks):
        raise PreventUpdate
    if (not linea):
        raise PreventUpdate

    for k, v in eda.lineas_estrategicas.items():
        if v == linea:
            seleccion = k
    message = dbc.Alert(f"You have selected - {seleccion}.",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True)
    if linea == 1:
        markdown = f"""
        Likewise, within PDM document there is a chapter called “Líneas Estratégicas” which establishes the different strategic lines of action that encompass the proposals of the government plan and its execution in relation to the most important issues for the city future. Therefore, it was performed a text analysis in order to obtain the most relevant words (the words with higher frequency in the text) for each PDM strategic line by word clouds. You can observe each word cloud for each strategic line selecting the interest option in the given list.
        """
        return message, markdown, 'assets/images/wc_pdm.jpg'
    elif linea == 2:
        markdown = f"""
        The first strategic line seeks to create a digital culture and economic reactivation that will improve the quality of life of the population of Medellin through the management of new opportunities, education, entrepreneurship and job creation in areas associated with the digital economy and the fourth industrial revolution. This objective is closely associ- ated with the words ”life”, ”culture” and ”technology”
        """
        return message, markdown, 'assets/images/wcl1.jpg'
    elif linea == 3:
        markdown = f"""
        The second strategic line seeks to articulate the city with cultural projects that strengthen the creative potential of citizens, safeguarding their heritage and memories, making Medellin a more supportive and peaceful city. It also contains programs focused on youth, gender equality, education, arts, and science. This makes it easy to explain the frequency of the
keywords.
        """
        return message, markdown, 'assets/images/wcl2.jpg'
    elif linea == 4:
        markdown = f"""
        Line strategy 3 focuses on the citizens of Medellin, in promoting, creating and guaranteeing basic and cultural living conditions, in order to have the ability to enhance their human and individual talents. Likewise, it promotes the generation of social, community, healthy, creative, safe and sustainable environments. In addition, in this line there are programs established for youth from public health to the so-called ”Valle del Software”.
        """
        return message, markdown, 'assets/images/wcl3.jpg'
    elif linea == 5:
        markdown = f"""
        The fourth strategic line seeks to move Medellin towards a future of sustainability, in which dignified habitability is guaranteed for its inhabitants and functional and harmonious integration with rural areas. In this line, programs for sustainable and intelligent mobility are highlighted in which include clean energies and cultural transformations, focusing on the conservation of all forms of life.
        """               
        return message, markdown, 'assets/images/wcl4.jpg'
    elif linea == 6:
        markdown = f"""
        The last line strategy aims to reinforce the synergy between government and citizenship, an open dialogue from the different knowledge, the consensus between the different actors and the collective construction of the citizen territorial peace process. Victims and justice are one of the components of this line, as well as security in terms of citizen coexistence and cybersecurity.
        """
        return message, markdown, 'assets/images/wcl5.jpg'

# Data understanding II



# model callback

# Generate a random tweet 
@app.callback(Output('random_feedback', 'children'),
              Output('textarea_preprocess', 'value'),
              Input('button_random', 'n_clicks'),)

def gen_random_tweet(nclicks):
    if (not nclicks):
        raise PreventUpdate
    random_tweet = model.df['full_text'].sample().values[0]

    message = dbc.Alert(f"Random tweet successfully generated.",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True,)

    return message, random_tweet

# Tweet text preprocessing 
@app.callback(Output('feedback_text_proc', 'children'),
              Output('display_preprocess_tweet_text_md', 'children'),
              Input('button1', 'n_clicks'),
              State('textarea_preprocess', 'value'))

def display_preprocees_text(nclicks, text):
    if (not nclicks):
        raise PreventUpdate
    if (not text):
        raise PreventUpdate

    # clean_text = model.clean_tweet(text)
    text1 = model.text_to_lower(text)
    text2 = model.remove_numbers(text1)
    text3 = model.remove_punct(text2)
    text4 = model.remove_accent(text3)
    text5 = model.remove_stopword(text4)
    markdown = f"""
    ###### Raw Text 

    {text} 

    ###### Unify the case of the text: convert it to lowercase.

    {text1}


    ###### Remove numbers.

    {text2}


    ###### Remove punctuation marks and special characters

    {text3}


    ###### Remove accents

    {text4}


    ###### Remove stopwords

    {text5}


    """

    message = dbc.Alert(f"The entered tweet has been successfully processed.",
                        color='success',
                         fade=True,
                         is_open=True,
                         duration=4000,
                         dismissable=True,)

    return message, markdown

# Tweet text classification
@app.callback(Output('feedback_tw_clas', 'children'),
              Output('display_tweet_sentiment_md', 'children'),
              Input('button2', 'n_clicks'),
              State('textarea_preprocess', 'value'))

def gen_sentiment(nclicks, tweet):
    if (not nclicks):
        raise PreventUpdate
    if (not tweet):
        raise PreventUpdate

    sentiment = model.log_reg(tweet)
    if sentiment:
        markdown = f"Positive 😃✅"
        sen = 'Positive'
    else:
        markdown = f"Negative 😡❌"
        sen = 'Negative'

    message = dbc.Alert(f"Your tweet has been classified as {sen} sentiment.",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True,)
    return message, markdown

# report callback

# Explore tweet text sentiment by keyword #####################
@app.callback(Output('explore_feedback', 'children'),
              Output('display_random_tweet_by_key_md', 'children'),
              Input('button1', 'n_clicks'),
              State('random_tweet_year_dropdown', 'value'),
              State('random_tweet_month_dropdown', 'value'),
              State('random_tweet_day_dropdown', 'value'),
              State('random_tweet_keyword_dropdown', 'value'),
              State('random_tweet_sentiment_dropdown', 'value'),)

def gen_random_tweet(nclicks, year, month, day, keyword, sentiment):
    if (not nclicks):
        raise PreventUpdate
    if (not year) and (not month) and (not day) and (not keyword) and (not sentiment):
        year = 2019
        month = 12
        day = 24
        keyword = 9 
        sentiment = 1 

    df_filtered = report.df[(report.df['year'].eq(year)) 
                            & (report.df['month'].eq(month)) 
                            & (report.df['day'].eq(day)) 
                            & (report.df['key_word'] == (keyword)) 
                            & (report.df['sentiment'].eq(sentiment))]

    try:
        random_tweet = df_filtered[['full_text', 'predicted_probability']].sample()
    except ValueError:
        raise PreventUpdate
    else:
        tweet = random_tweet.iloc[0,0]
        predict_prob = random_tweet.iloc[0,1]
        if sentiment == 1:
            p_value = 100 * (2 * predict_prob - 1)
            name = 'Positive Probability'
        elif sentiment == 0:
            p_value = -100 * (2 * predict_prob - 1)
            name = 'Negative Probability'

        markdown = f""" 
        **Tweet:** {tweet}

        **Predicted Probability:** {predict_prob:.4f}

        **{name}**: {p_value:.2f}% 
        """

        sentiments = {1: 'Positive', 0:'Negative'}
    message = dbc.Alert(f"Random tweet generated successfully, you have chosen: {year} (year), {month} (month), {day} (day), {keywords.get(keyword)} (keyword) and {sentiments.get(sentiment)} (sentiment).",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True,)
    return message, markdown

    
# condition to execute the app
if __name__ == '__main__':
    app.run_server(debug=True)
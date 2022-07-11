from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
from pages import tools
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('pages/data/sentiment_1_0.csv')

def log_reg(text):
    df_rating = df
    #df_rating=pd.read_csv('dash_app/pages/data/sentiment_1_0.csv')
    # clean the tweet and save it on a new column

    def clean_tweet(tweet):
        new_tweet=' '
        words = tweet.split()
        for w in words:
            wl = w.lower() # word in lower case
    
            # replace numbers
            for number, new_value in tools.replace_numbers_dict.items():
                wl = str(wl).replace(number,new_value)

            # replace some punctuations mark to keep only words
            for punctuation, new_value in tools.replace_punctuation_dict.items():
                wl = wl.replace(punctuation,new_value)
    
            # replace accent mark 
            for accent, new_value in tools.replace_accent_dict.items():
                wl = wl.replace(accent,new_value)

            if wl not in tools.model_stop_wprds:
                new_tweet += f'{wl} '
        return new_tweet[:-1]
    # clean data
    df_rating['clean_tweet'] = df_rating['full_text'].apply(clean_tweet)
    # split data into train and test
    tweets_train, tweets_test = train_test_split(df_rating, test_size=0.2, random_state=0)    # vectorize data
    vectorizer = CountVectorizer()
    x_train_bow = vectorizer.fit_transform(tweets_train['clean_tweet'])
    y_train_bow = tweets_train['sentiment']
    # train model
    lr_model_all = LogisticRegression()
    lr_model_all.fit(x_train_bow, y_train_bow)
    # predict
    text=clean_tweet(text)
    return lr_model_all.predict(vectorizer.transform([text]))[0]

def clean_tweet(tweet):

    new_tweet = ''
    words = tweet.split()
    for w in words:
        wl = w.lower() # word in lower case

        # replace numbers
        for number, new_value in tools.replace_numbers_dict.items():
            wl = str(wl).replace(number,new_value)

        # replace some punctuations mark to keep only words
        for punctuation, new_value in tools.replace_punctuation_dict.items():
            wl = wl.replace(punctuation,new_value)
        # replace accent
        for accent, new_value in tools.replace_accent_dict.items():
            wl = wl.replace(accent,new_value)

        # remove stop words
        if wl not in tools.model_stop_wprds:
            new_tweet += f'{wl} '

    return new_tweet[:-1]

def text_to_lower(tweet):
    new_tweet = ''
    words = tweet.split()
    for w in words:
        wl = w.lower() # word in lower case
        new_tweet += f'{wl} '
    return new_tweet[:-1]

def remove_numbers(tweet):
    new_tweet = ''
    words = tweet.split()
    for w in words:
        for number, new_value in tools.replace_numbers_dict.items():
            w = str(w).replace(number,new_value)
        new_tweet += f'{w} '
    return new_tweet[:-1]

def remove_punct(tweet):
    new_tweet = ''
    words = tweet.split()
    for w in words:
        for punctuation, new_value in tools.replace_punctuation_dict.items():
            w = w.replace(punctuation,new_value)
        new_tweet += f'{w} '
    return new_tweet[:-1]

def remove_accent(tweet):
    new_tweet = ''
    words = tweet.split()
    for w in words:
        for accent, new_value in tools.replace_accent_dict.items():
            w = w.replace(accent,new_value)
        new_tweet += f'{w} '
    return new_tweet[:-1]

def remove_stopword(tweet):
    new_tweet = ''
    words = tweet.split()
    for w in words:
        if w not in tools.model_stop_wprds:
            new_tweet += f'{w} '
    return new_tweet[:-1]


p1='''
Welcome to the model section. 
Once the data exploration is finished, you will be able to interact 
with the application in this section to generate any tweet from our dataset, 
do the cleaning process of the tweet 
and its classification according to its sentiment. 
Once this section is finished, you will be able to apply this model to the complete dataset.
we will be working with the dataset containing tweets from 2019 to 2022.
'''
p2=''' 
The first thing you will do is understand the cleaning process. This is detailed in the following section and one of the steps of the cleanup is to remove the stopwords. We have prepared a word cloud of them. Do you notice anything in the cloud?
'''
p3='''
What are stopwords?
They are words such as "de", "en" or "la", for example, that do not bring any sentiment to the model. You may even have noticed that "Medellín" has been included in this cloud. The reason is that "Medellín" appears throughout the dataset and since it is the name of a city it will not be meaningful to have it in the dataset either. Removing the stopwords will be a part of the cleaning process of the next step.
'''

p4='''
Let's think of someone who writes "Amo Medellin" and another person who writes "amo medellín". Both want to express the same thing. By removing accents and unifying the lowercase case, we can obtain an equivalent expression for both: "amo medellin". This way the model will work better and removing the stopwords will be easier. Now, you can write a text randomly generating a tweet from our dataset to observe the detailed cleaning process.
'''


p5='''
Now that you have gone through the cleaning process, you will be able to know if the text you wrote or the tweet generated is positive or negative.
'''


p6='''
Do you agree with the outcome of the sentiment? At this point it should be made clear that models are approximations of reality and therefore have a margin of error. How can we measure how close to the real result is the sentiment result you have just obtained? If we apply the model to the complete dataset, what would we get? The next section will answer these questions.
'''


layout = html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Model'),
        ], style={'textAlign': 'center'}),
    html.Br(), html.Br(),
    html.P(p1),

############### Stopwords #################

    html.Br(), html.Br(),
    dbc.CardHeader(html.H3('Stopwords')),
    html.Br(),
    html.P(p2),
    html.Br(), html.Br(),
    dbc.Row([
        dbc.Col(),
        dbc.Col([
            dcc.Loading([
            html.Div([
                html.Img(src='assets/images/wc_text_stop.jpg')
            ]),
            ]),

        ]),
        dbc.Col(),    
    ]),
    html.Br(),html.Br(),

    html.P(p3),


############### Tweet text preprocessing #################
    html.Br(),html.Br(),
    dbc.CardHeader(html.H3('Tweet text preprocessing')),
    html.Br(),
    html.P(p4),
    html.Br(),
    dbc.Label('Tweet text:'),
    dcc.Textarea(
        id='textarea_preprocess',
        placeholder='Enter the text of the tweet',
        style={'width': '100%', 'height': 100}),
    html.Br(),html.Br(),
    html.Div([
                dbc.Alert(f"Enter the text to be processed in the Tweet Text box, if you don't feel creative press the generate random tweet button to do it for you.",
                         color='info',
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],

                id='feedback_text_proc'),
    html.Br(),
    html.Div(id='random_feedback'),
    html.Div([
            dbc.Button("Generate a random tweet",
            outline=True,
            color="primary",
            className="me-1",
            size="sm", id="button_random"),
                ], className="d-grid gap-2 col-6 mx-auto"),
    html.Br(),
    html.Div([
        dbc.Button("Preprocess Text",
        outline=True,
        color="primary",
        className="me-1",
        size="sm",
        id="button1"),
        ],  className="d-grid gap-2 col-6 mx-auto"), 
    html.Br(),
        dcc.Loading([
            dcc.Markdown(id='display_preprocess_tweet_text_md',
                        style={'backgroundColor': '#FFFFFF',
                        'border': '2px solid powderblue',
                        'padding': '30px'}),
        ]),

############### Tweet classification #################
    html.Br(),
    dbc.CardHeader(html.H3('Tweet classification')),
    html.Br(),
    html.P(p5),
    html.Br(),
    html.Div([
                dbc.Alert(f"At the time of viewing this message, the model has an accuracy of 77.7%, so the user may find unexpected results. Please send us your report.",
                         color="warning",
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],

                id='class_warn'),
    html.Div([
                dbc.Alert(f"Click the 'Sentiment classification' button to classify the text entered in the 'Tweet text' box according to a sentiment: positive or negative.",
                         color='info',
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],

                id='feedback_tw_clas'),
    html.Br(), 
     html.Div([
        dbc.Button("Sentiment classification",
        outline=True,
        color="primary",
        className="me-1",
        size="sm",
        id="button2"),
        ],  className="d-grid gap-2 col-6 mx-auto"), 
    html.Br(),
        dcc.Loading([
            dcc.Markdown(id='display_tweet_sentiment_md',
                        style={'backgroundColor': '#FFFFFF', 'border': '2px solid powderblue', 'padding': '30px'}),
        ]),
    html.Br(),html.Br(),
    html.P(p6),
    ])


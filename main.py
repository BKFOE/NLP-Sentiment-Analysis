import streamlit as st
import glob
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path

# Access all the txt files in the folder
filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

# Create an empty list to store negative, and positive scores, and date values
pos = []
neg = []
date = []

# Get the input data, load into python, and analyze content for sentiment and append to list
# created the list of dates from the filenames
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    neg.append(scores["neg"])
    pos.append(scores["pos"])
    date.append(Path(filepath).stem)

# Design the website
st.title("Diary Tone")
st.subheader("Positivity")
x_value = date
y_value = pos
pos_figure = px.line(x=x_value, y=y_value, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
x_value = date
y_value = neg
neg_figure = px.line(x=x_value, y=y_value, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)

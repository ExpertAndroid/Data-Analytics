import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objs as go  # Import Plotly for creating interactive plots
import seaborn as sns

# Load data
mydata = pd.read_csv('D:\\Big Data Analytics\\Pythonpractice\\pandas\\Cleaned_ball_by_ball.csv')

# Title and header
st.title("Ball By Ball IT20 Data")
st.header("Cricket")

# Display DataFrame
newData = mydata.drop(['Unnamed: 0', 'Extra Type'], axis=1)
st.dataframe(newData)

# Sidebar
with st.sidebar:
    st.image('t20.png', width=150,)
    st.title('T20 Cricket Data')

# Function to plot bar chart for wins by batting first and second
def batFirstandSecondWins():
    unique_matches = mydata.drop_duplicates(subset='Match ID')

    bat_first_wins = unique_matches[unique_matches['Bat First'] == unique_matches['Winner']].shape[0]
    bat_second_wins = unique_matches[unique_matches['Bat Second'] == unique_matches['Winner']].shape[0]

    categories = ['Batting First', 'Batting Second']
    wins_count = [bat_first_wins, bat_second_wins]

    # Create Plotly bar chart
    fig = go.Figure(data=[go.Bar(x=categories, y=wins_count, marker=dict(color=['blue', 'yellow']))])
    fig.update_layout(title='Wins by Batting First vs. Batting Second',
                      xaxis_title='Batting Team',
                      yaxis_title='Number of Wins')
    st.plotly_chart(fig)

# Function to plot bar chart for top 10 winning countries
def top10winningCountries():
    unique_countries = mydata.groupby('Match ID')['Winner'].unique().value_counts()
    top_10_countries = unique_countries.head(10)

    # Convert country names to strings
    top_10_countries.index = top_10_countries.index.map(lambda x: ', '.join(x))

    # Define a dictionary mapping countries to their respective colors
    country_colors = {
        'India': 'blue',
        'Australia': 'yellow',
        'England': '#ADD8E6',
        'Pakistan': 'green',
        'New Zealand' : 'black',
        'South Africa' : '#90EE90',
        'Sri Lanka': 'blue',
        'West Indies': 'red',
        'Afghanistan' : '#ADD8F9',
        'Ireland' : '#90EE90'
        # Add more countries and their colors as needed
    }

    # Retrieve the colors for the top 10 countries
    colors = [country_colors.get(country, 'gray') for country in top_10_countries.index]

    # Create Plotly bar chart
    fig = go.Figure(data=[go.Bar(x=top_10_countries.index, y=top_10_countries.values, marker=dict(color=colors))])
    fig.update_layout(title='Top 10 Countries of Most Winnings',
                      xaxis_title='Country',
                      yaxis_title='Number of Matches Won')
    st.plotly_chart(fig)

 

# Function to plot bar chart for matches with target score > 200
def chasedScuccessfully():
    high_target_matches = mydata[mydata['Target Score'] > 200]
    unique_matches3 = high_target_matches.groupby('Match ID')['Chased Successfully'].sum()
    won = (unique_matches3 > 0).sum()
    lost = (unique_matches3 == 0).sum()

    # Create Plotly bar chart
    fig = go.Figure(data=[go.Bar(x=['Successfully Chased', 'Unsuccessfully Chased'], y=[won, lost], marker=dict(color=['green', 'red']))])
    fig.update_layout(title='Matches Result with Target Score > 200',
                      xaxis_title='Result',
                      yaxis_title='Number of Matches')
    st.plotly_chart(fig)

# Function to plot bar chart for most successful chased grounds
def mostSuccessfullChasedGrounds():
    venue_successful_chases = mydata[mydata['Chased Successfully'] == 1].groupby('Venue')['Match ID'].nunique()
    top_10_venues = venue_successful_chases.nlargest(10)

    shortened_venues = [venue[:15] + '...' if len(venue) > 15 else venue for venue in top_10_venues.index]

    # Create Plotly bar chart
    fig = go.Figure(data=[go.Bar(x=shortened_venues, y=top_10_venues.values, marker=dict(color=sns.color_palette('Set2', n_colors=len(top_10_venues))))])
    fig.update_layout(title='Successful Chases by Venue',
                      xaxis_title='Venue',
                      yaxis_title='Number of Successful Chases')
    st.plotly_chart(fig)

# Calling functions
mostSuccessfullChasedGrounds()
top10winningCountries()
batFirstandSecondWins()
chasedScuccessfully()

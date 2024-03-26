import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

mydata = pd.read_csv('D:\\Big Data Analytics\\Pythonpractice\\pandas\\Cleaned_ball_by_ball.csv')
st.title("Ball By Ball IT20 Data")
st.header("Cricket")

st.dataframe(mydata)


with st.sidebar:
    st.image('t20.png', width=150,)
    st.title('T20 Cricket Data')



# all_matches = mydata['Match ID'].count



# unique_countries = mydata['Winner'].unique()


# winning_matches_count = mydata['Winner'].value_counts()
# top_5_countries = winning_matches_count.head()


# plot = top_5_countries.plot(kind='bar', color=['green', 'blue', 'black', "green", "yellow"])
# plt.title('Top 5 Countries of Most Winnings')
# plt.xlabel('Country')
# plt.ylabel('Number of Matches Won')

# st.header("Top 5 Most Winning Countries")

# st.pyplot(plot.figure)

# st.header("Bat First Vs Bat Second")

# bat_first_wins = mydata[(mydata['Bat First'] == mydata['Winner']) & (mydata['Chased Successfully'] == 0)]

# bat_second_wins = mydata[(mydata['Bat Second'] == mydata['Winner']) & (mydata['Chased Successfully'] == 1)]

# bat_first_wins_count = len(bat_first_wins)
# bat_second_wins_count = len(bat_second_wins)


# categories = ['Batting First', 'Batting Second']
# wins_count = [bat_first_wins_count, bat_second_wins_count]

# plot1 = plt.bar(categories, wins_count, color=['blue', 'green'])
# plt.title('Wins by Batting First vs. Batting Second')
# plt.xlabel('Batting Team')
# plt.ylabel('Number of Wins')
# st.bar_chart(plot1.datavalues)

def batFirstandSecondWins():
    unique_matches1 = mydata.drop_duplicates(subset='Match ID')

    bat_first_wins = unique_matches1[unique_matches1['Bat First'] == unique_matches1['Winner']].shape[0]

    bat_second_wins = unique_matches1[unique_matches1['Bat Second'] == unique_matches1['Winner']].shape[0]


    categories = ['Batting First', 'Batting Second']
    wins_count = [bat_first_wins, bat_second_wins]

    plot1 = plt.bar(categories, wins_count, color=['blue', 'green'])
    plt.title('Wins by Batting First vs. Batting Second')
    plt.xlabel('Batting Team')
    plt.ylabel('Number of Wins')
    st.bar_chart(plot1.datavalues)
    # plt.show()

def top10grounds():
    
   unique_matches2 = mydata.drop_duplicates(subset='Match ID')

   grounds = unique_matches2.groupby('Match ID')['Venue'].unique().value_counts()
   top_10_grounds = grounds.head(10)

   plot2 = top_10_grounds.plot(kind='bar', color=['green', 'blue', 'black', "#90EE90", "yellow", "#ADD8E6", "blue", "brown", "blue", "#90EE90"])
   plt.title('Top 10 Grounds of Most Matches')
   plt.xlabel('Grounds')
   plt.ylabel('Number of Matches')
#    plt.show()  
   st.pyplot(fig=plot2.figure)  

def top10winningCountries():
    unique_countries = mydata.groupby('Match ID')['Winner'].unique().value_counts()

    top_10_countries = unique_countries.head(10)


    plot3 = top_10_countries.plot(kind='bar', color=['green', 'blue', 'black', "#90EE90", "yellow", "#ADD8E6", "blue", "brown", "blue", "#90EE90"])
    plt.title('Top 10 Countries of Most Winnings')
    plt.xlabel('Country')
    plt.ylabel('Number of Matches Won')
    # plt.show()
    st.pyplot(fig=plot3.figure) 

def chasedScuccessfully():
   high_target_matches = mydata[mydata['Target Score'] > 200]

   unique_matches3 = high_target_matches.groupby('Match ID')['Chased Successfully'].sum()
   won = (unique_matches3 > 0).sum()
   lost = (unique_matches3 == 0).sum()

   plot4 = plt.bar(['Successfully Chased', 'UnSuccessfully Chased'], [won, lost], color=['green', 'red'])
   plt.title('Matches Result with Target Score > 200')
   plt.ylabel('Number of Matches')
#    plt.show()
   st.bar_chart(plot4.datavalues)

top10winningCountries()
batFirstandSecondWins()
# top10grounds()
chasedScuccessfully()   



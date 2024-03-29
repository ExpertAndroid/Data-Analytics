import streamlit as st
# import numpy as np
# import pandas as pd
# import matplotlib.pylab as plt
# import seaborn as sns

# mydata = pd.read_csv('D:\\Big Data Analytics\\Pythonpractice\\pandas\\Cleaned_ball_by_ball.csv')
# st.title("Ball By Ball IT20 Data")
# st.header("Cricket")
st.write('Hello Streamlit')
# unique_matches = ''
# st.dataframe(mydata)


# with st.sidebar:
#     st.image('t20.png', width=150,)
#     st.title('T20 Cricket Data')


# def batFirstandSecondWins():
#     unique_matches = mydata.drop_duplicates(subset='Match ID')

#     bat_first_wins = unique_matches[unique_matches['Bat First'] == unique_matches['Winner']].shape[0]

#     bat_second_wins = unique_matches[unique_matches['Bat Second'] == unique_matches['Winner']].shape[0]


#     categories = ['Batting First', 'Batting Second']
#     wins_count = [bat_first_wins, bat_second_wins]

#     fig, ax = plt.subplots()
#     ax.bar(categories , wins_count, color=['blue', 'yellow'])
#     ax.set_title('Wins by Batting First vs. Batting Second')
#     ax.set_ylabel('Number of Wins')
#     ax.set_xlabel('Batting Team')
#     st.pyplot(fig)

# def top10winningCountries():
#     unique_countries = mydata.groupby('Match ID')['Winner'].unique().value_counts()

#     top_10_countries = unique_countries.head(10)


#     plot3 = top_10_countries.plot(kind='bar', color=['green', 'blue', 'black', "#90EE90", "yellow", "#ADD8E6", "blue", "brown", "blue", "#90EE90"])
#     plt.title('Top 10 Countries of Most Winnings')
#     plt.xlabel('Country')
#     plt.ylabel('Number of Matches Won')
#     # plt.show()
#     st.pyplot(fig=plot3.figure) 

# def chasedScuccessfully():
#     high_target_matches = mydata[mydata['Target Score'] > 200]

#     unique_matches3 = high_target_matches.groupby('Match ID')['Chased Successfully'].sum()
#     won = (unique_matches3 > 0).sum()
#     lost = (unique_matches3 == 0).sum()

#     fig, ax = plt.subplots()
#     ax.bar(['Successfully Chased', 'Unsuccessfully Chased'], [won, lost], color=['green', 'red'])
#     ax.set_title('Matches Result with Target Score > 200')
#     ax.set_ylabel('Number of Matches')
#     ax.set_xlabel('Result')
#     st.pyplot(fig)

# def mostSuccessfullChasedGrounds():
#    unique_matches = mydata.drop_duplicates(subset='Match ID')

#    unique_data = unique_matches.groupby('Match ID').agg({
#     "Chased Successfully" : "first",
#     "Venue" : "first"
#    }).reset_index()

#    num_words_to_keep = 2 
#    unique_data['Abbreviated Ground'] = unique_data['Venue'].str.split().str.slice(0, num_words_to_keep).str.join(' ')

#    chased_data = unique_data[unique_data['Chased Successfully'] == 1]

#    chased_score_grounds = chased_data['Abbreviated Ground'].value_counts().head(10)

#    colors = ['green', 'yellow', 'blue', 'skyblue', 'red']

#    plot4 = chased_score_grounds.plot(kind='bar', color=colors)

#    # plot4 = sns.barplot(x=chased_score_grounds.index, y=chased_score_grounds.values, palette=colors)
#    plt.title('Top 10 Grounds with Most Successful Chases')
#    plt.xlabel('Ground')
#    plt.ylabel('Number of Successful Chases')
#    plt.xticks(rotation=90)
#    st.pyplot(fig=plot4.figure)  

# # mostSuccessfullChasedGrounds()
# # top10winningCountries()
# # batFirstandSecondWins()
# # chasedScuccessfully()   



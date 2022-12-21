# ---------------------Imports-------------------------------
from PIL import Image
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------Data-------------------------------
loc='D:\\MIT\\Mini project\\IPL\\IPL_DATA\\ipl_male_csv2\\IPL_DATA.csv'
loc1='D:\\MIT\\Mini project\\IPL\Project 1\\matches.csv'
data=pd.read_csv(loc,sep=',')
matches=pd.read_csv(loc1,sep=',')

# ----------------------Image-----------------------------------


image=Image.open('D:\MIT\Mini project\IPL\Project 1\images\IPL-Logo-PNG.jpg')


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.image(image,use_column_width=True)
st.write(""" ## “Every game you play, they will record your good performance, your bad performance, you played against which bowler, you scored against which team and which bowler, and the whole data will easily show you that you are good against Pakistan but you’re not good performed against Bangladesh, you’re good against South Africa but you’re not good against England. In 2003 when our computer analytics guy come in and he showed me videos and different kinds of data analysis, I got amazed!!!""")
"""
***

# Welcome to our prediction
"""





options=st.selectbox('Please Select',['Descripti    ve Analysis','Predictive Analysis'])
venue_ser = data['venue'].value_counts()
venue_df = pd.DataFrame(columns=['venue', 'matches'])
for items in venue_ser.iteritems():
    temp_df = pd.DataFrame({
        'venue':[items[0]],
        'matches':[items[1]]
    })
    venue_df = venue_df.append(temp_df, ignore_index=True)

def venues():
    
    st.subheader('The venue that hosted the maximum number of matches')
   
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(x='matches', y='venue', data=venue_df);
    st.pyplot(fig)
    max=venue_df['matches'][0]
    team=venue_df['venue'][0]

    st.write(""" ### The maximum number of match hosted by a team is""",max)
    st.write(""" ### Hosted by""",team)
    """***"""

team_wins_ser = matches['winner'].value_counts()
team_wins_df = pd.DataFrame(columns=["team", "wins"])
for items in team_wins_ser.iteritems():
    temp_df1 = pd.DataFrame({
        'team':[items[0]],
        'wins':[items[1]]
    })
    team_wins_df = team_wins_df.append(temp_df1, ignore_index=True)
def succ_team():
    st.subheader('The most successfull Team')

    fig = plt.figure(figsize=(10, 4))
    sns.barplot(x='wins', y='team', data=team_wins_df, palette='Paired');
    st.pyplot(fig)
    succ=team_wins_df['team'][0]
    wins=team_wins_df['wins'][0]
    

    st.write(""" ### The most successfull Team is""",succ)
    st.write(""" ### With""",wins,"wins")
    """***"""


mvp_ser = matches['player_of_match'].value_counts()
mvp_ten_df = pd.DataFrame(columns=["player", "wins"])
count = 0
for items in mvp_ser.iteritems():
    if count>9:
        break
    else:
        temp_df2 = pd.DataFrame({
            'player':[items[0]],
            'wins':[items[1]]
        })
        mvp_ten_df = mvp_ten_df.append(temp_df2, ignore_index=True)
        count += 1  
def valuable_player():
    plt.title("Top Ten IPL Players")
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(x='wins', y='player', data=mvp_ten_df, palette='Paired');
    st.pyplot(fig)
    valuable_player=mvp_ten_df['player'][0]
    wins=mvp_ten_df['wins'][0]
    

    st.write(""" ### The most most valuable player is""",valuable_player)
    st.write(""" ### With""",wins,"wins of player of the match")
    st.write(""" ### Six Indian players have figured in the top ten IPL players list """)
    """***"""

toss_ser = matches['toss_winner'].value_counts()
toss_df = pd.DataFrame(columns=["team", "wins"])

for items in toss_ser.iteritems():
    temp_df3 = pd.DataFrame({
        'team':[items[0]],
        'wins':[items[1]]
    })
    toss_df = toss_df.append(temp_df3, ignore_index=True)
def toss_win():
    fig = plt.figure(figsize=(10, 4))
    plt.title("How IPL Teams fared in toss?")
    sns.barplot(x='wins', y='team', data=toss_df, palette='Paired');
    st.pyplot(fig)
    toss_win=toss_df['team'][0]
    wins=toss_df['wins'][0]

    st.write(""" ###  The most toss is won by""",toss_win)
    st.write(""" ### With""",wins,"wins")
    st.write(""" ### All the top teams in IPL are successful in winning the toss as well. """)
    """***"""





def major_victories():
    defend_vict_ser = matches['win_by_runs'].value_counts()
    defend_vict_ser.sort_values(ascending=True)
    st.table(defend_vict_ser.head())

    st.write("""# What are the major victories in IPL? Is it better to defend or chase in IPL?""")  
    st.markdown("""### 1)  Of the 756 IPL matches played from 2008 to 2020, 419 matches were won chasing the target. Hence, more victories were registered by teams chasing a total(batting second) than defending the total.""")
      
    st.write("""### 2)  When defending a total, the biggest victory was by 146 runs""")  
    st.write("""### 3)   Of the 756 IPL matches played from 2008 to 2019, 350 matches were won defending the total.""")  
    st.write("""### 4)   When chasing a target, the biggest victory was by 10 wickets(without losing any wickets and there are 11 such instances).""")  
    
    chasing_vict_df = pd.DataFrame(columns=['victory_margin', 'instances'])
    chasing_vict_ser = matches['win_by_wickets'].value_counts()

    for items in chasing_vict_ser.iteritems():    
        temp_df7 = pd.DataFrame({
        'victory_margin': [items[0]],
        'instances': [items[1]]
    })
        chasing_vict_df = chasing_vict_df.append(temp_df7, ignore_index=True)
    chasing_vict_df2 = chasing_vict_df.drop([0]) 
    
    plt.title("The IPL victories in numbers when chasing a total")
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(x='victory_margin', y='instances', data=chasing_vict_df2);
    st.pyplot(fig)






def toss_win_prob():
    win_count=0
    st.write(""" # Does winning the toss has any advantage?""")
    for index, value in matches.iterrows():
        if(value['toss_winner']==value['winner']):

            win_count += 1
    st.write("""## The number of times the team winning toss have won:""", win_count)
    prob = win_count/len(matches)
    st.subheader('The probability of winning if won the toss: {:.2f}' .format(prob))
    st.write(""" #### The probability of winning when the team had won the toss is 52%""") 
    
    













    


def Descriptive():
    venues()
    succ_team()
    valuable_player()
    toss_win()
    major_victories()
    toss_win_prob()












import pickle


def Predictive():
    st.write("Predictive")
    teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']
    cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']
    pipe = pickle.load(open('pipe.pkl','rb'))
    st.title('IPL Win Predictor')
    col1, col2 = st.columns(2)
    with col1:
        batting_team = st.selectbox('Select the batting team',sorted(teams))
    with col2:
        bowling_team = st.selectbox('Select the bowling team',sorted(teams))
    selected_city = st.selectbox('Select host city',sorted(cities))
    target = st.number_input('Target')
    col3,col4,col5 = st.columns(3)
    with col3:
        score = st.number_input('Score')
    with col4:
        overs = st.number_input('Overs completed')
    with col5:
        wickets = st.number_input('Wickets out')
        if st.button('Predict Probability'):
            runs_left = target - score
            balls_left = 120 - (overs*6)
            wickets = 10 - wickets
            crr = score/overs
            rrr = (runs_left*6)/balls_left
            input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
            result = pipe.predict_proba(input_df)
            loss = result[0][0]
            win = result[0][1]
            st.header(batting_team + "- " + str(round(win*100)) + "%")
            st.header(bowling_team + "- " + str(round(loss*100)) + "%")




    

if options=='Descriptive Analysis':
    
    Descriptive()
else:
    Predictive()










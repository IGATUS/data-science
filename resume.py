import streamlit as st 
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
#creating containers for the various sections
header=st.beta_container()
dataset=st.beta_container()
features=st.beta_container()
model_training=st.beta_container()
st.markdown("""
<style>
    .main{
        background-color:#D5F5F5;
    }
</style>
""",
unsafe_allow_html=True)
@st.cache
def get_data(filename):
    taxi_data=pd.read_csv(filename)
    return taxi_data
#to write something inside the container say the header container we have
with header:
    st.title('Welcome to my awesome data science project')
    st.text('This Project makes use of the Restaurant Business Ranking Dataset from Kaggle.....')

with dataset:
    st.header('Restaurant Business Rankings Dataset')
    st.text('I found this dataset on www.kaggle.com')
    taxi_data=get_data('independence.csv')
    st.write(taxi_data.head())
    st.subheader('Average Check')
    Average=pd.DataFrame(taxi_data['Average Check'].value_counts()).head(50)
    st.bar_chart(Average)
with features:
    st.header('The features I created')
    st.markdown('* **first feature:** I created this feature because of this....I calculated it using this logic...')
    st.markdown('* **second feature:** I created this feature because of this....I calculated it using this logic...')
with model_training:
    st.header('Time to train the model')
    st.text('Here you go to choose the hyperparameters of the model and see how the performance changes')
    sel_col,disp_col=st.beta_columns(2) #here you set the number of columns you want
    max_depth=sel_col.slider('what should be the max_dept of the model?',min_value=10,max_value=100,value=20,step=10)
    n_estimators=sel_col.selectbox('How many trees should be there?',options=[100,200,300,'No limit'],index=0)
    sel_col.text('Here is a list of features in my data:')
    sel_col.write(taxi_data.columns)
    input_features=sel_col.text_input('which feature should be used as the input feature?','Average Check')
    if n_estimators=='No limit':
        regr=RandomForestRegressor(max_depth=max_depth)
    else:
        regr=RandomForestRegressor(max_depth=max_depth,n_estimators=n_estimators)
    x=taxi_data[[input_features]]
    y=taxi_data[['Meals Served']]
    regr.fit(x,y)
    prediction=regr.predict(y)
    disp_col.subheader('Mean absolute error of the model is:')
    disp_col.write(mean_absolute_error(y,prediction))
    disp_col.subheader('Mean squared error of the model is:')
    disp_col.write(mean_squared_error(y,prediction))
    disp_col.subheader('R squared score of the model is:')
    disp_col.write(r2_score(y,prediction))
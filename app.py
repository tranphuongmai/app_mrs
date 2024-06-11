# Importing the package
import streamlit as st

# Importing the module
from eda import df1, df2, df3, df4, df5, df6, df7, preprocessing
from ml import get_recom
from cv import about_me

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
     
     
     menu = ["Home", "Data Exploration And Preprocessing",  "Movie Analysis", 
             "Movie Recommendation System", "About Me"]

     choice = st.sidebar.selectbox("Menu", menu)

     if choice == "Home":
          st.title("Welcome to my :blue[porfolio]!")
          st.title("My name is Mai Tran, a Data Analyst.")
          st.text("""
         This is a project I implemented with my classmate Halil Ibrahim at Wild Code 
         School, where i learnt to become a data analyst. Our target is to create the 
         MRF - Movie Recommendation System which will recommend similar titles to user's 
         given title according to Genres, popularity, Duration, etc. 
                  
         We started with 10.73 millions titles that we explored to understand the content
         of all the given datasets. We filtered to down-size into a dataset of 450k titles.
         We then clean and remove missing values to get a final one with 430k titles.         
                  """)
          st.image("asset/home_page_filtering.png")
          st.text("/n")
          st.text("""

         About the creation of the recommendation system, we first convert all the text 
         values into numeric values by using LabelEncoder for column 'Type' and method 
         which converted each category of column 'Genres' into a label with binary values.

         Since this is a non-supervised model, we passed the step 'model traing' by going 
         directly to the prediction of NearestNeighbors, an unsupervised learner for 
         implementing neighbor searches.

         We then tried to change the hyperparameter to get our model better but we dont' see
         much improvement so we sorted values by setting the weight on Votes and Genres.
                  """)
          st.image("asset/home2.png")

     elif choice == "Data Exploration And Preprocessing":
          
          submenu = ["Exploration", "Preprocessing"]
          choice_sub = st.sidebar.selectbox("Drop down to choose", submenu)
          
          if choice_sub == "Exploration":
              st.title(":blue[DATA EXPLORATION]")
              st.text(""" 
               In this project, we worked on 7 mass datasets of more than 10 millions
               titles about movies, tvshow, videos, etc.  Dealing with files that are too 
               large in size, we coud not import all the datasets at the same time, there 
               was no other option than mining 1 or 2 dataset each time.
                      
               In addition, according to our client's expectation, we had to create this
               system for a particular target of users in a sparsely populated place where 
               elderly population occupates almost 60%.
""")
               
              if st.sidebar.button("DF1"):
                 st.header("The dataset 'title.rating.tsv'")
                 df1()
              if st.sidebar.button("DF2"):
                 st.header("The dataset 'title.akas.tsv'")
                 df2()
              if st.sidebar.button("DF3"):
                 st.header("This is df3")
                 df3()
              if st.sidebar.button("DF4"):
                 st.header("This is df4")
                 df4()
              if st.sidebar.button("DF5"):
                 st.header("This is df5")
                 df5()            
              if st.sidebar.button("DF6"):
                 st.header("This is df6")
                 df6()
              if st.sidebar.button("DF7"):
                 st.header("This is df7")
                 df7()



          elif choice_sub == "Preprocessing":
               st.title(":blue[DATA EXPLORATION]")
               st.text("""
               After combining and filtering the KPI we have a dataframe with around 450k titles.
               Our filtering standard is only titles with average ratings above 5 and  only titles
               with type related to short films.
""")       
               preprocessing()

     elif choice == "Movie Analysis":
          st.title(":blue[MOVIE ANALYSIS]")
          st.header("In the section Dataviz, we chose to visualize all the KPI related to our dataset by using PowerBI, a very strong and smart tool for Data Visualization.")
          st.text("""
               We created 3 dashboards containing all the filters with the idea of a filter 
               funnel, which starts with the released years (decade) then title categories then 
               genre categories. 
               
               In the first dashboard, we want to presentate about the evolution of Duration, 
               and Creation of all the titles according to each category. Then we want to point 
               out the correlation between Votes and Average Ratings in order to co to the 
               conclusion that 'movies with high votes often have good ratings'.
""")       
          st.image("asset/PBI1.png")

          st.text("/n")
          st.text("""
               Second and third dashboard will show the imponent titles and production staffs 
               accoring to title categories, staff categories and released year. There is also 
               a filter for genre categories.
""")
          st.image("asset/PBI2.png")
          st.image("asset/PBI3.png")

     elif choice == "Movie Recommendation System":
          get_recom()
     else:
          st.title("Hi👋! I'm Mai.")
          st.header("My favourite tools are Python for mass data analysis and PowerBI for visualization.")
          st.write("---")
          about_me()
         
          
          
         
               



main()
         

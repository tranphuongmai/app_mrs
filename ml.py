# importing package

import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors


def get_recom():
    st.title("Now, it's time for our favorite movies.")

    st.header("Please enter a title")

    title = st.text_input("Movie title", "The Avengers")
    st.write("The current movie title is", title)

    
    df_return = pd.read_csv(r"data/return_movies.csv")
   
    df_return.insert(0, 'Title', df_return.pop('Title'))

    df_return = df_return.sort_values(['Type of title', 'Released year',                         
                         'Average Ratings', 'Duration', 'Votes'], 
                        ascending=[
                            True, False,                     
                            True, False, True
                            ] )
    
   # Copy and nomalize all variables for model
    df = df_return.copy()
   

    # Convert genres to list of strings
    df['Genres'] = df['Genres'].str.split(',')

    # Create numeric label for each category of genres
    genres_cat = ['Action', 'Adventure', 'Animation', 'Biography','Comedy', 
                 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 
                 'Horror','Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
                 'Music', 'History', 'War', 'Western', 'Musical']

    for i in genres_cat:
        df[i] = df['Genres'].apply(lambda x:1 if i in x else 0)


    # Create numeric label for each category of titleType
    label_encoder = LabelEncoder()
    df['Type of title'] = label_encoder.fit_transform(df['Type of title'])

    # Drop non-selected columns
    df = df.drop(columns=['Genres'], axis = 1)
    # Lower the title's names
    df['Title']= df['Title'].apply(lambda x: x.lower())

    # Change position of all variables
    df = df[[
                 'Title', 
                  'Type of title',
                 'Action', 'Adventure', 'Animation', 'Biography','Comedy', 
                 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 
                 'Horror','Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
                 'Music', 'History', 'War', 'Western', 'Musical',
                 'Votes', 'Average Ratings', 'Adult title', 'Released year', 'Duration',
                 
                 ]]



    # Set title as index
    df = df.set_index('Title')
    
    df = df.sort_values(['Type of title', 'Released year',                         
                         'Average Ratings', 'Duration', 'Votes'], 
                        ascending=[
                            True, False,                     
                            True, False, True
                            ] )
    
    
    # Initialize variable X
    X = df.select_dtypes("number")

    # Standardize features of X
    scaler = StandardScaler()
    scaler.fit(X)

    X_scaled = pd.DataFrame(scaler.transform(X), index=X.index, columns=X.columns)

    
    # Lower title's name
    title = title.lower()
    
    # To identify the searching film
    # Scale searching value
    input_title_scaled = X_scaled.loc[title].to_frame().T
    
    # Show the KPI of serching film to compare with returned values
    #input_title = X.loc[title].to_frame().T
    


    # Fit model
    modelKNN = NearestNeighbors(n_neighbors=5)
    modelKNN.fit(X_scaled)

    # Identify distance and indeices of similar films
    neigh_dist, neigh_film = modelKNN.kneighbors(input_title_scaled, n_neighbors=11)
    film_similar = neigh_film[0][1:]
    user_film = neigh_film[0][:1]
    
    try:
       st.markdown("Your favorite title is:")
       st.write(df_return.iloc[user_film]) 
       st.markdown("We would like to recommend you 10 similar titles below. Hope you will enjoy them!")
       st.write(df_return.iloc[film_similar])
    except(KeyError, IndexError):
       st.write("Sorry, that title does not exist. Please try another.")

   

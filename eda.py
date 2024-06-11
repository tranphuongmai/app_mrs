# importing package
import streamlit as st
import pandas as pd

def df1():
    df1 = pd.read_csv(r"data/title.ratings.csv")
    st.subheader("This dataset is about the average ratings and the numbers of votes of  id which represents each title's type.")
    st.dataframe(df1)
    
    st.text("\n") 
    st.text("""
    First, let's look at the column 'numVotes', statistically we notice that 75% of 
    the dataset is occupied by the values below 250 numbers of vote which may give 
    the impression that there are 75% of movies and tvshows are very little popular. 
    If we visualize the distribution of each movie's frequency, we can not see much 
    because of a massive distribution in the interval 5 and less than 500 numbers of
    votes while the maximum number is 2.888.676.""")
    st.image("asset/exploration_rating_numvotes.png")

    st.text("\n") 
    st.text("""
    Then, we head to the statistics of the 'averageRating', we can say that most of 
    data distributes in the interval between 5 and 9, but its 9 deciles point out 
    that 90% of the dataset have a rate note higher than 5. Maybe we can choose this 
    condition to remove some outliers of the dataset.""")
    st.image("asset/exploration_rating_rating.png")

    st.text("\n") 
    st.text("""
    Here, we tried to look for a correlation between  Votes and number of votes and 
    we see that there is polynomial regression which is very light but because of 
    the massive outliers we can not point it out clearly. However, we   can observe 
    that the films which have a high number of votes will tend to have high score. 
    Because the bad notes which are less than 5 occurence in just the first quantile 
    of the dataset, we decide to remove this partie to keep only films with notes 
    higher than 5.""")
    st.image("asset/exploration_rating_numvotesRate.png")
    
    

def df2():
    df2 = pd.read_csv(r"data/title.akas.csv")
    st.subheader("This dataset provides information about linguistic versions of titles. There are 48.134.030 entries.")
    st.dataframe(df2)

    st.text("\n") 
    st.text("""
    We normalized the values of all the columns and projected them into bar chart to
    see which columns are impossible to be used. Apparently, we only have 4 columns 
    which could be useful, so we tried to count the frequency of each 'titleId' for
    the 'numLanguages' and we noticed that 50% titles of the dataset have less than 
    20 linguistic versions including the original version.""")
    st.image("asset/exploration_akas_missingvalues.png")
    
    st.text("\n")
    st.text("""
    We projected the distribution of total languages into a line chart and we see that 
    most of the titles will have in average 2 to 10 languages, but there are also 
    exceptional cases which have up to 250 languages.
            """)
    st.image("asset/exploration_akas_total.png")

    st.text(" \n")
    st.text("""
    Then, we tried to identify the original language in the hope that we can use this
    feature, but the result is 100% missing. So we decided not to use this dataset.""")
    st.image("asset/exploration_akas_missing_regional.png")

    
def df3():
    df3 = pd.read_csv(r"data/title.crew.csv")
    st.subheader("This dataset is condisered as a dimension table which contains 3  ID columns of title, director and writer.  ")
    st.dataframe(df3)

    st.text("\n ")

    st.text("""
    We projected the KPI into a bar chart to see if there are any films had many 
    directors and writers. If it's true, what is the maximum number of them?
            
    We found many titles having many directors and writers, more than what we had 
    expected. We supposed that they must belong to the category 'Series'.
                        """)
    st.image("asset/exploration_crew_columns.png")

    st.text(" \n")
    st.text("""
    We want to check there is how many percent of titles which don't have a director
    or a writer. Then, we wonder why?? Because there are many self-made video/short 
    which don't mention writer or director.""")
    col1, col2 = st.columns(2)
    with col1:
        st.image("asset/exploration_crew_direct.png")
    with col2:    
        st.image("asset/exploration_crew_writer.png")

    st.text("\n ")
    st.text("""
    We will not use this dataset because we can get Directors and Writers of each title
    by using anothe one. It's the next df.""")
   

def df4():
    df4 = pd.read_csv(r"data/title.episode.csv")
    st.subheader("This dataset provides infomation about all the types 'Series' and their's episodes. So we can see one ID of title and one of sub-title (episode).")
    st.dataframe(df4)

    st.text("\n ")
     
    st.text("""
    Have a look at the distribution of Season numbers. We noticed that there are 
    something which are not normal here. Series with almost 1000 or 2000 seasons? 
            """)
    st.image("asset/exploration_episode_boxplot.png")

    st.text("\n ")
    st.text("""
    We searched for those unusual series and we found out that there is a way of 
    naming the series by using the year number, or we can say that it has no relation
    to the order of the series.       
            """)
    st.image("asset/exploration_episode_weird1.png")
    st.image("asset/exploration_episode_weird2.png")

    
    st.text("\n ")
    st.text("""
    Then we checked the maximum total episodes of the series, we found out that there 
    is a massif occurence of this tytpe of title in the whole dataset. We will consider
    if we will keep this titles's type for our recommendation system or not.
            """)
    st.image("asset/exploration_episode_top1.png")
    st.image("asset/exploration_episode_top2.png")

    


def df5():
    df5 = pd.read_csv(r"data/title.basics.csv")
    st.subheader("This dataset carries all the features important of more than 10 millions  titles as type of title, title's name, genres, etc.")
    st.dataframe(df5)
     
    st.text("\n")
     
    st.text("""
    After overviewing all the columns's labels, we consider this one will be our 
    main dataset. Except of the column 'endYear' with almost 100% missing, the rest
    is usful for our system. But we can not keep all 10 millions titles so we need 
    to select. 
            
    First, we projected all the categories of column 'titleType' to check theirs 
    ditribution. We oserved that 'tvEpisode' which is a sub-category of type 'series' 
    is taking up the majority of this dataset. As we considered that we want to have
    only short movie in our system, so we decied to remove this type of titles.       
            """)
    st.image("asset/exploration_basic_type.png")

    st.text("\n ")
    st.text("""
    Have a look at all the types of titles after removing the 'series'. We are going to
    compare the types 'video' and 'short' to see what is the difference between them.
            """)
    st.image("asset/exploration_basic_type2.png")

    st.text("\n ")
    st.text("""
    We can conclude that the types 'short' were made as a small project when the 
    duration is as short as 1-4 minutes but there are always a scenario behind. 
    Ortherwise, there are some long videos, one with duration up to 35000 minutes, 
    but there isn't a concrete content in these types.
            
    We decided to remove all the titles belonging to 'video'.       
            """)
    col1, col2 = st.columns(2)
    with col1:
        st.image("asset/exploration_basic_short.png")
    with col2:    
        st.image("asset/exploration_basic_video.png")
    


def df6():
    df6 = pd.read_csv(r"data/title.principals.csv")
    st.subheader("This dataset contains information of all the production staffs of each title.")
    st.dataframe(df6)
     
    st.text("\n ")
     
    st.text("""
    We projected to see distribution of each category. Aparently, actor and actress are
    leading the list, followed by the category 'self', those who made their own movies.
            
    This dataset will be merge with another one to get name of each person then we will
    combine it to the main dataset to get a fully informative dataset.
            """)
    st.image("asset/exploration_principalc_1.png")

    st.text("\n ")
    st.text("""
    Let's have a look at people who contributed the most to arts industry but we might 
    never heard about their name.""")
    st.image("asset/exploration_principalc_2.png")
    


def df7():
    df7 = pd.read_csv(r"data/name.basics.csv")
    st.subheader("This dataset is about all of the people who dedicated to the arts industry, including philosophies already passed away as writers.")
    st.dataframe(df7)
     
    st.text("\n ")
     
    st.text("""
    Check the proportion of missing values in the dataset, we consider fast that we 
    can only use the column 'primaryName'-people's  name and 'nconst'-their ID to 
    merge with another dataset for details.
            """)
    st.image("asset/exploration_df7.png")


## Preprocessing
def preprocessing():
    st.header("Overviewing filtered dataset")
    st.markdown("This is our main dataset which is merged by 2 datasets.")
    tbr_staff =  pd.read_csv(r"data/basic_rating.csv")
    st.dataframe(tbr_staff)
    
    # Check missing values of each column
    st.markdown("Then, we check missing values by normalize the scale to a percentage. ")
    st.markdown("We decide to remove the column 'endYear' due to 100% of missing.")
    st.markdown("It seems like we also have missing values in columns 'genres' and 'runtimeMinutes' to handle. Let's do it together.")
    st.image("asset/prepocessing3.png")


    st.header("Try to fill missing values by using the additional dataset 'tmdb_full'")
    st.markdown("Luckily, we have an additional dataset from website tmdb with more than 300k titles, let's see if we can take advantage of this dataset or not. Now overview of the dataset 'tmdb_full.csv'.")
   
    tmbd_before = pd.read_csv(r"data/tmdb_full.csv")
    st.dataframe(tmbd_before)

    st.markdown("The column 'genres' was setting as string so we can not work on it, need to use a module to convert it into correct type 'list of string'. Then we convert convert type of other columns to get same format as our main dataset.")
    
    
    st.markdown("Take a look at our efforts. Well done!")
    st.image("asset/prepocessing4.png")


    st.markdown("Create a dataframe with only null values of column 'genres' from main dataframe to filter missing values then we will use concat() to combine them together")
    
    
    st.markdown("Hooray! We got 7596 values from using the additional dataframe. This is the result. But we wtill have many problems with NaN of columns 'genres' and 'runtimeMinute'.")
    st.image("asset/prepocessing5.png")
 

    st.markdown("Let's have a look at the NaN distribution of each type of titles.")
    st.image("asset/prepocessing6.png")

    
    st.header("Check NaN of 'genres' of each 'titleType'")
    st.markdown("We cut the data of each titleType into two: one has only null values, one without null value and we will analyze each of them to find the solution for filling NaN.")
    
    st.write(" ")
    st.subheader("Question:")
    st.markdown("1.'tvSpecial' contains the genres more like show, talk-show, reality-show, documentary. Do we need to remove this type of title which is not related to our target, it's about 10.000 titles??")
    st.markdown("2.'tvMovie' also has genres show, game-show. What is the solution? We keep these genres? Remove them?")
    st.markdown("3. Also for Movie: Talk-Show, News, TV-Reality. Are they very important in our dataset?")
    st.markdown("We tried to understand the logic of each genres in this titleType 'tvSpecial' So we have type of genres similar to movie and tvmovie's ones. But, if we try to search keyword from primaryTitle, we will see the logic is different from movie and tvmovie's ones. For exemple, With the typ of genres 'Comedy', it's about a comedy talked-Show in 'tvSpecial' while it's a comedy movie in 'tvMovie' and 'movie'.")

    title = pd.DataFrame({"value": ["short", "movie", "tvMovie", "tvShort"]})
    st.markdown("So, now we only have 4 types of titles in out dataset")
    st.write(title)



    st.header("Replace NaN of 'runtimeMinutes' by using median of each 'titleType'")
    st.markdown("Let's project values of this column into a boxplot to analyse then choose a good method for this task.")
    st.markdown("In order to observe better the distribution of each type, we removed all the outliers above 800 minutes.")
    st.markdown("Because the duration of each type is different, so we can not fill NaN by a general median of our dataset.")
    
    st.image("asset/prepocessing1.png")


    st.subheader("Method:")
    st.markdown("We will split the dataset into 4 according to titles's type then we calculate the median of all values which are below  Q3+1.5*IQR.")
  
    
    startYear = [1942, 2001, 1992, 1963, 1983, 2020,
             2018, 2021, 2019, 2019, 2021, 2015,
             2022, 2022, 2022, 2022, 2021, 2023,
             2021, 2016, 2022, 2021, 2022, 2022, 
             2022, 2022, 2022, 2022, 2021, 2014,
             2018, 2018, 2017, 2021, 2018, 2019,
             2017, 2023]  
    st.markdown("This is the list of all missing years of the column 'startYear'")
    st.write(startYear)

    st.markdown("After filling, we have only one problem with column 'genres'.")
    

    st.write("")
    st.markdown("We can not find a good solution to fill NaN of column 'genres', so we decided to drop all titles with NaN.")
    st.markdown("Then we combined our dataset with 2 others to get variables of staffs. Our final dataset will be like this:")
    st.image("asset/prepocessing2.png")
    st.write("")
    st.markdown("Due to the size of dataset, we can not excute the last step here. But we will show the KPI of our final dataset in the 'Movie Analysis' section.")





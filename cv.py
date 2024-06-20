from pathlib import Path

import streamlit as st
#from PIL import Image

def about_me():
    # --- PATH SETTINGS ---

    #css_file = current_dir / "styles" / "main.css"
    #resume_file = current_dir / "assets" / "CV.pdf"
    profile_pic = "asset/pic_cv.jpg"


    # --- GENERAL SETTINGS ---
    
    NAME = ":blue[Mai TRAN]"
    DESCRIPTION = """
    Data Analyst
    """
    ADRESS = "Paris, France"
    CONTACT = "+33 6 25 35 04 35"
    EMAIL = "ves.tranmai@gmail.com"
    SOCIAL_MEDIA = {" ": " ",
        "LinkedIn": "https://www.linkedin.com/in/tran-mai-341283306/",
        "GitHub": "https://github.com/tranphuongmai",
        " ": " "
        }
    


    #st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



    # --- PERSONNAL SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.header(DESCRIPTION)
        st.write("📍", ADRESS)
        st.write("📱", CONTACT)
        st.write("📫", EMAIL)
        st.download_button(
            label=" 📄 Download Resume",
            data="PDFbyte",
            #file_name=resume_file.name,
            mime="application/octet-stream",
        )


    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
    


    # --- WORK HISTORY ---
    st.write('\n')
    st.write("---")
    st.subheader("Professional Experience")
    

    # --- JOB 1
    st.write("💼", "**Communications Manager/Marketing Department Assistant | Stage Group**")
    st.text("""
            IT company targeting Japanese market with resources located in HCMC, Vietnam
            (06/2017 - 05/2018)
            """)
    st.text(
        """
        🔹 Coordination between Japanese and Vietnamese employees
        🔹 Translation of software, web content, customer specifications
        🔹 Vietnamese market research 
    """
    )

    # --- JOB 2
    st.write('\n')
    st.write("💼", "**Store Manager| Ichioka Seika Vietnam**")
    st.text("""
            Manufacturer and seller of traditional Japanese sweets from Tokushima,
            based in HCMC Vietnam.
            (06/2016 - 05/2017)""")
    st.text(
        """
        🔹 Manage a team of 6 sales staffs
        🔹 Implement marketing and merchandising plan
        🔹 Stock management
        🔹 Relations with partners (Takashimaya shopping center)
    """)

    # --- JOB 3
    st.write('\n')
    st.write("💼", "**Sales assistant | Maison JSC**")
    st.text("""
            Distributor of international brands in HCMC and Hanoi, Vietnam. 
            (10/2011 - 06/2014)""")
    st.text(
        """
         🔹 Sales with targets
         🔹 Assistant floor manager
         🔹 Cash desk management
    """
    )

    # --- Projects & Accomplishments ---
    st.write('\n')
    st.write("---")
    st.subheader("Implemented Projects")
    

    # project 3 
    #pro3 = "https://github.com/tranphuongmai/Python_Sklearn_Pandas"
    st.markdown("**Movie Recommendation System**")
    st.text("""
    Using only Python programming language for implementing this project. We used
    Pandas for massive data exploration and preprocessing, then scikit-learn for 
    creating the movie recommendation system. Thanks to Streamlit, we can deploy 
    our system as an application.
    """)
    st.text("""
            💻 Used Tools:
            ▪️ Python, Pandas, Scikit-learn 
            ▪️ Seaborn, Matplotlib, plotly express, Power BI
            ▪️ Agile, Trello, Canva, Streamlit
            """)
    st.write(f"[Github](https://github.com/tranphuongmai/Python_Sklearn_Pandas)")
    st.write('\n')
   
    # project 2 
    #pro2 = "https://github.com/tranphuongmai/SQL_Ex_and_Poject/tree/main/project_toyandsci_SQL_PBI"
    st.markdown("**Distribution Company Daily Report**")
    st.text("""
   Building 3 dashboards that visualize KPIs regarding sales, finance, inventory and
   personnel issues of a toy distribution company. The retrieved KPI are requested by
   Database Language (MySQL) which are then connected to PowerBI for visualization.
   We worked in teams of 3 people by using Agile methodology and Trello tools to 
   manage each person's tasks.   
    """)
    st.text("""
            💻 Used Tools:
            ▪️ MySQL 
            ▪️ Power BI
            ▪️ Power Point, Agile, Trello""")
    st.write(f"[Github](https://github.com/tranphuongmai/SQL_Ex_and_Poject/tree/main/project_toyandsci_SQL_PBI)")
    st.write('\n')

    # project 1 
    #pro1 = "https://github.com/tranphuongmai"
    st.write("**E-commercial Sales Dashboard**")
    st.text("""
    Building a sales dashboard which visualizes the KPI over 4 years of an E-commercial
    company as: sales and profit evolution, point out the segment of company's main 
    consumers, customer analysis for 'Personalized PR project', product analysis for 
    inventory management. All the dashboards have a filtering system according to year
    and region.
    """)
    st.text("""
            💻 Used Tools:
            ▪️ MS Excel 
            ▪️ Power BI
            """)
    st.write(f"[Github](https://github.com/tranphuongmai)")

    
    # --- SKILLS ---
    st.write('\n')
    st.write("---")
    st.subheader("Skills")
    col1, col2= st.columns(2)
    with col1:
       st.text("""
               💠 Programming: 
                   ▪️ Python 
                   (Scikit-learn, Pandas)
                   ▪️ MySQL
                   ▪️ DAX (intermediate)
               
               💠 Data Visulization:
                   ▪️ PowerBi, Tableau
                   ▪️ Seaborn, Matplotlib, 
                   Plotly Express 
               
               💠 Others: 
                  ▪️ Agile 
                  ▪️ Canva, Power Point
               """)
    with col2:
       st.text("""
               💠 Modeling:
                  ▪️ Logistic Regression
                  ▪️ Linear Regression 
                  ▪️ Decision Trees
                  ▪️ KNN, Nearest Neighbors
               
               💠 Languages:
                  ▪️ French (fluent)
                  ▪️ English (fluent) 
                  ▪️ Japanese (intermediate) 
                  ▪️ Vietnamese (mothertongue)
               
               💠  Soft skills:
                  ▪️ Analytical and structured mindset
                  ▪️ Autonomous and capable of team work
               """)
       

    
    st.text("""
            
             
            
            
                """)
    

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.write("---")
    st.subheader("Formation")
    
    
    st.text("""
            💠 Bachelor Degree (intenive course) in Data Analysis - Wild Code School
            France 2024
                 ▪️ Data preprocessing with algorithms in Python
                 ▪️ DataViz with database languages and visualization software
                 ▪️ Data mining with Pandas, SQL, DAX
            
            💠 Bachelor Degree in Japanese Studies- National Institute of Oriental Languages
            and Civilization (INALCO)
            France 2023

            💠 DUT Foreign Trade - Hong Bang Internationnal University
            Vietnam 2011
            
                """)
    
    # --- HOBBY ---
    st.write('\n')
    st.write("---")
    st.subheader("Hobby")
   
    st.text("""
            🔹 Independent travel: discovering new places, culture and local food
            🔹 Cooking: preparing, enjoying mediterranean and asian cuisine
            🔹 Sport: hiking, yoga
           
                """)

    
    


    
    


    


    

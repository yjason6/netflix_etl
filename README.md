<!-- ABOUT THE PROJECT -->
## About The Project - Netflix data from Kaggle ETL Process

The purpose of this project is to demonstrate the end to end Extract, Transform, Load (ETL) process that is commonly used to build pipelines in data engineering. 

Netflix dataset containing data related to 

-   Show type

-   Title

-   Director(s)

-   Country

-   Date added to Netflix

-   Release year

-   Show rating

-   Show duration

-   Show categories

has been downloaded from Kaggle.com - https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization/

Data from the csv file was transformed using Python Pandas. 

Transformed csv files were then ultimately local loaded into PostgreSQL for querying and also local loaded into PowerBI for data visualisation 

<!-- LIBRARY TOOLKIT -->
## Library & Toolkit Used

-   Python Pandas

<!-- TRANSFORMATION -->
## Data Transformations Performed

-   Pandas get_dummies function 

-   Date format change

-   Splitting of a column

-   Concatenation of Dataframes

-   Renaming of columns

-   String split

-   Pandas explode function

-   Pandas groupby function

-   Pandas sum function


<!-- VISULISATION -->
## How to run ETL process

1.  Clone repository to download netflix.py

2.  Download original Kaggle Netflix dataset (csv file) from - https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization/

3.  Place the two files in the same folder, run netflix.py script with Pandas library installed

4.  Expect 3 output files
    -   netflix_movies_show.csv
    -   director.csv
    -   categories_country.csv

5.  The 3 output files were fed into PowerBI for visualisation






import pandas as pd

# Read original CSV file from Kaggle
df = pd.read_csv('netflix1.csv')

# TRANSFORMATION

# ***** DATA TRANSFORMATION 1 - Splitting 'listed_in' column *****

# Selecting the right columns - minus 'director'
# Keeping 'listed_in' column for the purpose of data verification 
netflix_movies_show=df[["show_id","type","title","country","date_added","release_year","rating","duration","listed_in"]]

# Using Pandas function of get_dummies, split 'listed_in' column by comma
# Merging the two dataframes
netflix_movies_show = pd.concat([netflix_movies_show, df['listed_in'].str.get_dummies(sep=', ')], axis=1)

# ***** DATA TRANSFORMATION 2 - Conversion of American date format to DD/YY/YYYY format *****

netflix_movies_show['date_added'] = pd.to_datetime(netflix_movies_show["date_added"]).dt.strftime('%d-%m-%Y') 

# ***** DATA TRANSFORMATION 3 - Split of duration column to allow for filtering in PowerBI
netflix_movies_show[['time', 'min_or_season']] = df['duration'].str.split(' ', expand=True)

# ***** DATA TRANSFORMATION 4 - Renaming of columns for 'netflix_movies_show' df *****
netflix_movies_show = netflix_movies_show.rename(columns={
                                'type': 'netflix_type',
                                'Action & Adventure': 'action_adventure', 
                                'Anime Features': 'anime_features', 
                                'Anime Series': 'anime_series', 
                                'British TV Shows': 'british_tv_shows', 
                                'Children & Family Movies': 'children_family_movies',
                                'Classic & Cult TV': 'classic_cult_tv',
                                'Classic Movies': 'classic_movies',
                                'Comedies': 'comedies',
                                'Crime TV Shows': 'crime_tv_shows',
                                'Cult Movies': 'cult_movies',
                                'Documentaries': 'documentaries',
                                'Docuseries': 'docuseries',
                                'Dramas': 'dramas',
                                'Faith & Spirituality': 'faith_spirituality',
                                'Horror Movies': 'horror_movies',
                                'Independent Movies': 'independent_movies',
                                'International Movies': 'international_movies',
                                'International TV Shows': 'international_tv_shows',
                                "Kids' TV": 'kids_tv', 
                                'Korean TV Shows': 'korean_tv_shows',   
                                'LGBTQ Movies': 'lgbtq_movies', 
                                'Movies': 'movies', 
                                'Music & Musicals': 'music_musicals',   
                                'Reality TV': 'reality_tv', 
                                'Romantic Movies': 'romantic_movies',   
                                'Romantic TV Shows': 'romantic_tv_shows',   
                                'Sci-Fi & Fantasy': 'sci_fi_fantasy',   
                                'Science & Nature TV': 'science_nature_tv', 
                                'Spanish-Language TV Shows': 'spanish_language_tv_shows',   
                                'Sports Movies': 'sports_movies',   
                                'Stand-Up Comedy': 'stand_up_comedy',
                                'Stand-Up Comedy & Talk Shows': 'stand_up_comedy_talk_show',    
                                'TV Action & Adventure': 'tv_action_adventure', 
                                'TV Comedies': 'tv_comedies',   
                                'TV Dramas': 'tv_dramas',
                                'TV Horror': 'tv_horror',   
                                'TV Mysteries': 'tv_mysteries', 
                                'TV Sci-Fi & Fantasy': 'tv_sci_fi_fantasy', 
                                'TV Shows': 'tv_shows',
                                'TV Thrillers': 'tv_thrillers',
                                'Teen TV Shows': 'teen_tv_shows',
                                'Thrillers': 'thrillers'})

# Export 'netflix_movies_show' to csv
netflix_movies_show.to_csv('netflix_movies_show.csv')
print('Successfully exported netflix_movies_show.csv')

# ***** DATA TRANSFORMATION 5 - Seperate Splitting of director column *****

# Seperate DF for director related data
director=df[["type","title","country","director"]]

# Split string by comma, convert to list

x = director['director'].str.split(', ').tolist()

# Pandas explode function to split 'director' column in to different rows
director = director.explode('director', ignore_index=True)

# ***** DATA TRANSFORMATION 6 - Renaming of columns for 'director' df *****
director = director.rename(columns={
                                'type': 'netflix_type',
                                'title': 'title', 
                                'country': 'country',
                                'director': 'director'
                                })

# Export 'director' to csv
director.to_csv('director.csv')
print('Successfully exported director.csv')


# ***** DATA TRANSFORMATION 7 - Seperate df for country and cateogries / Transpose *****

netflix_movies_show2 = netflix_movies_show[["country", "action_adventure", "anime_features", "anime_series", "british_tv_shows", "children_family_movies", "classic_cult_tv",
"classic_movies", "comedies", "crime_tv_shows", "cult_movies", "documentaries", "docuseries", "dramas", "faith_spirituality", "horror_movies", "independent_movies", "international_movies",
"international_tv_shows", "kids_tv", "korean_tv_shows", "lgbtq_movies", "movies", "music_musicals", "reality_tv", "romantic_movies", "romantic_tv_shows", "sci_fi_fantasy", "science_nature_tv", 
"spanish_language_tv_shows", "sports_movies", "stand_up_comedy", "stand_up_comedy_talk_show", "tv_action_adventure", "tv_comedies", "tv_dramas", "tv_horror", "tv_mysteries", "tv_sci_fi_fantasy", 
"tv_shows", "tv_thrillers", "teen_tv_shows", "thrillers"]]

categories_country = netflix_movies_show2.groupby('country').sum()

# Export 'country_categories_transposed' to csv
categories_country.to_csv('categories_country.csv')
print('Successfully exported country_categories_transposed.to_csv')


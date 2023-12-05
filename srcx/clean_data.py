import csv
import pandas as pd

# 12.) Workflow: Data Cleaning and Processing 

### List of all csv files for word clouds:
##### 1.) dict1_newest_post_titles.csv: this csv file contains counts of all the words found from all the titles of posts about artifical intelligence sorted by "newest"
##### 2.) dict2_newest_comments.csv:* this csv file contains counts of all the words found from all the comments on posts about artifical intelligence sorted by "newest"
##### 3.) dict3_most_comment_post_titles_word_counts_dict_final.csv: this csv file contains counts of all the words found from all the titles of posts about artifical intelligence sorted by "most comments"
##### 4.) dict4_relevance_comments_word_counts_dict_final.csv: this csv file contains counts of all the words found from all the comments on posts about artifical intelligence sorted by "relevance"
##### 5.) dict5_top_comment_word_counts_dict_final.csv:this csv file contains counts of all the words found from all the comments on posts about artifical intelligence sorted by "TOP"
##### 6.) dict6_top_post_titles_word_counts_dict_final.csv: this csv file contains counts of all the words found from all the titles of posts about artifical intelligence sorted by "TOP"
##### 7.) dict7_hot_post_titles_word_counts_dict_final.csv: this csv file contains counts of all the words found from all the titles of posts about artifical intelligence sorted by "HOT"
##### 8.) dict8_hot_post_titles_past_year_word_counts_dict_final.csv: this csv file contains counts of all the words found from all the titles of posts about artifical intelligence sorted by "TOP" from the past year
##### 9.) dict9_relevance_post_titles_past_year_word_counts_dict_final.csv: this csv file contains counts of all the words found from all the titles of posts about artifical intelligence sorted by "relevance" from the past year
##### 10.) dict10_most_comments_post_titles_past_year_word_counts_dict_final.csv: this csv file contains counts of all the words found from all the titles of posts about artifical intelligence sorted by "most comments" from the past year

# The first step is to create a list of stop words to use to clean the data. 
# Stop words are the words in a stop list which are filtered out before or after processing of natural language data because they are insignificant. 
# These words do not add any significant meaning to my analysis and will skew my results and my word clouds:

stop_words = ['artifical','the', 'and', 'it', 'that', 'to', 'for', 'in','so','was',"it's",'at','about', 
              'is', 'are', 'we', 'i', 'be','of','a','you','as','with','but','an','not','on','or','this','by',
              'they','have', 'a','an', 'the', 'and', 'it', 'for', 'or', 'but', 'in', 'my', 'your', 'if', 'no', 'yes', 'my','what', 'from']

## 1.) Processing the data frame for the 1st csv
df1 = pd.read_csv('data/raw/dict1_newest_post_titles.csv')
# The first step would be to remove all instances of words that only appear once or twice because they're not relevant
df1 = df1[df1["Count"] > 2]
# This next step removes the stop words
filtered_df1 = df1[~df1['Word'].isin(stop_words)]
# Convert df to a dictionary 
word_count_dict_1 = dict(zip(filtered_df1['Word'], filtered_df1['Count']))

# Then export it to a csv:
with open('data/processed/processed_data_dict_1_posts.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_dict_1.items():
        w.writerow([key, value])

## 2.) Processing the data frame for the 2nd csv
df2 = pd.read_csv('data/raw/dict2_newest_comments.csv')
df2 = df2[df2["Count"] > 2]
filtered_df2 = df2[~df2['Word'].isin(stop_words)]
word_count_dict_2 = dict(zip(filtered_df2['Word'], filtered_df2['Count']))

# Then export it to a csv:
with open('data/processed/processed_data_dict_2_comments.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_dict_2.items():
        w.writerow([key, value])

## 3.) Processing the data frame for the 3rd csv
df3 = pd.read_csv('data/raw/dict3_most_comment_post_titles_word_counts_dict_final.csv')
df3 = df3[df3["Count"] > 2]
filtered_df3 = df3[~df3['Word'].isin(stop_words)]
word_count_dict_3 = dict(zip(filtered_df3['Word'], filtered_df3['Count']))

# Then export it to a csv:
with open('data/processed/processed_data_dict_3_posts.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_dict_3.items():
        w.writerow([key, value])

## 4.) Processing the data frame for the 4th csv
df4 = pd.read_csv('data/raw/dict4_relevance_comments_word_counts_dict_final.csv')
df4 = df4[df4["Count"] > 2]
filtered_df4 = df4[~df4['Word'].isin(stop_words)]
word_count_dict_4 = dict(zip(filtered_df4['Word'], filtered_df4['Count']))

with open('data/processed/processed_data_dict_4_comments.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_dict_4.items():
        w.writerow([key, value])

## 5.) Processing the data frame for the 5th csv
df5 = pd.read_csv('data/raw/dict5_top_comment_word_counts_dict_final.csv')
df5 = df5[df5["Count"] > 2]
filtered_df5 = df5[~df5['Word'].isin(stop_words)]
word_count_dict_5 = dict(zip(filtered_df5['Word'], filtered_df5['Count']))

with open('data/processed/processed_data_dict_5_comments.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_dict_5.items():
        w.writerow([key, value])
    
## 6.) Processing the data frame for the 6th csv
df6 = pd.read_csv('data/raw/dict6_top_post_titles_word_counts_dict_final.csv')
df6 = df6[df6["Count"] > 2]
filtered_df6 = df6[~df6['Word'].isin(stop_words)]
word_count_dict_6 = dict(zip(filtered_df6['Word'], filtered_df6['Count']))

with open('data/processed/processed_data_dict_6_posts.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_dict_6.items():
        w.writerow([key, value])

## 7.) Processing the data frame for the 7th csv
df7 = pd.read_csv('data/raw/dict7_hot_post_titles_word_counts_dict_final.csv')
df7 = df7[df7["Count"] > 2]
filtered_df7 = df7[~df7['Word'].isin(stop_words)]
word_count_dict_7 = dict(zip(filtered_df7['Word'], filtered_df7['Count']))

with open('data/processed/processed_data_dict_7_posts.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_dict_7.items():
        w.writerow([key, value])

## 8.) Processing the data frame for the 8th csv
df8 = pd.read_csv('data/raw/dict8_hot_post_titles_past_year_word_counts_dict_final.csv')
df8 = df8[df8["Count"] > 2]
filtered_df8 = df8[~df8['Word'].isin(stop_words)]
word_count_dict_8 = dict(zip(filtered_df8['Word'], filtered_df8['Count']))

with open('data/processed/processed_data_dict_8_posts.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_dict_8.items():
        w.writerow([key, value])

## 9.) Processing the data frame for the 9th csv
df9 = pd.read_csv('data/raw/dict9_relevance_post_titles_past_year_word_counts_dict_final.csv')
df9 = df9[df9["Count"] > 2]
filtered_df9 = df9[~df9['Word'].isin(stop_words)]
word_count_dict_9 = dict(zip(filtered_df9['Word'], filtered_df9['Count']))

with open('data/processed/processed_data_dict_9_posts.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_dict_9.items():
        w.writerow([key, value])

## 10.) Processing the data frame for the 10th csv
df10 = pd.read_csv('data/raw/dict10_most_comments_post_titles_past_year_word_counts_dict_final.csv')
df10 = df10[df10["Count"] > 2]
filtered_df10 = df10[~df10['Word'].isin(stop_words)]
word_count_dict_10 = dict(zip(filtered_df10['Word'], filtered_df10['Count']))

with open('data/processed/processed_data_dict_10_posts.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_dict_10.items():
        w.writerow([key, value])

## Combining the dfs for comments

list_of_comment_dfs = [filtered_df2, filtered_df4, filtered_df5]
# Concatenate the list of dfs into a single df
combined_df_comments = pd.concat(list_of_comment_dfs, ignore_index=True)
final_df_comments = combined_df_comments.groupby('Word')['Count'].sum().reset_index()

stop_words_2 = ['artifical','the', 'and', 'it', 'that', 'to', 'for', 'in','so','was',"it's",'at','about', 
              'is', 'are', 'we', 'i', 'be','of','a','you','as','with','but','an','not','on','or','this','by',
              'they','have', 'a','an', 'the', 'and', 'it', 'for', 'or', 'but', 'in', 'my', 'your', 'if', 'no', 'yes', 'my','what', 'from', 'he', 'has','will','all',
             'also','how','only','also','some','can','could','do','he','some','would','its','just','like','their','out','which','our','said','when','who']

df_comments = final_df_comments[final_df_comments["Count"] > 2]
filtered_df_comments = df_comments[~df_comments['Word'].isin(stop_words_2)]
word_count_final_dict = dict(zip(filtered_df_comments['Word'], filtered_df_comments['Count']))

# Exporting the final comment count to a csv
with open('data/processed/final_comments_combined.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_final_dict.items():
        w.writerow([key, value])

## Combining the post title dfs:
list_of_post_dfs = [filtered_df1, filtered_df3, filtered_df6, filtered_df7, filtered_df8, filtered_df9, filtered_df10]
# Concatenate the list of dfs into a single df
combined_df_posts = pd.concat(list_of_post_dfs, ignore_index=True)
final_df_posts = combined_df_posts.groupby('Word')['Count'].sum().reset_index()
df_posts = final_df_posts[final_df_posts["Count"] > 2]
filtered_df_posts = df_posts[~df_posts['Word'].isin(stop_words_2)]
word_count_final_dict_2 = dict(zip(filtered_df_posts['Word'], filtered_df_posts['Count']))

# Exporting it
with open('data/processed/final_posts_combined.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_final_dict_2.items():
        w.writerow([key, value])

# Combining both of those just because it may be interesting to see:
list_of_dfs = [filtered_df_posts, filtered_df_comments]
all_combined = pd.concat(list_of_dfs, ignore_index=True)
final_df_all = all_combined.groupby('Word')['Count'].sum().reset_index()
df_final = final_df_all[final_df_all["Count"] > 2]
filtered_df_final = df_final[~df_final['Word'].isin(stop_words_2)]
final_dict_final = dict(zip(filtered_df_final['Word'], filtered_df_final['Count']))

# Exporting that final csv
with open('data/processed/final_combined_posts_comments.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in final_dict_final.items():
        w.writerow([key, value])

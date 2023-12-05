import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import csv
import seaborn as sns
from datetime import datetime
from dateutil import parser


stop_words = ['artifical','the', 'and', 'it', 'that', 'to', 'for', 'in','so','was',"it's",'at','about', 
              'is', 'are', 'we', 'i', 'be','of','a','you','as','with','but','an','not','on','or','this','by',
              'they','have', 'a','an', 'the', 'and', 'it', 'for', 'or', 'but', 'in', 'my', 'your', 'if', 
              'no', 'yes', 'my','what', 'from']
stop_words_2 = ['its', 'can','out','one','our','all',
                   'from','will','like','their','just','has','would','where','there',
                   'how','where']

## 1.) Processing the data frame for the 1st csv
df1 = pd.read_csv('data/processed/processed_data_dict_1_posts.csv')
df1 = df1[df1["Count"] > 2]
filtered_df1 = df1[~df1['Word'].isin(stop_words)]
word_count_dict_1 = dict(zip(filtered_df1['Word'], filtered_df1['Count']))

# Create WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='hsv').generate_from_frequencies(word_count_dict_1)

# Display the generated image:
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in post titles sorted by "newest"', fontsize=18, color='black', 
          bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))


plt.savefig('results/wordcloud_1_posts.png', format='png', dpi=300, bbox_inches='tight')
#plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Visualizing the second csv
df2 = pd.read_csv('data/processed/processed_data_dict_2_comments.csv')
df2 = df2[df2["Count"] > 2]
filtered_df2 = df2[~df2['Word'].isin(stop_words_2)]
word_count_dict_2 = dict(zip(filtered_df2['Word'], filtered_df2['Count']))
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='turbo').generate_from_frequencies(word_count_dict_2)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in post comments sorted by "newest"', fontsize=18, color='black', 
          bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))

output_path = 'results/wordcloud_2_comments.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Visualizing the third csv
df3 = pd.read_csv('data/processed/processed_data_dict_3_posts.csv')
df3 = df3[df3["Count"] > 2]
filtered_df3 = df3[~df3['Word'].isin(stop_words)]
word_count_dict_3 = dict(zip(filtered_df3['Word'], filtered_df3['Count']))
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='hsv').generate_from_frequencies(word_count_dict_3)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in post titles sorted by "most comments', fontsize=18, color='black', 
          bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))

output_path = 'results/wordcloud_3_posts.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Visualizing the fourth csv
df4 = pd.read_csv('data/processed/processed_data_dict_4_comments.csv')
df4 = df4[df4["Count"] > 2]
filtered_df4 = df4[~df4['Word'].isin(stop_words_2)]
word_count_dict_4 = dict(zip(filtered_df4['Word'], filtered_df4['Count']))
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='turbo').generate_from_frequencies(word_count_dict_4)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in post comments sorted by "relevance"', fontsize=18, color='black', 
          bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))

output_path = 'results/wordcloud_4_comments.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Visualizing the fifth csv
df5 = pd.read_csv('data/processed/processed_data_dict_5_comments.csv')
df5 = df5[df5["Count"] > 2]
filtered_df5 = df5[~df5['Word'].isin(stop_words)]
word_count_dict_5 = dict(zip(filtered_df5['Word'], filtered_df5['Count']))
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='turbo').generate_from_frequencies(word_count_dict_5)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in post comments sorted by "TOP⬆', fontsize=18, color='black', 
          bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))

output_path = 'results/wordcloud_5_comments.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Visualizing the sixth csv
df6 = pd.read_csv('data/processed/processed_data_dict_6_posts.csv')
df6 = df6[df6["Count"] > 2]
filtered_df6 = df6[~df6['Word'].isin(stop_words)]
word_count_dict_6 = dict(zip(filtered_df6['Word'], filtered_df6['Count']))
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='hsv').generate_from_frequencies(word_count_dict_6)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in post titles sorted by "TOP⬆', fontsize=18, color='black', 
          bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))

output_path = 'results/wordcloud_6_posts.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Visualizing the seventh csv
df7 = pd.read_csv('data/processed/processed_data_dict_7_posts.csv')
df7 = df7[df7["Count"] > 2]
filtered_df7 = df7[~df7['Word'].isin(stop_words)]
word_count_dict_7 = dict(zip(filtered_df7['Word'], filtered_df7['Count']))
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='hsv').generate_from_frequencies(word_count_dict_7)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in post titles sorted by "HOT"', fontsize=18, color='black', 
          bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))

output_path = 'results/wordcloud_7_posts.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Visualizing the eighth csv
df8 = pd.read_csv('data/processed/processed_data_dict_8_posts.csv')
df8 = df8[df8["Count"] > 2]
filtered_df8 = df8[~df8['Word'].isin(stop_words)]
word_count_dict_8 = dict(zip(filtered_df8['Word'], filtered_df8['Count']))
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='hsv').generate_from_frequencies(word_count_dict_8)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in post titles sorted by "HOT" within the past year', 
          fontsize=18, color='black', bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))

output_path = 'results/wordcloud_8_posts.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Visualizing the ninth csv
df9 = pd.read_csv('data/processed/processed_data_dict_9_posts.csv')
df9 = df9[df9["Count"] > 2]
filtered_df9 = df9[~df9['Word'].isin(stop_words)]
word_count_dict_9 = dict(zip(filtered_df9['Word'], filtered_df9['Count']))
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='hsv').generate_from_frequencies(word_count_dict_9)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in post titles sorted by "relevance" within the past year', 
          fontsize=18, color='black', bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))

output_path = 'results/wordcloud_9_posts.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Visualizing the tenth csv
df10 = pd.read_csv('data/processed/processed_data_dict_9_posts.csv')
df10 = df10[df10["Count"] > 2]
filtered_df10 = df10[~df10['Word'].isin(stop_words)]
word_count_dict_10 = dict(zip(filtered_df10['Word'], filtered_df10['Count']))
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='hsv').generate_from_frequencies(word_count_dict_10)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in post titles sorted by "most comments" within the past year', 
          fontsize=18, color='black', bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))

output_path = 'results/wordcloud_10_posts.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Visualizing the concatenated comments csv
stop_words_x = ['artifical','the', 'and', 'it', 'that', 'to', 'for', 'in','so','was',"it's",'at','about', 
              'is', 'are', 'we', 'i', 'be','of','a','you','as','with','but','an','not','on','or','this','by',
              'they','have', 'a','an', 'the', 'and', 'it', 'for', 'or', 'but', 'in', 'my', 'your', 'if', 'no', 'yes', 'my','what', 'from', 'he', 'has','will','all',
             'also','how','only','also','some','can','could','do','he','some','would','its','just','like','their','out','which','our','said','when','who',
             'its', 'can','out','one','our','all',
                   'from','will','like','their','just','has','would','where','there',
                   'how','where']
list_of_comment_dfs = [filtered_df2, filtered_df4, filtered_df5]
combined_df_comments = pd.concat(list_of_comment_dfs, ignore_index=True)
final_df_comments = combined_df_comments.groupby('Word')['Count'].sum().reset_index()
df_comments = final_df_comments[final_df_comments["Count"] > 2]
filtered_df_comments = df_comments[~df_comments['Word'].isin(stop_words_x)]
word_count_final_dict = dict(zip(filtered_df_comments['Word'], filtered_df_comments['Count']))

wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='turbo').generate_from_frequencies(word_count_final_dict)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in all post comments', fontsize=20, color='black', 
          bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))

output_path = 'results/wordcloud_all_comments.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()

with open('results/final_comments_combined.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_final_dict.items():
        w.writerow([key, value])
#--------------------------------------------------------------------------------------------------------------------
# Visualizing the concatenated posts csv
list_of_post_dfs = [filtered_df1, filtered_df3, filtered_df6, filtered_df7, 
                    filtered_df8, filtered_df9, filtered_df10]
combined_df_posts = pd.concat(list_of_post_dfs, ignore_index=True)
final_df_posts = combined_df_posts.groupby('Word')['Count'].sum().reset_index()
df_posts = final_df_posts[final_df_posts["Count"] > 2]
filtered_df_posts = df_posts[~df_posts['Word'].isin(stop_words_x)]
word_count_final_dict_2 = dict(zip(filtered_df_posts['Word'], filtered_df_posts['Count']))
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      font_path='/Library/Fonts/Verdana.ttf', 
                      colormap='hsv').generate_from_frequencies(word_count_final_dict_2)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Most commonly used words in all post titles', fontsize=20, color='black', 
          bbox=dict(facecolor='yellow', edgecolor='white', boxstyle='round,pad=0.1'))

output_path = 'results/wordcloud_all_posts.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()

with open('results/final_posts_combined.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Word', 'Count'])
    for key, value in word_count_final_dict_2.items():
        w.writerow([key, value])
#----------------------------------------------------------------------------------------------------------
stop_words_y = ['artifical','the', 'and', 'it', 'that', 'to', 'for', 'in','so','was',"it's",'at','about', 
              'is', 'are', 'we', 'i', 'be','of','a','you','as','with','but','an','not','on','or','this','by',
              'they','have', 'a','an', 'the', 'and', 'it', 'for', 'or', 'but', 'in', 'my', 'your', 'if', 'no', 
              'yes', 'my','what', 'from', 'he', 'has','will','all',
             'also','how','only','also','some','can','could','do','he','some','would','its','just','like','their',
             'out','which','our','said','when','who',
             'its', 'can','out','one','our','all',
                   'from','will','like','their','just','has','would','where','there',
                   'how','where','were','us','into','more','been','than','time','up','new','even','now',
               'other','because','these','such','then','ai','say',
                'had','over','humans','make','any','them','years','use','get','most','first']
df = pd.read_csv("data/processed/final_posts_combined.csv")
df = df[~df['Word'].isin(stop_words_y)]
# Most common words
most_common_words = df.nlargest(12, 'Count')[2:] # <------
plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Word', data=most_common_words, palette='turbo') # <------
ax = sns.barplot(x='Count', y='Word', data=most_common_words, palette='turbo')
for p in ax.patches:
    ax.annotate(f'{p.get_width():.0f}', (p.get_width(), p.get_y() + p.get_height() / 2), 
                ha='left', va='center', fontsize=10, color='black')
plt.title('Top 10 most common words in post titles (other than "artificial" and "intelligence"):')
plt.xlabel('Count')
plt.ylabel('Word')

output_path = 'results/top_10_most_common_words_on_posts.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
# Word frequency distribution
plt.figure(figsize=(12, 6))
sns.histplot(df['Count'], bins=30, kde=True, color='purple') # <------
plt.title('Word Frequency Distribution')
plt.xlabel('Count')
plt.ylabel('Frequency')

output_path = 'results/Word_Frequency_dist_posts.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
#----------------------------------------------------------------------------------------------------------
# visualizing the combined comments csv
df = pd.read_csv("data/processed/final_comments_combined.csv")
df = df[~df['Word'].isin(stop_words_y)]
# Most common words
most_common_words = df.nlargest(12, 'Count')[2:]
# Plot a bar chart of the top 10 words
plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Word', data=most_common_words, palette='turbo') # <------
ax = sns.barplot(x='Count', y='Word', data=most_common_words, palette='turbo')
# Display count values on the bars
for p in ax.patches:
    ax.annotate(f'{p.get_width():.0f}', (p.get_width(), p.get_y() + p.get_height() / 2), 
                ha='left', va='center', fontsize=10, color='black')
plt.title('Top 10 most common words in comments(other than "artificial" and "intelligence"):')
plt.xlabel('Count')
plt.ylabel('Word')

output_path = 'results/top_10_most_common_words_in_comments.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
# Word frequency distribution
plt.figure(figsize=(12, 6))
sns.histplot(df['Count'], bins=30, kde=True, color='purple') # <------
plt.title('Word Frequency Distribution')
plt.xlabel('Count')
plt.ylabel('Frequency')

output_path = 'results/Word_Frequency_dist_comments.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
#plt.show()
#----------------------------------------------------------------------------------------------------------
# Visualizing popular subreddits:
df = pd.read_csv("data/raw/post_data_from_all_time_top_relevance_most-comments.csv")
# Visualizing popular subreddits:
df = pd.read_csv("data/raw/post_data_from_all_time_top_relevance_most-comments.csv")
top_subreddits_votes = df.groupby('Subreddit')['Votes'].sum().reset_index()
top_subreddits_votes = top_subreddits_votes.sort_values(by='Votes', ascending=False).head(30)
plt.figure(figsize=(12, 8), dpi=300)
sns.barplot(x='Votes', y='Subreddit', data=top_subreddits_votes, palette='turbo', legend=False)  # <------
plt.xlabel('Total Votes')
plt.ylabel('Subreddit')
plt.title('Top 20 Subreddits Based on Total Votes')

output_path = 'results/popular_subreddits.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
plt.show()

output_path = 'results/popular_subreddits.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')
plt.show()

# Visualizing the post dataset

df = pd.read_csv("data/raw/post_data_from_all_time_top_relevance_most-comments.csv")
df["Date"] = df["Date"].apply(lambda x: parser.parse(x))
df["Day"] = df["Date"].dt.day_name()
df["Hour"] = df["Date"].dt.hour
heatmap_data = df.pivot_table(index="Day", columns="Hour", values="Title", aggfunc="count", fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap="PuRd", annot=True, fmt="d", cbar_kws={'label': 'Number of Posts'})
plt.title("Post Activity Heatmap by Day and Time")

output_path = 'results/heatmap_posting_times.png'
plt.savefig(output_path, format='png', dpi=300, bbox_inches='tight')

plt.show()








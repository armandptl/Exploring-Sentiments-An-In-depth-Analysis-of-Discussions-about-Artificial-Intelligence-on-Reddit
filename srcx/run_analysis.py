import pandas as pd
import json
import numpy as np

all_results_posts = {}
post_files = [1, 3, 6, 7, 8, 9, 10]

for i in post_files:
    csv_path = f"data/processed/processed_data_dict_{i}_posts.csv"
    df = pd.read_csv(f"{csv_path}")
    total_unique_words = df['Word'].nunique()
    total_word_count = df['Count'].sum()
    most_common_words = df.nlargest(12, 'Count')[2:]  
    df['Word_Length'] = df['Word'].apply(len)
    average_word_length = df['Word_Length'].mean()
    # Storing the results in the dictionary
    file_results_posts = {
        'Total_Unique_Words': total_unique_words,
        'Total_Word_Count': total_word_count,
        'Most_Common_Words': most_common_words,
        'Average_Word_Length': average_word_length
    }
    
    # Saving the results in the dictionary 
    all_results_posts[csv_path] = file_results_posts

aggregate_results_posts = {
    'Total_Unique_Words': sum(result['Total_Unique_Words'] for result in all_results_posts.values()),
    'Total_Word_Count': sum(result['Total_Word_Count'] for result in all_results_posts.values()),
    'Average_Word_Length': sum(result['Average_Word_Length'] for result in all_results_posts.values()) / len(all_results_posts),
    'Most_Common_Words': pd.concat([result['Most_Common_Words'] for result in all_results_posts.values()])
}

def convert_to_serializable(obj):
    if isinstance(obj, np.int64):
        return int(obj)
    elif isinstance(obj, pd.DataFrame):
        # Convert df to JSON string
        return obj.to_json(orient='split')
    return obj
# Convert int64 values and df to serializable formats
all_results_serializable = {key: {k: convert_to_serializable(v) for k, v in value.items()} for key, value in all_results_posts.items()}
# Convert to json format
output_json = json.dumps(all_results_serializable, indent=4)
# Save to a json file
with open('results/aggregate_results_for_posts.json', 'w') as json_file:
    json_file.write(output_json)

# For comments
all_results_comments = {}
comment_files = [2,4,5]
for i in comment_files:
    csv_path = f"data/processed/processed_data_dict_{i}_comments.csv"
    df = pd.read_csv(f"{csv_path}")
    words_to_remove = ['its', 'then','general','even','time','because','only','than','know','any','when',
                       'them','up','us','more','who','had','some','also','were','into','said','other','been',
                       'which','can','out','one','our','all','from','will','like','their','just','has','would',
                       'where','there','how','where']
    df = df[~df['Word'].isin(words_to_remove)]
    total_unique_words = df['Word'].nunique()
    total_word_count = df['Count'].sum()
    most_common_words = df.nlargest(12, 'Count')[2:]  
    df['Word_Length'] = df['Word'].apply(len)
    average_word_length = df['Word_Length'].mean()
    file_results = {
        'Total_Unique_Words': total_unique_words,
        'Total_Word_Count': total_word_count,
        'Most_Common_Words': most_common_words,
        'Average_Word_Length': average_word_length
    }
    all_results_comments[csv_path] = file_results
all_results_serializable_comments = {
    key: {k: convert_to_serializable(v) for k, v in value.items()} for key, value in all_results_comments.items()
    }
output_json = json.dumps(all_results_serializable_comments, indent=4)
with open('results/aggregate_results_for_comments.json', 'w') as json_file:
    json_file.write(output_json)
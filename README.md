# Exploring-Sentiments-on-AI
I embarked on this project to explore Reddit users' perspectives on the surge of artificial intelligence in media, technology, and academia. The central question is: how do Reddit users convey sentiments in discussions about AI, and what insights can be derived from analyzing these patterns?

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/h_LXMCrc)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12818876&assignment_repo_type=AssignmentRepo)
# DSCI 510 Final Project

## Name of the Project
Exploring Sentiments: An In-depth Analysis of Discussions about Artificial Intelligence on Reddit

## Team Members (Name and Student IDs)
Armand Patel: 9357393246

## Instructions to create a conda enviornment
1. Clone the repository (https://classroom.github.com/a/h_LXMCrc)
git clone https://github.com/your-username/your-repo.git

cd your-repo

conda create --name myenv python=3.8
conda activate myenv
pip install -r requirements.txt

## Instructions on how to install the required libraries
You need to do:
pip install wordcloud
pip install --upgrade seaborn matplotlib
pip install requests
pip install selenium
pip install beautifulsoup4
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn

You are required to use safari to run the code,
For Safari, my code uses the selenium Safari driver. It's included with Safari and should work without additional installations. However, make sure you have the "Allow Remote Automation" option enabled in Safari's Develop menu.
Ensure that the Safari browser is up-to-date and the "Develop" menu is visible. You can enable the "Develop" menu in Safari by going to Safari > Preferences > Advanced and checking the "Show Develop menu in menu bar" option.
Once you've done that, you should be able to use webdriver.Safari() without any additional driver installations.
If you encounter any issues, you might need to update your Safari browser or check the Selenium documentation for Safari-specific requirements.

All the other required libraries are found in requirements.txt

## Instructions on how to download the data
The data was extracted from several links which are housed in the get_data.py file, so just running the file 
collects the data. I used selenium and a webdriver on safari (so safari must be used for this) to dynamically
scroll through the reddit website and collect all the html scripts to then parse through beautifulsoup4. I then collected all the words and separated the words, post titles, comments, votes, and all other necessary data from
these html scripts.
To download the data, run:
python3 final-project-armandptl/src/get_data.py

The files will then be pushed to the raw data folder

## Instructions on how to clean the data
The data was cleaned simply by dropping useless stop words that were not helpful to my analysis. 
This was done several times.
To clean the data in the raw data folder, run:
python3 final-project-armandptl/src/clean_data.py

The processed data will be pushed to the processed data folder

## Instrucions on how to run analysis code
To run the analysis on the data, I have written several scripts that produce JSON files with the results that 
are needed to understand the project that are pushed to the results folder.
To analyze the processed data, run:
python3 final-project-armandptl/src/run_analysis.py

The analysis JSON files will be pushed to the results folder

## Instructions on how to create visualizations
All the code to visualize the data is housed in the visualize_results.py file:
To visualize the data, run:
python3 final-project-armandptl/src/visualize_results.py

The resulting files and photos will be pushed to the results folder

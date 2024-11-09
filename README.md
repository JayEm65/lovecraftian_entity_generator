## Project Overview
This project involves scraping, analyzing, and visualizing H.P. Lovecraft's works, as well as using machine learning to generate Lovecraftian names based on the entities identified in his texts.

## Features:
1. **Web Scraping**:
    - Scrapes Lovecraft's fiction, poetry, essays, and letters from [H.P. Lovecraft's website](https://www.hplovecraft.com/writings/texts/).
    - Standardizes titles and collects the relevant text.

2. **API Data Collection**:
    - Fetches data about Lovecraftian entities (e.g., creatures, gods, races) from an external API and stores it as JSON files.

3. **Data Analysis**:
    - Analyzes the scraped and fetched data to identify entities (e.g., creatures, gods) mentioned in Lovecraft's works.
    - Counts occurrences of these entities in the texts.

4. **Visualization**:
    - Visualizes the most common Lovecraftian entities using a bar chart.
    - Offers the ability to filter by entity type (e.g., `Great Old One`, `Creature`).

5. **Sequence Generation**:
    - Uses an LSTM model to train on the names of Lovecraftian entities and generate new names that resemble those found in the author's works.

## How It Works:
1. **Scrape Works**: Web scraping pulls down the text for various works from Lovecraft's website.
2. **Fetch API Data**: API calls are made to an external Lovecraft API to retrieve data on various entities.
3. **Filter Texts**: The collected text is filtered to identify mentions of various Lovecraftian entities.
4. **Count Occurrences**: The frequency of entity mentions is counted, and the results are saved and visualized.
5. **Train LSTM Model**: An LSTM model is trained on the entity names to generate new Lovecraftian-like names.



# Lovecraftian Text Scraping and Analysis Project

This project is a data scraping and analysis tool focused on the works of H.P. Lovecraft. It scrapes various text-based content (fiction, poetry, essays, and letters) from an online source, collects data from a Lovecraft API, and analyzes common entities (creatures, races, gods, etc.) in the texts. Additionally, it includes a character-level LSTM model to explore entity name generation based on common patterns.


## Project Overview

This project performs the following steps:

1. **Scrapes Lovecraft's writings** from a selected website.
2. **Collects data** on Lovecraftian entities via API calls.
3. **Processes and cleans** the data for analysis.
4. **Analyzes** the presence of key entities in the texts.
5. **Visualizes** the most common Lovecraftian entities.
6. **Generates new entity names** using a character-level LSTM model.

## Features

- **Scraping Lovecraft Works**: Gathers texts from various categories on an online source.
- **API Data Collection**: Pulls data on creatures, races, and gods from the Lovecraft API.
- **Data Cleaning and Analysis**: Cleans entity names, merges plural forms, and counts occurrences in the texts.
- **Visualization**: Creates bar charts of the most mentioned entities.
- **LSTM Model for Name Generation**: Generates new Lovecraftian entity names based on character patterns.

## Project Structure

```plaintext
├── data/                        # Folder containing scraped and processed data files
│   ├── lovecraft_<content>.csv  # CSV files for each content type (e.g., fiction, poetry)
│   ├── <entity>.json            # JSON files containing data from API (e.g., creatures.json)
│   ├── lovecraft_name_counts.csv # CSV file with entity counts and types
├── scripts/                     # Folder containing project scripts
│   ├── scrape_lovecraft.py      # Script to scrape and save Lovecraft texts
│   ├── api_collection.py        # Script to collect data from API
│   ├── data_cleaning.py         # Script for data cleaning and analysis
│   ├── lstm_name_generator.py   # Script for the LSTM model
└── README.md                    # Project documentation


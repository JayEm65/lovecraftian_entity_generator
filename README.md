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

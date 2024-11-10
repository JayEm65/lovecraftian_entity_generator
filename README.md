# Lovecraftian Entity Generator: Unveiling Cosmic Horrors

### by Marc Jahnert

This project explores the intersection of H.P. Lovecraft’s cosmic horror and machine learning, generating new, fictional entities by training a character-level LSTM model on Lovecraft’s existing works. The project scrapes and processes Lovecraft’s texts, analyzes common entities, and produces names that adhere to Lovecraft's unique conventions.

---

## Project Overview

**Google Slides:** [Lovecraftian Entity Generator: Unveiling Cosmic Horrors](https://docs.google.com/presentation/d/1QjYuLG4xp1hbzdGRNWBjPAmmWQDwZ7SIeqHvyDPXDLk/edit?usp=sharing)

**Goal:**  
The project generates Lovecraftian entity names by scraping Lovecraft’s works, analyzing and processing the text, and then using a character-level LSTM (Long Short-Term Memory) model to create new names that align with Lovecraft’s stylistic conventions.

**Key Features:**
- **Web Scraping**: Scrapes Lovecraft’s texts for entity references.
- **API Data Integration**: Fetches data on Lovecraftian creatures, gods, and races from an external API.
- **Data Cleaning**: Standardizes names and merges variations (e.g., plural forms, spelling differences).
- **Exploratory Data Analysis (EDA)**: Identifies and visualizes the most common Lovecraftian entities.
- **Name Generation**: Utilizes an LSTM model to generate new Lovecraftian-like names.

---

## How It Works

### 1. **Scrape Lovecraft’s Works**  
Using BeautifulSoup and requests, the project scrapes Lovecraft's writings from his website, which includes fiction, poetry, essays, and letters.

### 2. **Fetch Lovecraftian Entity Data**  
The Lovecraftian API (by Iván Fuentes) is used to pull structured data about entities, such as creatures, gods, and races. This supplements the scraped text to ensure a diverse collection of entity references.

### 3. **Text Processing & Data Cleaning**  
Scraped data is preprocessed to clean and standardize entity names, correcting for plural forms and spelling variations.

### 4. **Exploratory Data Analysis (EDA)**  
The dataset is analyzed to identify the most common Lovecraftian entities, helping refine the name generation model.

### 5. **LSTM Model for Name Generation**  
A character-level LSTM model is trained on the cleaned dataset. It learns the patterns in Lovecraftian names and generates new ones based on these learned conventions.

---

## Project Breakdown

### Data Collection & Preprocessing  
- **Scraping Lovecraft's Texts**: Texts are pulled from [H.P. Lovecraft's Website](https://www.hplovecraft.com/writings/texts/), with error handling for a stable extraction process.
- **Merging Entity Variations**: Plural forms (e.g., "deep ones" vs. "deep one") are merged, and common spelling discrepancies are corrected for consistency.
- **API Integration**: The [The Lovecraftian API](https://lovecraftapirest.fly.dev) is pulled for additional data on creatures, gods, and Great Old Ones to expand the variety of the dataset.

### Exploratory Data Analysis  
The data is analyzed to identify the most frequently mentioned Lovecraftian entities, guiding the generation of names that fit within these parameters.

---

## Model Development & Architecture

### LSTM Model Details  
- **Character-Level Model**: The model processes sequences of characters, capturing the nuances of Lovecraftian name structure.
- **Architecture**: The model consists of two LSTM layers with dropout layers to prevent overfitting.
- **Accuracy**: Achieved 99% accuracy through optimized sequence length, normalization, and vocabulary handling.
- **Training Process**: Input-output sequences are created based on 5-character windows to predict the next character in the name sequence, generating realistic entity names.

---

## Challenges & Solutions

### Key Challenges:
- **Data Quality Inconsistencies**: Lovecraft’s texts contained inconsistencies that complicated the data cleaning process.
- **Stylistic Alignment**: Ensuring that generated names fit Lovecraft’s style required fine-tuning the model.
- **Avoiding Overfitting**: Balancing model accuracy and generalization involved using dropout layers.

### Solutions Implemented:
- **Data Cleaning**: Various functions were applied to standardize names and merge similar entities.
- **Regularization**: Dropout layers in the LSTM prevented overfitting, ensuring generalization of the model.

---

## Results & Future Work

### Results
- **Name Generation**: The model successfully generates Lovecraftian names that closely resemble those found in the author's works.
- **Accuracy**: Achieved 99% accuracy in generating names stylistically aligned with Lovecraft’s conventions.

### Future Directions:
- **Longer Sequences & Transformer Models**: Experimenting with these techniques to increase the richness of generated names.
- **Improved Preprocessing**: Incorporating more subtle stylistic features from Lovecraft’s texts for better model performance.

---

## Conclusion

This project has developed a model capable of generating realistic, novel Lovecraftian entities. It opens up new possibilities in game design, horror fiction, and immersive world-building.

**Future Vision:**  
An actual app to run this generator on mobile and web. The model is yet to be expanded with advanced architectures such as transformers, allowing for more creativity and sophistication in entity generation. (LLM)

---

## Tools & Libraries:
- **BeautifulSoup**: For web scraping Lovecraft’s works.
- **Requests**: For making HTTP requests to scrape text.
- **TensorFlow & Keras**: For implementing the LSTM model.
- **Pandas & NLTK* (Yet to be used.*)**: For preprocessing and data handling.

---

## Acknowledgments

- **H.P. Lovecraft**: For his pioneering work in cosmic horror and the Cthulhu Mythos.
- **[Iván Fuentes](https://github.com/navifuentes)**: For providing The Lovecraftian API.


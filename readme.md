# Text Summarizer Flask App

This Flask web application utilizes the TextRank algorithm to generate abstractive summaries of provided text. The summarization is based on the importance of sentences, determined by their similarity and relevance within the given content.

## Features

- **Summarize Text:** Input or paste the text content directly into the web interface.
- **Summarize Web Content:** Provide a URL link, and the application will fetch the content and generate a summary.
- **Adjustable Summary Length:** Adjust the summary length by specifying the percentage of the original text to include in the summary.

## How to Use

1. Clone this repository to your local machine.
2. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage Instructions

1. Enter or paste the text into the provided text area.
2. Optionally, provide a URL link to fetch content from a webpage.
3. Adjust the summary length by specifying the percentage of the original text to include.
4. Click the "Summarize" button to generate the summary.

## Sample

### Original Text

Norse, Nordic, or Scandinavian mythology is the body of myths belonging to the North Germanic peoples, stemming from Old Norse religion and continuing after the Christianization of Scandinavia, and into the Nordic folklore of the modern period. The northernmost extension of Germanic mythology and stemming from Proto-Germanic folklore, Norse mythology consists of tales of various deities, beings, and heroes derived from numerous sources from both before and after the pagan period, including medieval manuscripts, archaeological representations, and folk tradition. The source texts mention numerous gods such as the thunder-god Thor, the raven-flanked god Odin, the goddess Freyja, and numerous other deities.

Most of the surviving mythology centers on the plights of the gods and their interaction with several other beings, such as humanity and the jötnar, beings who may be friends, lovers, foes, or family members of the gods. The cosmos in Norse mythology consists of Nine Worlds that flank a central sacred tree, Yggdrasil. Units of time and elements of the cosmology are personified as deities or beings. Various forms of a creation myth are recounted, where the world is created from the flesh of the primordial being Ymir, and the first two humans are Ask and Embla. These worlds are foretold to be reborn after the events of Ragnarök when an immense battle occurs between the gods and their enemies, and the world is enveloped in flames, only to be reborn anew. There the surviving gods will meet, and the land will be fertile and green, and two humans will repopulate the world.

Norse mythology has been the subject of scholarly discourse since the 17th century when key texts attracted the attention of the intellectual circles of Europe. By way of comparative mythology and historical linguistics, scholars have identified elements of Germanic mythology reaching as far back as Proto-Indo-European mythology. During the modern period, the Romanticist Viking revival re-awoke an interest in the subject matter, and references to Norse mythology may now be found throughout modern popular culture. The myths have further been revived in a religious context among adherents of Germanic Neopaganism.

**Original Word Count:** 345

### Summarized Text

Norse, Nordic, or Scandinavian mythology is the body of myths belonging to the North Germanic peoples, stemming from Old Norse religion and continuing after the Christianization of Scandinavia, and into the Nordic folklore of the modern period. Most of the surviving mythology centers on the plights of the gods and their interaction with several other beings, such as humanity and the jötnar, beings who may be friends, lovers, foes, or family members of the gods.

**Summary Percent:** 20%
**Summarized Word Count:** 75

Feel free to explore and enhance the application as needed!

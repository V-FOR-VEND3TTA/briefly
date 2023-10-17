import tkinter as tk  # Installed by 'pip install tkinter'
import nltk  # Installed by 'pip install nltk'
from textblob import TextBlob  # Installed by 'pip install textblob'
from newspaper import Article # Installed by 'pip install newspaper3k'

# Dependencies:
# - tkinter: Used for GUI components.
# - nltk: Natural Language Toolkit for text processing.
# - textblob: Text analysis library.
# - newspaper3k: For article parsing and summarization.

def summarize():
    """
    Summarize the article from the URL provided in the 'utext' text widget.
    
    Downloads, parses, and performs natural language processing on the article. 
    Displays the article's title, author, publication date, summary, and sentiment analysis results.
    """
    # Get the URL input from the text widget
    url = utext.get('1.0', "end").strip()
 
    # Create an Article object and download, parse, and perform natural language processing
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # Enable text widgets for editing
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    # Clear and insert article information into text widgets
    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    # Perform sentiment analysis of the text
    analysis = TextBlob(article.text)

    # Clear and insert sentiment analysis results into the sentiment text widget
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    # Disable text widgets for editing
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

# Create the main application window
root = tk.Tk()
root.title("Briefly - A Fantastic News Summarizer")
root.geometry('1200x600')

# Labels for various sections
tlabel = tk.Label(root, text='Title')
tlabel.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()

plabel = tk.Label(root, text='Publication Date')
plabel.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()

selabel = tk.Label(root, text='Sentiment Analysis')
selabel.pack()

ulabel = tk.Label(root, text='URL')
ulabel.pack()

# Text widgets for displaying information
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#ddd')
title.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#ddd')
author.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#ddd')
publication.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#ddd')
summary.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#ddd')
sentiment.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

# Button for triggering article summarization
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

# Start the GUI application
root.mainloop()

# 1. Import aller notwendigen Daten (Tickets, Stopwords, Libraries)
# Import der Pandas-Bibliothek
import pandas as pd
import nltk
# CSV-Import der Ticket-Daten aus dem Order "Data" im Projektorder
tickets = pd.read_csv('Data/support_tickets.csv', low_memory=False)
pd.set_option('display.max_columns', None)

# 2. Stoppworte in Zielformat bringen
# Datenschutz-Stoppworte aus CSV holen und in Liste konvertieren
ds_stop_words = pd.read_csv('Data/datenschutz_stop_words.csv',
low_memory=False)
# Generiere ein Set aus dem CSV mit Datenschutz-Stoppwörtern
ds_stop_words_set = set()
for sublist in ds_stop_words_list:
ds_stop_words_set.add(sublist[0])
# Listen mit deutschen und englischen Stoppwörtern von NLKT laden
from nltk.corpus import stopwords
de_stopwords = stopwords.words('german')
en_stopwords = stopwords.words('english')

# 3. Vorverarbeitung mit NLTK
# 3.1. Tokenisierung für Stoppwort-Entfernung
# Tokenisierung mit Entfernung von Punktuation von Spalte "titel_beschreibung"
def identify_tokens(row):
titel_beschreibung = row['titel_beschreibung']
tokens = nltk.word_tokenize(titel_beschreibung)
# taken only words (not punctuation)
token_words = [w for w in tokens if w.isalpha()]
return token_words
tickets['titel_beschreibung_tokenized'] = \
tickets.apply(identify_tokens, axis=1)
# Tokenisierung mit Entfernung von Punktuation von Spalte "titel_beschreibung_kommentare" tokenisieren
def identify_tokens(row):
title_beschreibung_kommentare = row['title_beschreibung_kommentare']
tokens = nltk.word_tokenize(title_beschreibung_kommentare)
# taken only words (not punctuation)
token_words = [w for w in tokens if w.isalpha()]
return token_words
tickets['title_beschreibung_kommentare_tokenized'] = \
tickets.apply(identify_tokens, axis=1)

# 3.2. Entfernung von Datenschutz-Stoppwörtern
def remove_stops(row):
list = row['titel_beschreibung_tokenized']
titel_beschreibung_tokenized_no_ds_stop_words = [w for w in list
E-2
if not w in ds_stop_words_set]
return titel_beschreibung_tokenized_no_ds_stop_words
tickets['titel_beschreibung_tokenized_no_ds_stop_words'] = \
tickets.apply(remove_stops, axis=1)
def remove_stops(row):
list = row['title_beschreibung_kommentare_tokenized']
titel_beschreibung_kommentare_tokenized_no_ds_stop_words = [w
for w in list if not w in ds_stop_words_set]
return titel_beschreibung_kommentare_tokenized_no_ds_stop_words
tickets['titel_beschreibung_kommentare_tokenized_no_ds_stop_words'] = \
tickets.apply(remove_stops, axis=1)

# 3.3. Entfernung von deutschen Stoppwörter
def remove_stops(row):
list = \
row['titel_beschreibung_kommentare_tokenized_no_ds_stop_words']
titel_beschreibung_tokenized_no_de_stop_words = [w for w in list
if not w in de_stopwords]
return titel_beschreibung_tokenized_no_de_stop_words
tickets['titel_beschreibung_tokenized_no_de_stop_words'] = \
tickets.apply(remove_stops, axis=1)
def remove_stops(row):
list = \
row['titel_beschreibung_kommentare_tokenized_no_ds_stop_words']
titel_beschreibung_kommentare_tokenized_no_de_stop_words = [w
for w in list if not w in de_stopwords]
return titel_beschreibung_kommentare_tokenized_no_de_stop_words
tickets['titel_beschreibung_kommentare_tokenized_no_de_stop_words'] = \
tickets.apply(remove_stops, axis=1)
# 3.4. Entfernung von englischen Stoppwörter
def remove_stops(row):
list = \
row['titel_beschreibung_kommentare_tokenized_no_de_stop_words']
titel_beschreibung_tokenized_no_en_stop_words = [w for w in list
if not w in en_stopwords]
return titel_beschreibung_tokenized_no_en_stop_words
tickets['titel_beschreibung_tokenized_no_en_stop_words'] = \
tickets.apply(remove_stops, axis=1)
def remove_stops(row):
list = \
row['titel_beschreibung_kommentare_tokenized_no_de_stop_words']
titel_beschreibung_kommentare_tokenized_no_en_stop_words = [w
for w in list if not w in en_stopwords]
return titel_beschreibung_kommentare_tokenized_no_en_stop_words
tickets['titel_beschreibung_kommentare_tokenized_no_en_stop_words'] = \
tickets.apply(remove_stops, axis=1)

# 3.4. Tokens wieder zu Sätzen vervollständigen („join“)
def rejoin_words(row):
list = row['titel_beschreibung_tokenized_no_en_stop_words']
joined_words = ' '.join(list)
return joined_words
E-3
tickets['titel_beschreibung_anonymisiert'] = \
tickets.apply(rejoin_words, axis=1)
def rejoin_words(row):
list = \
row['titel_beschreibung_kommentare_tokenized_no_en_stop_words']
joined_words = ' '.join(list)
return joined_words
tickets['titel_beschreibung_kommentare_anonymisiert'] = \
tickets.apply(rejoin_words, axis=1)

# 4. Vorverarbeitete Daten als CSV speichern
tickets.to_csv('ticket_anonymized_nostopwords.csv', sep=';')
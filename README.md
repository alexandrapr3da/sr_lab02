# Laborator 2 - Sisteme de Recomandare (Integrare Recombee)

Acest repository conține rezolvarea pentru Laboratorul 2.

## Descrierea Dataset-ului

Pentru acest proiect a fost ales dataset-ul **[7k Books with Metadata](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata)**, preluat de pe platforma Kaggle.

Fișierul `books.csv` conține metadate detaliate pentru aproximativ 7.000 de cărți.

Din totalul coloanelor disponibile, am selectat și definit următoarele proprietăți în interfața Recombee pentru entitățile de tip *Item*:

* **`title`** (*String*): Titlul cărții.
* **`authors`** (*String*): Autorul sau autorii cărții.
* **`categories`** (*String*): Genul literar sau categoria din care face parte cartea.
* **`published_year`** (*Integer*): Anul în care a fost publicată ediția.
* **`average_rating`** (*Double*): Nota medie de evaluare oferită de cititori.
* **`num_pages`** (*Integer*): Numărul de pagini.
* **`description`** (*String*): Un scurt rezumat sau o descriere a cărții.

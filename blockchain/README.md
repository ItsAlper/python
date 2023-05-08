# BLOCKCHAIN - Uložiště
Kód bsahuje implementaci jednoduchého úložiště založeného na technologii blockchain v Pythonu. Lze ukládat data do bloků a řadit je do řetězce bloků. Uložiště používá proof-of-work algoritmus pro ověření nových bloků a pro bezpečnost dat.
Projekt obsahuje dvě třídy a to Block a Chain.

## Třída Block
index - index bloku v řetězci bloků

timestamp - datum a čas vytvoření bloku

data - data, která jsou ukládána do bloku

previous_hash - hash hodnota předchozího bloku v řetězci bloků

nonce - hodnota nonce pro ověření nového bloku

hash - hash hodnota aktuálního bloku

metoda -  calc_hash() - vypočítává hash hodnotu aktuálního bloku na základě jeho atributů

## Třída Chain
blocks - seznam bloků v řetězci bloků

difficulty - obtížnost vytváření nových bloků

metoda create_genesis_block() - vytváří první blok v řetězci bloků

metodu add_block(block) - přidává nový blok do řetězce bloků

metoda get_last_block() - vrátí poslední blok v řetězci bloků

metoda is_valid() - ověřuje platnost řetězce blok.


### Videa, která byla učebně nápomocná k dokonání úkolu
https://www.youtube.com/watch?v=pYasYyjByKI

https://www.youtube.com/watch?v=M576WGiDBdQ

https://www.youtube.com/watch?v=9LANHWWequw

https://www.youtube.com/watch?v=zovwM4jeYMk

https://www.youtube.com/watch?v=alNU9AVWkQk

https://www.investopedia.com/terms/p/proof-work.asp

Ještě bych se rád omluvil za pozdní odevzdání úkolu, časově jsem to nestíhal.

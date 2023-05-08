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
Třída Block obsahuje metodu calc_hash(), která vypočítá hash hodnotu aktuálního bloku na základě jeho atributů. Tato metoda se používá pro ověření nových bloků.

## Třída Chain
blocks - seznam bloků v řetězci bloků
difficulty - obtížnost vytváření nových bloků
Třída Chain obsahuje metodu create_genesis_block(), která vytvoří první blok v řetězci bloků, a metodu add_block(block), která přidá nový blok do řetězce bloků. Třída také obsahuje metodu get_last_block(), která vrátí poslední blok v řetězci bloků, a metodu is_valid(), která ověří platnost řetězce bloků.


### Videa, která byla učebně nápomocná k dokonání úkolu
https://www.youtube.com/watch?v=pYasYyjByKI
https://www.youtube.com/watch?v=M576WGiDBdQ
https://www.youtube.com/watch?v=9LANHWWequw
https://www.youtube.com/watch?v=zovwM4jeYMk
https://www.youtube.com/watch?v=alNU9AVWkQk
https://www.investopedia.com/terms/p/proof-work.asp

Ještě bych se rád omluvil za pozdní odevzdání úkolu, časově jsem to nestíhal. Má chyba.

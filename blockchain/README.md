# BLOCKCHAIN - Uložiště
Kód bsahuje implementaci jednoduchého úložiště založeného na technologii blockchain v Pythonu. Lze ukládat data do bloků a řadit je do řetězce bloků. Uložiště používá proof-of-work algoritmus pro ověření nových bloků a pro bezpečnost dat.
Projekt obsahuje dvě třídy a to Block a Chain.

## Třída Block
timestamp: časové razítko bloku

data: data uložená v bloku

previous_block: hash předchozího bloku v řetězci

nonce: číslo, které se používá k výpočtu hash hodnoty bloku

hash: hash hodnota bloku

## Třída Chain
create_genesis_block(): vytvoří a vrátí první blok v řetězci

add_block(data): přidá nový blok do řetězce s danými daty

get_last_block(): vrátí poslední blok v řetězci

is_valid(): ověří platnost celého řetězce

## UML Class diagram
https://cdn.discordapp.com/attachments/1027539954278076476/1105208189894533231/UML_blch.png

### Videa, která byla učebně nápomocná k dokonání úkolu
https://www.youtube.com/watch?v=pYasYyjByKI

https://www.youtube.com/watch?v=M576WGiDBdQ

https://www.youtube.com/watch?v=9LANHWWequw

https://www.youtube.com/watch?v=zovwM4jeYMk

https://www.youtube.com/watch?v=alNU9AVWkQk

https://www.investopedia.com/terms/p/proof-work.asp

Ještě bych se rád omluvil za pozdní odevzdání úkolu, časově jsem to nestíhal.

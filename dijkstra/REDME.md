# JEDNODUCHÝ POPIS KÓDU DIJKSTRA

Začátek - počáteční uzlel má hodnotu 0, dále přiřazujeme ostatním uzlům počáteční vzdálenost nekonečno.

Popořadě, tedy postupně, vybíráme uzly s nejmenší dosud zjištěnou vzdáleností.

Zkoumáme všechny sousedy, pakliže nalezneme kratší cestu aktualizujeme vzdálenosti.

Po zpracování všech sousedů vybraného uzlu jej odstraňujeme ze seznamu nezpracovaných uzlů.

Cílem je získat nejkratší vzdálenosti od počátečního uzlu ke všem ostatním uzlům v grafu.

## VÝSTUP

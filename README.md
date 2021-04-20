# Ohjelmistotuotanto harjoitustyö

Tälle sivulle tulee Helsingin yliopiston ohjelmistotuotanto-kurssin harjoitustyö, sekä laskuharjoitustehtävien vastauksia.

# Dungeon World -roolipelin hahmolomake

Ohjelman avulla on mahdollista luoda omia hahmoja Dungeon World -roolipeliin ja pitää kirjaa niiden taidoista.

[Lisätietoa Dungeon World -pelistä](https://dungeon-world.com/)

## Dokumentaatio

[Vaativuusmäärittely](https://github.com/hhautajarvi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/hhautajarvi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/hhautajarvi/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Python versiot

Toimivuus testattu Pythonin versiolla 3.8.5. Versiolla 3.6.9 testattaessa coverage ei toiminut.

## Ohjelman tilanne

Projektissa toimii tällä hetkellä käyttäjän ja hahmon luonti tekstikäyttöliittymässä ja ne voi tallentaa olemassaoleviin .json-tiedostoihin. Vanhan hahmon pelaaminen, uuden hahmoluokan luominen tai vanhan käyttäjän valinta eivät vielä toimi.

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Pylintin määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
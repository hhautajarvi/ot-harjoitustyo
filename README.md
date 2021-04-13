# Ohjelmistotuotanto harjoitustyö

Tälle sivulle tulee Helsingin yliopiston ohjelmistotuotanto-kurssin harjoitustyö, sekä laskuharjoitustehtävien vastauksia.

## Dokumentaatio

[Vaativuusmäärittely](https://github.com/hhautajarvi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/hhautajarvi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

## Python versiot

Toimivuus testattu Pythonin versiolla 3.8.5

## Ohjelman tilanne

Projektissa toimii tällä hetkellä käyttäjän ja hahmon luonti tekstikäyttöliittymässä.

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
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
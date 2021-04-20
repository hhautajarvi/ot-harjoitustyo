# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi tehdä Dungeon World -roolipeliin omalle hahmolleen lomakkeen, josta löytyy hahmon 
kyvyt ja taitojen tasot. Valmiiden hahmoluokkien lisäksi pelaaja voi luoda oman mukautetun luokkansa. 
Sovelluksen avulla hahmon kykyjä voi pelin aikana päivittää ja hahmon liikkeille voi myös "heittää noppaa".

[Linkki Dungeon World -peli kotisivuille josta löytyy pelistä lisätietoa](https://dungeon-world.com/)

## Suunnitellut toiminnallisuudet

### Aloitusruutu

* Käyttäjä voi tehtdä uuden käyttäjän tai valita vanhan käyttäjän (tehty)

### Hahmon valinta

* Käyttäjä voi luoda uudelle hahmolleen uniikin nimen jonka jälkeen siirrytään täyttämään hahmon kykyjä (tehty (ei tarkasta vielä onko uniikki))
* Käyttäjä voi valita listasta jonkin jo tekemistään hahmoista ja päivittää sen kykyjä pelin edessä 
* Käyttäjä voi luoda uuden hahmoluokan

### Uuden hahmon luominen

* Käyttäjä voi valita tekeekö hahmon valmiin hahmoluokan vai oman mukautetun luokan pohjalle (tehty)
* Hahmon tekemisessä hahmolle valitaan eettinen suuntaus, rotu ja kuuden pääkyvyn tasot (tehty)
* Hahmolle voi lisätä halutessaan taustatarinan, kuvauksen ulkonäöstä ja kuvan tiedostona (tehty)
* Hahmot tallennetaan tiedostoon (tehty)

### Uuden luokan luominen

* Käyttäjä antaa uudelle luokalle nimen ja kuvauksen. Luokalle annetaan myös osumapisteet (HP), tavaran 
kantokyky (load) ja hyökkäämiseen käytettävän nopan silmäluku (damage dice).
* Luokalle valitaan sopivat rodut ja niille omat kyvyt
* Luokalle valitaan sopivat eettiset suuntaukset ja niille omat kuvaukset
* Luokalle tehdään halutut aloitusliikkeet, sekä edistyneemmät liikkeet joita käyttäjä voi valita kerättyään 
tarpeeksi kokemusta. Edistyneemmät liikkeet ovat jaoteltu erikseen tasoille 2-5 ja 6-10. Näille liikkeille 
annetaan nimet ja kuvaukset.

### Hahmon pelaaminen

* Käyttäjä näkee hahmon kyvyt ja voi vielä muokata niitä haluamikseen, sekä pelin edetessä muuttaa esim. kokemus-
ja osumapisteitä
* Käyttäjä voi lisätä hahmonsa inventaarioon tavaraa ja kultaa. Tavaroille voi antaa kuvauksen ja painon ja mahdollisen
panssariarvon vaatteille tai aseille vahinkoarvon.
* Hahmolle voi lisätä oppimiaan uusia taitoja tai taikoja
* Hahmolleen voi "heittää noppaa". Käyttäjä voi valita tilanteen mukaan montaako ja minkä silmäluvun noppia heittää
* Hahmolle voi tehdä vapaita muistiinpanoja. 

## Prioriteetit

Pääpaino on saada toteutettua valmiit pelin perusluokat ja niillä toimiva hahmon pelaaminen.
Uusien luokkien luominen toteutetaan tämän jälkeen. Muita jatkokehitysideoita on esimerkiksi nopanheitto eri kyvyille
ja taidoille ja pelaajan kertoimien vaikutuksen laskeminen näihin nopanheittoihin suoraan.

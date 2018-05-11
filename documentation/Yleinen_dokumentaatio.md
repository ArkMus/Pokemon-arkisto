### Kuvaus
Projektin tavoitus olisi arkisto jota voisi käyttää samalla kuin pelaa alkuperäisiä pokemon pelejä. Käyttäjä voisi etsiä ja lisätä pokemoneja omaan kokoelmaan listasta joka sisältää kaikki alkuperäiset 151 pokemonta. Käyttäjän kokoelmassa voisi seurata mitkä pokemonit hän on saanut kiinni ja mitkä hän haluaisi saada.

### CRUD tietokannassa 
CRUD löytyy "collections" ja "pokemons" tauluista.

**collections**
Create: Käyttäjä voi lisätä pokemoneja omaan kokoelmaan "List of all the pokemon sivulta.

Read: Käyttäjälle näytetään oma kokoelma "Collection" sivulla.

Update: Käyttäjä voi vaihtaa nimejä pokemonille jotka on hänen kokoelmassa.

Delete: Käyttäjä voi poistaa pokemoneja hänen kokoelmasta.


**pokemons**
Create: Ylläpitäjä voi lisätä uusia pokemoneja.

Read: Kuka vaan voi nähdä listan kaikeista pokemoneista.

Update: Ylläpitäjä voi muokata pokemonien nimen ja numeron.

Delete: Ylläpitäjä voi poistaa pokemoneja.


### CREATE TABLE -lauseet
Jos tietokantaa ei ole olemassa, ohjelma luo ne käyttämällä seuraavat lauseet:

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);


CREATE TABLE pokemons (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	number VARCHAR(144) NOT NULL, 
	imglink VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);


CREATE TABLE collections (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	number VARCHAR(144) NOT NULL, 
	caught INTEGER NOT NULL, 
	imglink VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);


CREATE TABLE roles (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	role VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```

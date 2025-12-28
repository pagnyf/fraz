class Country {
  constructor(name, capital, population, language) {
    this.name = name;
    this.capital = capital;
    this.population = population;
    this.language = language;
  }

  displayProperties() {
    console.log(`Country: ${this.name}`);
    console.log(`Capital: ${this.capital}`);
    console.log(`Population: ${this.population}`);
    console.log(`Language: ${this.language}`);
  }
}

// Main
const usa = new Country(
  "United States",
  "Washington D.C.",
  331000000,
  "English",
);
usa.displayProperties();

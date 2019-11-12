class Country:
    def __init__(self, name, continent, pop, area):
        self._Name = name
        self._Population = int(pop)
        self._Area = area
        self._Continent = continent

    def __repr__(self):
        return self._Name + " in " + self._Continent

    def setPopulation(self, pop):
        self._Population = pop

    def getName(self):
        return self._Name

    def getArea(self):
        return self._Area

    def getPopulation(self):
        return self._Population

    def getContinent(self):
        return self._Continent

    def getPopDensity(self):
        return float(float(self._Population) / float(self._Area))

    def save(self, outobject):
        outobject.write(
            self._Name + "|" + self._Continent + "|" + str(self._Population) + "|" + str(self.getPopDensity()) + "\n")


# Create dictionary
class CountryCatalogue:
    def __init__(self, filename):
        self._cDictionary = dict()
        self._cCatalogue = dict()
        continents = open("continent.txt", "r") # Provides initial data set with the countries and their respective continents
        continents.readline()
        for line in continents:
            data1 = line.split(",")[0]
            data2 = line.strip("\n").split(",")[1]
            self._cDictionary[data1] = data2

        datafile = open("data.txt", "r") # Provides initial data set with countries and their respective population and area
        datafile.readline()
        for line in datafile:
            parts = line.strip("\n").split("|", 2)
            country = parts[0]
            population = parts[1].replace(",", "")
            area = parts[2].replace(",", "")
            c = Country(country, self._cDictionary[country], population, area)
            self._cCatalogue[c.getName()] = c

    def printCountryCatalogue(self):
        for c in self._cCatalogue:
            print(self._cCatalogue[c], "\n")

    def findCountry(self):
        c = input("Enter a country: ")
        flag = 0
        if c in self._cCatalogue:
            print("Country :", self._cCatalogue[c].getName(), "\nContinent : ", self._cCatalogue[c].getContinent(),
                  "\nPopulation : ", self._cCatalogue[c].getPopulation(), "\nArea : ", self._cCatalogue[c].getArea(), "\n")
        else:
            print("No country by name ", c, "exist in record.\n")

    def deleteCountry(self):
        c = input("Enter a country: ")
        if c in self._cDictionary:
            del self._cDictionary[c]
            del self._cCatalogue[c]
            print("Country : ", c, " is deleted successfully.\n")
        else:
            print("No country by name : ", c, "exist in records.\n")

    def addCountry(self):
        flag = 1
        while flag == 1:
            cName = input("Enter country name : ")
            population = int(input("Enter population : "))
            area = float(input("Enter area : "))
            continent = input("Enter continent : ")

            if cName in self._cDictionary:
                print("Country already in Catalogue you can’t add a country already in the catalogue.\n")
            else:
                flag = 0
                c = Country(cName, continent, population, area)
                self._cDictionary[cName] = continent
                self._cCatalogue[cName] = c
                self.saveCountryCatalogue()
                print("Country :", cName, "added", "successfully\n")


    def setPopulationOfASelectedCountry(self):
        cName = input("Enter the country name: ")
        newPop = int(input("What is the new population of the country ? ").strip())
        if cName in self._cCatalogue:
            c = self._cCatalogue[cName]
            c.setPopulation(newPop)
            self._cCatalogue[cName] = c
            print("Population density of :", cName, "is ", str(c.getPopDensity()), "\n")
        else:
            print("No country by name : ", cName, "exist in records.\n")

    def filterCountriesByContinent(self):
        c = input("Enter the name of the continent : ")

        for country in self._cDictionary:
            if self._cDictionary[country] == c:
                print(country)
        print("\n")

    def saveCountryCatalogue(self):
        file = open("data.txt", "w")
        countries = list()
        for c in self._cDictionary:
            countries.append(c)
        countries.sort()
        for country in countries:
            self._cCatalogue[country].save(file)
        file.close()

    def findCountryWithLargestPop(self):
        largest = -1
        c = ""
        for country in self._cCatalogue:
            if self._cCatalogue[country].getPopulation() > largest:
                largest = self._cCatalogue[country].getPopulation()
                c = country
        print("Country with highest population is :", c, "\n")

    def findCountryWithSmallestArea(self):
        smallest = -1
        c = ""
        # Initialize first value
        for country in self._cCatalogue:
            smallest = self._cCatalogue[country].getArea()
            c = country
            break

        for country in self._cCatalogue:
            if self._cCatalogue[country].getArea() < smallest:
                smallest = self._cCatalogue[country].getArea()
                c = country
        print("Country with smallest area is :", c, "\n")

    def findMostPopulousContinent(self):
        global continent
        populationOfContinent = dict()
        for country in self._cCatalogue:
            continent = self._cDictionary[country]
            if continent in populationOfContinent:
                populationOfContinent[continent] = populationOfContinent[continent] + self._cCatalogue[
                    country].getPopulation()
            else:
                populationOfContinent[continent] = self._cCatalogue[country].getPopulation()

        largest = -1
        for c in populationOfContinent:
            if populationOfContinent[c] > largest:
                largest = populationOfContinent[c]
                continent = c

        print("Continent with largest population is :", continent, " having population ",
              populationOfContinent[continent], "\n")

    def filterCountriesByPopDensity(self):
        lowerBound = float(input("Enter lower bound to population density : "))
        upperBound = float(input("Enter upper bound to population density : "))

        for c in self._cCatalogue:
            if lowerBound <= self._cCatalogue[c].getPopDensity() <= upperBound:
                print(c)

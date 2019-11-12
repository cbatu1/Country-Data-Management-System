from countryGalore import *


def main():

    # Function to present the options at the start of the program
    def runOptions():
        cc = CountryCatalogue('data.txt')

        # Function to allow user to select a new option without reprinting all the options to the terminal
        def selectOption():

            userInput = input("Please select an option and type the number: ")

            if userInput == "1":
                cc.findCountry()
                selectOption()
            elif userInput == "2":
                cc.addCountry()
                selectOption()
            elif userInput == "3":
                cc.deleteCountry()
                selectOption()
            elif userInput == "4":
                cc.findCountryWithSmallestArea()
                selectOption()
            elif userInput == "5":
                cc.findCountryWithLargestPop()
                selectOption()
            elif userInput == "6":
                cc.setPopulationOfASelectedCountry()
                selectOption()
            elif userInput == "7":
                cc.filterCountriesByContinent()
                selectOption()
            elif userInput == "8":
                cc.filterCountriesByPopDensity()
                selectOption()
            elif userInput == "9":
                cc.findMostPopulousContinent()
                selectOption()
            elif userInput == "10":
                cc.printCountryCatalogue()
                selectOption()
            elif userInput == "11":
                exit(main())
            else:
                print("Not a valid selection.\n")

        print("1. Find a country.")
        print("2. Add a country.")
        print("3. Delete a country.")
        print("4. Find the country with the smallest area.")
        print("5. Find the country with the largest population.")
        print("6. Set the population of a selected country.")
        print("7. Filter countries by continent.")
        print("8. Filter countries by population density.")
        print("9. Find the most populous continent.")
        print("10. Print the catalogue.")
        print("11. End the program.")

        selectOption()

    runOptions()


main()

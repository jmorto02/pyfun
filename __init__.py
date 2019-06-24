from pyfun.weather import Weather
from pyfun.wikipedia import Wikipedia
import re

w = Weather()
wi = Wikipedia()


def parse_command(command):
    if command.lower().strip() == 'weather':
        query = input("Enter a zipcode: ")
        data = w.get_by_zip_code(query)

        if data is None:
            raise Exception("Could not find weather data for that location.")

        current = data.weather[0]
        print(f"Currently the weather is {current.description}.")
        temp = int(float(data.main.temp - 273) * 1.8 + 32)
        print(f"Currently the temperature is {temp}ºF.")
        return 1

    elif command.lower().strip() == 'wiki':
        query = input("Enter something you want information about: ")
        data = wi.get_wiki_information(query)

        if data is None:
            raise Exception("Could not find information for that thing.")

        headline = data["query"]["pages"][list(data["query"]["pages"].keys())[0]]
        headline = re.sub('<[^<]+?>', '', headline["extract"]).replace('\n', '').replace('. ', '.\n')
        print(headline)
        return 1

    elif command.lower().strip() == 'exit':
        return 2

    else:
        print("Invalid command. Please enter 'Wiki' or 'Weather'")


while 1:
    command = input("Command: ")
    try:
        result = parse_command(command)
        if result == 2:
            break
    except Exception as e:
        print(f"No work. Exception: {str(e)}")

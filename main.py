# --------------------------------------------------------------------------------------------------------------------------------------------
# COVID CASES PROJECT
# --------------------------------------------------------------------------------------------------------------------------------------------
# Do a program in Python that processes a file with Rio Grande do Sul (RS) data about COVID-19, calculete and write:

# 1) total number of confirmed cases in RS (current and new)
# 2) total number of deaths in RS (current and new)
# 3) city with the most number of new cases in RS
# 4) city with lowest mortality numbers in RS
# 5) mean of new deaths in RS
# 6) bar plot with the incidence of cases in RS (five cities with the highest incidence)
# --------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt


# --------------------------------------------------------------------------------------------------------------------------------------------
# Reading the file
# --------------------------------------------------------------------------------------------------------------------------------------------
def readFile(name):
    file = open(name, encoding="utf-8")
    data = []
    for row in file:
        row1 = row[:-1]
        row2 = row1[
            1 : len(row1)
        ]  # removing the ',' in the begging of each row of the file
        data.append(row2)
    file.close()
    return data


# --------------------------------------------------------------------------------------------------------------------------------------------
# Write data of a list
# --------------------------------------------------------------------------------------------------------------------------------------------
def writeList(list):
    for item in list:
        print(item)


# --------------------------------------------------------------------------------------------------------------------------------------------
# Transforming e structuring the data in tuples
# --------------------------------------------------------------------------------------------------------------------------------------------
def transformingData(row):
    itens = row.split(",")
    itensTransformed = [
        itens[0]
    ]  # Municipality was included in the list before to not be convert to float
    count = 1
    # converting other itens to float
    while count < len(itens):
        itensTransformed.append(float(itens[count]))
        count += 1
    return itensTransformed


# --------------------------------------------------------------------------------------------------------------------------------------------
# List of list with data
# --------------------------------------------------------------------------------------------------------------------------------------------
def transformList(list):
    listOfItens = []
    count = 1  # skip the header
    # Take every row in the list and adds to other list
    while count < len(list):
        listOfItens.append(transformingData(list[count]))
        count += 1
    return listOfItens


# --------------------------------------------------------------------------------------------------------------------------------------------
# Confirmed cases
# --------------------------------------------------------------------------------------------------------------------------------------------
def totalConfirmed(list):
    confirmed = 0
    newConfirmed = 0
    for item in list:
        confirmed += item[1]
        newConfirmed += item[2]
    return confirmed + newConfirmed


# --------------------------------------------------------------------------------------------------------------------------------------------
# Death cases
# --------------------------------------------------------------------------------------------------------------------------------------------
def totalDeaths(list):
    deaths = 0
    newDeaths = 0
    for item in list:
        deaths += item[4]
        newDeaths += item[5]
    return deaths + newDeaths


# --------------------------------------------------------------------------------------------------------------------------------------------
# City with most new cases
# --------------------------------------------------------------------------------------------------------------------------------------------
def cityWithMostNewCases(list):
    city = list[0][0]
    most = list[0][2]
    for item in list:
        if item[2] > most:
            most = item[2]
            city = item[0]
    return city


# --------------------------------------------------------------------------------------------------------------------------------------------
# City with lowest mortality
# --------------------------------------------------------------------------------------------------------------------------------------------
def cityWithLessMortality(list):
    city = list[0][0]
    less = list[0][6]
    for item in list:
        if item[6] < less:
            less = item[6]
            city = item[0]
    return city


# --------------------------------------------------------------------------------------------------------------------------------------------
# Mean of new deaths
# --------------------------------------------------------------------------------------------------------------------------------------------
def meanNewDeaths(list):
    sum = 0
    for item in list:
        sum += item[5]
    return sum / len(list)


# --------------------------------------------------------------------------------------------------------------------------------------------
# Descending ordination using Bubble Sort
# --------------------------------------------------------------------------------------------------------------------------------------------
def orderByIncidence(cities, incidences):
    for i in range(
        len(incidences) - 1
    ):  # first loop repeates the oridination in the list
        for j in range(
            len(incidences) - 1 - i
        ):  # second loop makes the pairwise oridination until the penult element of the list
            # "-1" to not reach the limit of the list and compare the last element with the next that doesn't exist
            # -i discount the last position in each loop (starts in 0); assuming that the sort worked, the highest or lowest element will be in last position and so on
            if (
                incidences[j] < incidences[j + 1]
            ):  # comparing current position with the next
                aux = incidences[j]
                incidences[j] = incidences[j + 1]
                incidences[j + 1] = aux
                aux = cities[j]
                cities[j] = cities[j + 1]
                cities[j + 1] = aux


# --------------------------------------------------------------------------------------------------------------------------------------------
# Plot of incidences
# --------------------------------------------------------------------------------------------------------------------------------------------
def makePlot(cities, incidences, amount):
    cities2 = []
    incidences2 = []
    ind = 0
    while ind < amount:
        cities2.append(cities[ind])
        incidences2.append(incidences[ind])
        ind += 1
    plt.bar(cities2, incidences2)
    plt.title("Incidences by 100.000 inhabitants in RS")
    plt.xlabel("Cities")
    plt.ylabel("Incidences")
    plt.xticks(rotation=45)  # rotating labels 45 degrees
    plt.tight_layout()  # adjusting the plot
    plt.show()


# --------------------------------------------------------------------------------------------------------------------------------------------
# Searching for highest incidences
# --------------------------------------------------------------------------------------------------------------------------------------------
def treatIncidences(list, amount):
    cities = []
    incidences = []
    for item in list:
        cities.append(item[0])
        incidences.append(item[3])
    # print("\nPre-ordination")
    # print(cities)
    # print(incidences)
    orderByIncidence(cities, incidences)
    # print("\nPost-ordination")
    # print(cities)
    # print(incidences)
    makePlot(cities, incidences, amount)


# --------------------------------------------------------------------------------------------------------------------------------------------
# Main Program
# --------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    dataRaw = readFile("covid.csv")
    # writeList(dataRaw)
    header = dataRaw[0].split(",")
    # print(header)
    data = transformList(dataRaw)
    # writeList(data)

# --------------------------------------------------------------------------------------------------------------------------------------------
# 1) Total of confirmed cases
# --------------------------------------------------------------------------------------------------------------------------------------------
print(f"\nNumber of confirmed cases = {totalConfirmed(data):.0f}")
# --------------------------------------------------------------------------------------------------------------------------------------------
# 2) Total of deaths
# --------------------------------------------------------------------------------------------------------------------------------------------
print(f"Number of death cases = {totalDeaths(data):.0f}")
# --------------------------------------------------------------------------------------------------------------------------------------------
# 3) City with most new cases
# --------------------------------------------------------------------------------------------------------------------------------------------
print(f"The city with most new cases is{cityWithMostNewCases(data)}")
# --------------------------------------------------------------------------------------------------------------------------------------------
# 4) City with lowest mortality
# --------------------------------------------------------------------------------------------------------------------------------------------
print(f"The city with lowest mortality is{cityWithLessMortality(data)}")
# --------------------------------------------------------------------------------------------------------------------------------------------
# 5) Mean of new deaths
# --------------------------------------------------------------------------------------------------------------------------------------------
print(f"Mean of new deaths = {meanNewDeaths(data):.2f}\n")
# --------------------------------------------------------------------------------------------------------------------------------------------
# 6) Total of confirmed cases
# --------------------------------------------------------------------------------------------------------------------------------------------
treatIncidences(data, 5)

import requests
from zipfile import ZipFile
import pandas
import pprint

# Excel example data from https://www.contextures.com/xlsampledata01.html

r = requests.get('https://api.github.com/repos/jafedor/OrderDataAnalysis/zipball/main')
print(r.status_code)
# print(r.headers)
# print(r.content)

file_name = "datafile.zip"

with open(file_name, 'wb') as out:
    out.write(r.content)

with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')

excel_data_df = pandas.read_excel('jafedor-OrderDataAnalysis-205f624/ItemOrderData.xlsx', sheet_name='Orders')


# Prints the name of the person who spent the most and their total spent
def find_biggest_spender(df):
    person_totals = {}

    # Gather total spent for each person and store it in person_totals dictionary
    for row in range(0, len(df.index)):
        name = str(df.iloc[int(row)]['Name'])
        total_spent = float(df.iloc[int(row)]['Total'])
        # print(total_spent)

        if name not in person_totals:  # if this name hasn't been added to dict yet
            person_totals[name] = total_spent
        else:  # if this total should be added to previous total for this person
            person_totals[name] += total_spent

    # print(person_totals)
    max_spender = max(person_totals, key=person_totals.get)
    print(f'{max_spender} spent the most, spending ${person_totals[max_spender]}!')


# Prints the most popular item purchased in each region.
def find_top_items_per_region(df):
    units_ordered_totals = {'East': {}, 'Central': {}, 'West': {}}

    # Loop through the dataframe and fill in dictionary containing totals for each unit ordered in each region
    for row in range(0, len(df.index)):
        region = str(df.iloc[int(row)]['Region'])
        item = str(df.iloc[int(row)]['Item'])
        units_in_order = int(df.iloc[int(row)]['Units'])

        if item not in units_ordered_totals[region]:
            units_ordered_totals[region][item] = units_in_order
        else:
            units_ordered_totals[region][item] += units_in_order

    # print a nicely formatted dictionary displaying items ordered per region
    # printer = pprint.PrettyPrinter(width=30)
    # printer.pprint(units_ordered_totals)

    # Calculate the key with the max value for each region 
    for region in units_ordered_totals.keys():
        top_item = max(units_ordered_totals[region], key=units_ordered_totals[region].get)
        print(f'The most popular item in the {region} region was a {top_item}!')


# Who spent the most money and how much did they spend?
find_biggest_spender(excel_data_df)

# What were the most popular items ordered in each region?
find_top_items_per_region(excel_data_df)

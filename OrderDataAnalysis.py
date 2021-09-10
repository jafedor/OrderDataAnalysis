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
    info_dict = {}

    # Gather total spent for each person and store it in info_dict
    for row in range(0, len(df.index)):
        name = str(df.iloc[int(row)]['Name'])
        total_spent = float(df.iloc[int(row)]['Total'])
        # print(total_spent)

        if name not in info_dict:  # if this name hasn't been added to dict yet
            info_dict[name] = total_spent
        else:  # if this total should be added to previous total for this person
            info_dict[name] += total_spent

    # print(info_dict)
    max_spender = max(info_dict, key=info_dict.get)
    print(f'{max_spender} spent the most, spending ${info_dict[max_spender]}!')


# What were the most popular items ordered in each region?
def find_top_items_per_region(df):
    ans_dict = {'East': {}, 'Central': {}, 'West': {}}

    for row in range(0, len(df.index)):
        region = str(df.iloc[int(row)]['Region'])
        item = str(df.iloc[int(row)]['Item'])
        units_in_order = int(df.iloc[int(row)]['Units'])

        if item not in ans_dict[region]:
            ans_dict[region][item] = units_in_order
        else:
            ans_dict[region][item] += units_in_order

    # print a nicely formatted dictionary displaying items ordered per region
    # printer = pprint.PrettyPrinter(width=30)
    # printer.pprint(ans_dict)

    for region in ans_dict.keys():
        top_item = max(ans_dict[region], key=ans_dict[region].get)
        print(f'The most popular item in the {region} region was a {top_item}!')


find_biggest_spender(excel_data_df)
find_top_items_per_region(excel_data_df)

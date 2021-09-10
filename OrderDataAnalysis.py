import requests
import pandas
import pprint

# Use an HTTP get request with GitHub's API to download a spreadsheet from my GitHub repo
r = requests.get('https://raw.githubusercontent.com/jafedor/OrderDataAnalysis/main/ItemOrderData.xlsx')
print(r.status_code)
# print(f'{r.headers}\n{r.content}')

order_file_name = "ItemOrderData.xlsx"  # the name of the file that will hold the spreadsheet data

# Write the data retrieved from the get request to an Excel file for easier access
with open(order_file_name, 'wb') as out:
    out.write(r.content)

# Read the Excel file into a pandas dataframe for parsing
excel_data_df = pandas.read_excel('ItemOrderData.xlsx', sheet_name='Orders')


# Prints the name of the person who spent the most and their total spent
def find_biggest_spender(df):
    person_totals = {}  # contains the total amount spent for each person

    # Gather total spent for each person and store it in person_totals dictionary
    for row in range(0, len(df.index)):
        name = str(df.iloc[int(row)]['Name'])
        total_spent = float(df.iloc[int(row)]['Total'])

        if name not in person_totals:  # if this name hasn't been added to dict yet
            person_totals[name] = total_spent
        else:  # if this total should be added to previous total for this person
            person_totals[name] += total_spent

    # print(person_totals)
    max_spender = max(person_totals, key=person_totals.get)
    print(f'{max_spender} spent the most, spending ${person_totals[max_spender]}!')


# Prints the most popular item purchased in each region
def find_top_items_per_region(df):
    # contains the total units ordered of each item for each region
    units_ordered_totals = {'East': {}, 'Central': {}, 'West': {}}

    # Loop through the dataframe and fill in the 'units_ordered_totals' dictionary accordingly
    for row in range(0, len(df.index)):
        region = str(df.iloc[int(row)]['Region'])
        item = str(df.iloc[int(row)]['Item'])
        units_in_order = int(df.iloc[int(row)]['Units'])

        if item not in units_ordered_totals[region]: # if this item hasn't been added to dictionary for this region yet
            units_ordered_totals[region][item] = units_in_order
        else:  # if this order's units should be added to previous total units for this item in this region
            units_ordered_totals[region][item] += units_in_order

    # Calculate the key with the max value for each region 
    for region in units_ordered_totals.keys():
        top_item = max(units_ordered_totals[region], key=units_ordered_totals[region].get)
        print(f'The most popular item in the {region} region was a {top_item}!')

    # print a nicely formatted dictionary displaying items ordered per region (for answer checking purposes)
    # printer = pprint.PrettyPrinter(width=30)
    # printer.pprint(units_ordered_totals)


# Who spent the most money and how much did they spend?
find_biggest_spender(excel_data_df)

# What were the most popular items ordered in each region?
find_top_items_per_region(excel_data_df)

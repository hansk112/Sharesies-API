import json
import pandas as pd
import csv

# /home/hans/sharesies/Sharesies-API

# Reading JSON data from a file
with open("/home/hans/sharesies/Sharesies-API/portfolio.json") as f:
    json_data = json.load(f)

to_csv = json_data

print(json_data[0].keys())
keys = json_data[0].keys()

with open("/home/hans/sharesies/Sharesies-API/portfolio_output.csv", "w") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(to_csv)

# print(type(json_data))
# print(json_data)
# Converting JSON data to a pandas DataFrame
# df = pd.read_json(json_data)

# # Writing DataFrame to a CSV file
# df.to_csv("/home/hans/sharesies/Sharesies-API/portfolio_output.csv", index=False)

# print("Data has been written to "+
#       "/home/hans/sharesies/Sharesies-API/"+
#       "portfolio portfolio_output.csv")
import os, json
import math
import csv

import numpy as np
import matplotlib.pyplot as plt

stars = []
num_of_commits = []
num_of_contributors = []
age = []
counter = 0
# data = [['name', 'stars', 'contributors', "last_commit", "age"]]
data = []

path_to_dir = './'

total_json = {}

json_files = [pos_json for pos_json in os.listdir(path_to_dir) if pos_json.endswith('.json')]

for json_file in json_files:
    total_json = {**total_json, **json.load(open(json_file))}

with open("data.json", "w",  encoding='utf-8') as f:
    json.dump(total_json, f, ensure_ascii=False, indent=4)

    # for k, v in json_obj.items():
    #     try:
    #         star = v["info"]["stargazers_count"]
    #         contributors = len(v["contributors"])
    #         last_commits = v["commits"][0]["commit"]["author"]["date"]
    #         age = v['info']['created_at']
    #         data.append([k, star, contributors, last_commits, age])
    #     except:
    #         counter += 1

# stars = sorted(stars)

# print(len(json_obj) - counter)
# plt.hist(stars, facecolor='gray', align='mid', bins='auto', edgecolor='black', log=True)
# plt.show()
#
# print(f"AVG: {sum(stars) / len(stars)}")
# print(f"MAX: {max(stars)}")
# print(f"MIN: {min(stars)}")
# print(f"TOP 1%: {stars[math.ceil(len(stars) * 0.99)]}")

# with open("data.csv", 'a+', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     # Write each row
#     for row in data:
#         writer.writerow(row)

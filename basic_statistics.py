import json
import math
import csv

import numpy as np
import matplotlib.pyplot as plt

stars = []
num_of_commits = []
num_of_contributors = []
age = []
counter = 0
data = [['name', 'stars', 'contributors', "last_commit", "age"]]

json_obj = json.load(open('data.json'))

for k, v in json_obj.items():
    try:
        star = v["info"]["stargazers_count"]
        contributors = len(v["contributors"])
        last_commits = v["commits"][0]["commit"]["author"]["date"]
        age = v['info']['created_at']
        data.append([k, star, contributors, last_commits, age])
    except:
        counter += 1

stars = sorted(stars)

# print(len(json_obj) - counter)
# plt.hist(stars, facecolor='gray', align='mid', bins='auto', edgecolor='black', log=True)
# plt.show()
#
# print(f"AVG: {sum(stars) / len(stars)}")
# print(f"MAX: {max(stars)}")
# print(f"MIN: {min(stars)}")
# print(f"TOP 1%: {stars[math.ceil(len(stars) * 0.99)]}")

with open("data.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write each row
    for row in data:
        writer.writerow(row)
import requests
import json
import time
from alive_progress import alive_bar
from datetime import datetime
import argparse

import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
headers = {'Authorization': f'token {token}'}

parser = argparse.ArgumentParser()
parser.add_argument('--srow', action="store", dest='srow', default=0)
parser.add_argument('--erow', action="store", dest='erow', default=0)

args = parser.parse_args()

def get_details(tuple):
    owner = tuple[0]

    repo = tuple[1]
    # Get basic repository information
    repo_info_url = f'https://api.github.com/repos/{owner}/{repo}'
    response = requests.get(repo_info_url, headers=headers)
    repo_info = response.json()

    # Get contributors
    contributors_url = f'https://api.github.com/repos/{owner}/{repo}/contributors'
    response = requests.get(contributors_url, headers=headers)
    contributors = response.json()

    # Get commits
    commits_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(commits_url, headers=headers)
    commits = response.json()
    return repo_info, contributors, commits


if __name__ == "__main__":

    repos = []
    output = {}
    counter = 1

    start_row_num = int(args.srow)
    end_row = int(args.erow)

    print(f"START TIME: {datetime.now()}")

    with open('reuse_repository.csv', 'r') as repos_file:
        with alive_bar(end_row) as bar:
            row = repos_file.readline()
            while row and counter <= end_row:
                try:
                    if counter > start_row_num:
                        start = time.time()
                        columns = row.split(",")
                        info_tuple = (columns[1], columns[2])
                        repo_url = columns[3].strip()
                        output[repo_url] = {}
                        output[repo_url]["info"], output[repo_url]["contributors"], output[repo_url][
                            "commits"] = get_details(info_tuple)
                        end = time.time()
                        time_spent = end - start
                        if time_spent > 2.2:
                            pass
                        else:
                            time_sleep = (2.2 - time_spent)
                            time.sleep(time_sleep)

                except Exception as e:
                    print(e)
                row = repos_file.readline()
                counter += 1
                bar()

                if counter % 1000 == 0 and counter > start_row_num:
                    filename = 'data_' + str(counter / 1000) + '.json'
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(output, f, ensure_ascii=False, indent=4)
                        print(f"FILE {filename} saved")
                        output = {}

        filename = "last_bucket"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=4)
            print(f"FILE {filename} saved")
            output = {}

    print(f"END TIME: {datetime.now()}")

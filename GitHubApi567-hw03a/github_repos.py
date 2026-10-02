import json

import requests


def get_repositories(user):
    response = requests.get("https://api.github.com/users/" + user + "/repos")
    repositories = json.loads(response.text)
    results = []

    for repository in repositories:
        name = repository["name"]
        response = requests.get("https://api.github.com/repos/" + user + "/" + name + "/commits")
        commits = json.loads(response.text)
        results.append("Repo: " + name + " Number of commits: " + str(len(commits)))

    return results


if __name__ == "__main__":
    user = input("GitHub user ID: ")
    for result in get_repositories(user):
        print(result)

import urllib
import requests
import os


API_BASE_URL = "https://circleci.com/api/v1.1/"
GREEN = "✔️"
RED = "❌"
GREY = "⚪"


def get_token():
    with open(os.path.join(os.getcwd(), ".statusci")) as f:
        return f.read().strip()


def get_status(status):
    if status in ["success", "fixed"]:
        return GREEN
    elif status in ["failed", "timedout"]:
        return RED
    return GREY


def main():
    token = get_token()
    url = f"{API_BASE_URL}recent-builds"
    params = {"circle-token": token}
    response = requests.get(url, params=params)
    content = response.json()
    displayed = []
    for build in content:
        repo = f"{build['username']}/{build['reponame']}/{build['branch']}"
        if repo in displayed:
            continue

        status = get_status(build["status"])
        print(f"{status} {repo}")
        displayed.append(repo)


if __name__ == "__main__":
    main()

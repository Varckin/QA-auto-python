import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = "https://api.github.com"
REPO_NAME = os.getenv('REPO_NAME')
USERNAME = os.getenv('GITHUB_USERNAME')
TOKEN = os.getenv('GITHUB_TOKEN')

def create_repo():
    response = requests.post(
        f"{GITHUB_API_URL}/user/repos",
        auth=(USERNAME, TOKEN),
        json={"name": REPO_NAME, "private": False}
    )
    response.raise_for_status()
    return response.json()

def check_repo_exists():
    response = requests.get(
        f"{GITHUB_API_URL}/user/repos",
        auth=(USERNAME, TOKEN)
    )
    response.raise_for_status()
    repos = response.json()
    return any(repo['name'] == REPO_NAME for repo in repos)

def delete_repo():
    response = requests.delete(
        f"{GITHUB_API_URL}/repos/{USERNAME}/{REPO_NAME}",
        auth=(USERNAME, TOKEN)
    )
    response.raise_for_status()

def main():
    create_repo()
    assert check_repo_exists()
    delete_repo()
    assert not check_repo_exists()

if __name__ == "__main__":
    main()

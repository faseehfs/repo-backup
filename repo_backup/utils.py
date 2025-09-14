import requests
import os
from datetime import datetime


def repo_exists(repo_url):
    parts = repo_url.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]
    r = requests.get(f"https://api.github.com/repos/{owner}/{repo}")
    return r.status_code == 200


def path_from_name(config, repo_name):
    folder_name = f"{repo_name}-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.git"
    return os.path.join(config["backup_directory"], folder_name)


def url_from_name(config, repo_name):
    return f"https://{config['pat']}@github.com/{config['github_username']}/{repo_name}.git"

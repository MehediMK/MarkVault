# blog/github_utils.py
from github import Github, Auth
from decouple import config


def fetch_from_github():
    BRANCH_NAME = config("BRANCH_NAME")
    GITHUB_TOKEN = config("GITHUB_TOKEN")    
    REPO_NAME = config("REPO_NAME")
    
    auth = Auth.Token(GITHUB_TOKEN)
    g = Github(auth=auth)
    repo = g.get_user().get_repo(REPO_NAME)
    files = repo.get_contents("blogs", ref=BRANCH_NAME)
    
    blogs = []
    for file in files:
        if file.path.endswith(".md") or file.path.endswith(".json"):
            content = repo.get_contents(file.path, ref=BRANCH_NAME).decoded_content.decode()
            blogs.append({"file_name": file.path, "content": content})
    return blogs


def push_to_github(file_path):
    BRANCH_NAME = config("BRANCH_NAME")
    GITHUB_TOKEN = config("GITHUB_TOKEN")    
    REPO_NAME = config("REPO_NAME")
    
    auth = Auth.Token(GITHUB_TOKEN)
    g = Github(auth=auth)
    repo = g.get_user().get_repo(REPO_NAME)

    with open(file_path, "r") as file:
        content = file.read()

    file_name = file_path.split("\\")[-1]
    repo.create_file(f"blogs/{file_name}", f"Add {file_name}", content, branch=BRANCH_NAME)

# blog/github_utils.py
from github import Github, Auth
from decouple import config

# git variables here...
BRANCH_NAME = config("BRANCH_NAME")
GITHUB_TOKEN = config("GITHUB_TOKEN")    
REPO_NAME = config("REPO_NAME")


def get_git_repo(git_token: str, repo_name: str):
    """Get a git repository object from github 
    params::
        git_token: github token
        repo_name: repository name
    """
    
    auth = Auth.Token(git_token)
    git = Github(auth=auth)
    repo = git.get_user().get_repo(repo_name)
    
    return repo


def fetch_from_github(file_location):
    
    repo = get_git_repo(GITHUB_TOKEN, REPO_NAME)
    
    files = repo.get_contents(f"{file_location}", ref=BRANCH_NAME)
    
    blogs = []
    for file in files:
        if file.path.endswith(".md") or file.path.endswith(".json"):
            content = repo.get_contents(file.path, ref=BRANCH_NAME).decoded_content.decode()
            blogs.append({"file_name": file.path, "content": content})
    return blogs


def push_to_github(file_location, file_name, content):
    
    repo = get_git_repo(GITHUB_TOKEN, REPO_NAME)

    try:
        # Check if file exists, if so, update it
        file = repo.get_contents(f"blogs/{file_name}")
        repo.update_file(file.path, "Updated blog post", content, file.sha)
    except:
        # If file doesn't exist, create a new one
        repo.create_file(f"{file_location}/{file_name}", "New blog post created.", content, branch=BRANCH_NAME)
        
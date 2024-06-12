import os


def check_repo_secrets(repo_secrets):
    repo_status = True
    for secret in repo_secrets:
        if os.environ.get(secret) is None:
            repo_status = False
    return repo_status

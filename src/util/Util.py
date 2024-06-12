import os


def check_repo_secrets(repo_secrets):
    repo_status = True
    for secret in repo_secrets:
        if os.environ.get(secret) is None:
            print(f"# 仓库密钥 {secret} 未配置")
            repo_status = False
    return repo_status

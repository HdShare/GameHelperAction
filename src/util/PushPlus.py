import json
import os

import requests


def send(title, content):
    requests.post(
        "https://www.pushplus.plus/send",
        data=json.dumps(
            {
                "token": os.environ.get("pushplus_token"),
                "title": title,
                "content": content
            }
        ).encode(encoding="utf-8"),
        headers={"Content-Type": "application/json"}
    )

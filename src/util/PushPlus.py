import json
import os
import traceback

import requests


def send(title, content):
    try:
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
    except Exception as e:
        print(f"推送{title}异常: {e}")
        traceback.print_exc()

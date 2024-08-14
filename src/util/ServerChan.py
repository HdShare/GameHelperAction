import json
import os
import traceback

import requests


def send(text, desp):
    try:
        requests.post(
            f'https://sctapi.ftqq.com/{os.environ.get("serverchan_token")}.send',
            data=json.dumps(
                {
                    "text": text,
                    "desp": desp.replace("\n", "\n\n")
                }
            ).encode(encoding="utf-8"),
            headers={"Content-Type": "application/json"}
        )
    except Exception as e:
        print(f"推送{text}异常: {e}")
        traceback.print_exc()

import os
import traceback

import requests


def post_api_json(api, json_data):
    try:
        resp = requests.post(
            url="https://kohcamp.qq.com" + api,
            json=json_data,
            headers={
                "userId": os.environ["smoba_userId"],
                "token": os.environ["smoba_token"],
            }
        )
        resp_json = resp.json()
        if resp_json["returnCode"] == 0:
            return resp_json
        else:
            print(resp_json["returnMsg"])
            return None
    except Exception as e:
        print(f"接口{api}异常: {e}")
        traceback.print_exc()
        return None


def post_api_data(api, param_data):
    try:
        resp = requests.post(
            url="https://ssl.kohsocialapp.qq.com:10001" + api,
            data={
                "gameId": 20001,
                "userId": os.environ["smoba_userId"],
                "token": os.environ["smoba_token"],
                **param_data
            }
        )
        resp_json = resp.json()
        if resp_json["returnCode"] == 0:
            return resp_json
        else:
            print(resp_json["returnMsg"])
            return None
    except Exception as e:
        print(f"接口{api}异常: {e}")
        traceback.print_exc()
        return None


def post_api_native(name, data):
    try:
        resp = requests.post(
            url="https://yxzjfaas.native.qq.com/backend_polaris/?namespace=Faas&pdr_appid=3732&fn=" + name,
            json={
                "data": data,
                "base": {
                    "userinfo": {
                        "sPartition": "1277",
                        "sMSDKUrlParam": os.environ["smoba_sMSDKUrlParam"],
                        "sOpenId": os.environ["smoba_sOpenId"],
                        "sCampUserId": os.environ["smoba_sCampUserId"],
                    },
                    "pdr_app_ver": "lastest_gray",
                }
            },
        )
        resp_json = resp.json()
        if resp_json["code"] == 0:
            if resp_json["data"]["code"] == 0:
                return resp_json
            else:
                print(resp_json["data"]["message"])
                return None
        else:
            print(resp_json["message"])
            return None
    except Exception as e:
        print(f"接口{name}异常: {e}")
        traceback.print_exc()
        return None

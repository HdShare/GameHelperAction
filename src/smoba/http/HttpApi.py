import os

from src.smoba.http import HttpUtil


def task_list():
    resp_json = HttpUtil.post_api_json(
        "/operation/action/tasklist",
        {}
    )
    return resp_json


def task_reward(task_id):
    resp_json = HttpUtil.post_api_json(
        "/operation/action/rewardtask",
        {
            "taskIds": task_id,
        }
    )
    return resp_json


def info_list():
    resp_json = HttpUtil.post_api_json(
        "/info/listinfov2",
        {
            "channelId": "25818",
        }
    )
    return resp_json


def info_like(info_id, status):
    resp_json = HttpUtil.post_api_data(
        "/user/addlike",
        {
            "iInfoId": info_id,
            "like": status,
        }
    )
    return resp_json


def info_detail(info_id):
    resp_json = HttpUtil.post_api_data(
        "/game/detailinfov3",
        {
            "iInfoId": info_id,
        }
    )
    return resp_json


def signin():
    resp_json = HttpUtil.post_api_json(
        "/operation/action/newsignin",
        {
            "roleId": os.environ["roleId"],
        }
    )
    return resp_json


def play_task_data(task_type):
    resp_json = HttpUtil.post_api_data(
        "/play/gettaskconditiondata",
        {
            "type": task_type,
        }
    )
    return resp_json

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


def list_info_moment():
    resp_json = HttpUtil.post_api_json(
        "/info/listinfov2",
        {
            "channelId": "25818",
        }
    )
    return resp_json


def like_info(info_id, status):
    resp_json = HttpUtil.post_api_data(
        "/user/addlike",
        {
            "iInfoId": info_id,
            "like": status,
        }
    )
    return resp_json


def like_moment(moment_id, status):
    resp_json = HttpUtil.post_api_json(
        "/moment/like",
        {
            "momentId": moment_id,
            "isLike": status,
        }
    )
    return resp_json


def detail_info(info_id):
    resp_json = HttpUtil.post_api_data(
        "/game/detailinfov3",
        {
            "iInfoId": info_id,
        }
    )
    return resp_json


def detail_post(info_id):
    resp_json = HttpUtil.post_api_data(
        "/game/detailinfobbs",
        {
            "iInfoId": info_id,
        }
    )
    return resp_json


def detail_moment(moment_id):
    resp_json = HttpUtil.post_api_json(
        "/campcontent/detail",
        {
            "content_id": moment_id,
        }
    )
    return resp_json


def signin():
    resp_json = HttpUtil.post_api_json(
        "/operation/action/newsignin",
        {
            "roleId": os.environ["smoba_roleId"],
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


def records_list(page_size, record_type):
    resp_json = HttpUtil.post_api_json(
        "/records/getlist",
        {
            "pageSize": page_size,
            "type": record_type,
        }
    )
    return resp_json


def camp_get_task_list():
    resp_json = HttpUtil.post_api_native(
        "campGetTaskList",
        {}
    )
    return resp_json


def camp_get_task_reward():
    resp_json = HttpUtil.post_api_native(
        "campGetTaskReward",
        {}
    )
    return resp_json


def camp_set_task_finish_count():
    resp_json = HttpUtil.post_api_native(
        "campSetTaskFinishCount",
        {
            "taskIds": []
        }
    )
    return resp_json


def bbs_sign(bbs_id):
    resp_json = HttpUtil.post_api_data(
        "/moment/bbssign",
        {
            "bbsId": bbs_id,
        }
    )
    return resp_json

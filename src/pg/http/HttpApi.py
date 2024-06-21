import json

from src.pg.http import HttpUtil


def signin():
    resp_json = HttpUtil.post_h5api(
        "/act_dailysigninmonthly.php",
        {}
    )
    return resp_json


def like_records():
    resp_json = HttpUtil.post_api(
        "/user/likerecords",
        {}
    )
    return resp_json


def task_list():
    resp_json = HttpUtil.post_h5api(
        "/act_getscoretasklist.php",
        {}
    )
    return resp_json


def gift_receive(gift_id):
    resp_json = HttpUtil.post_h5api(
        "/act_receivelivenessgift.php",
        {
            "giftId": gift_id,
        }
    )
    return resp_json


def task_complete(task_id):
    resp_json = HttpUtil.post_h5api(
        "/completescoretask.php",
        {
            "taskId": task_id,
        }
    )
    return resp_json


def welfare_list():
    resp_json = HttpUtil.post_h5api(
        "/activity/welfare/tasklist.php",
        {}
    )
    return resp_json


def welfare_complete(task_index):
    resp_json = HttpUtil.post_h5api(
        "/activity/welfare/completetask.php",
        {
            "taskIndex": task_index,
        }
    )
    return resp_json


def page_info():
    resp_json = HttpUtil.post_api(
        "/game/infomainpage",
        {
            "type": "51005184",
            "pos1": "2",
            "sort": "2",
            "page": "1",
        }
    )
    return resp_json


def like_info(info_id, status):
    resp_json = HttpUtil.post_api(
        "/user/addlike",
        {
            "iInfoId": info_id,
            "like": status,
        }
    )
    return resp_json


def page_moment():
    resp_json = HttpUtil.post_api(
        "/moment/squaretagmoments",
        {
            "tagId": "1",
        }
    )
    return resp_json


def like_moment(moment_id, status):
    resp_json = HttpUtil.post_api(
        "/moment/like",
        {
            "momentId": moment_id,
            "type": status,
        }
    )
    return resp_json


def module_report(ext_data):
    resp_json = HttpUtil.post_api(
        "/game/batchmodulelogreport",
        {
            "extData": json.dumps(ext_data),
        }
    )
    return resp_json


def game_tool(tool_id, status):
    resp_json = HttpUtil.post_api(
        "/play/gametoolchange",
        {
            "id": tool_id,
            "status": status,
        }
    )
    return resp_json


def share(action, action_id):
    resp_json = HttpUtil.post_api(
        "/user/sharecallback",
        {
            "action": action,
            "id": action_id,
        }
    )
    return resp_json

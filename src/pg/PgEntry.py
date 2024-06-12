import os
from datetime import datetime

from src.pg.http import HttpApi
from src.util import PushPlus
from src.util import Util

send_content = ""


def signin():
    global send_content
    resp_json = HttpApi.signin()
    if resp_json is not None:
        send_content += ">签到成功"
    else:
        send_content += ">签到失败"


def do_task_list():
    global send_content
    resp_json = HttpApi.task_list()
    if resp_json is not None:
        send_content += ">获取任务列表成功"
        task_list = resp_json["data"]["taskList"]
        for task in task_list:
            task_id = task["taskId"]
            task_detail = task["detailDesc"]
            task_status = task["status"]
            if task_status == 0:
                task_complete(task_id, task_detail)
            elif task_status == 2:
                HttpApi.task_complete(task_id)
    else:
        send_content += ">获取任务列表失败"


def task_complete(task_id, task_detail):
    global send_content
    if task_id == 26:
        # print("本日通过和平营地启动1次游戏")
        send_content += f">任务失败(无法完成): {task_id}-{task_detail}"
    elif task_id == 27:
        # print("本日取胜1局计分模式（前五）")
        send_content += f">任务失败(无法完成): {task_id}-{task_detail}"
    elif task_id == 28:
        # print("本日为资讯点赞3次")
        page_info = HttpApi.page_info()
        if page_info is not None:
            like_count = 0
            for i in range(3):
                if HttpApi.like_info(page_info["data"]["list"][i]["iInfoId"], "1") is not None:
                    like_count += 1
            if like_count == 3:
                send_content += f">任务成功: {task_id}-{task_detail}"
                HttpApi.task_complete(task_id)
            else:
                send_content += f">任务失败(点赞异常): {task_id}-{task_detail}"
        else:
            send_content += f">任务失败(资讯异常): {task_id}-{task_detail}"
    elif task_id == 29:
        # print("本日为动态点赞3次")
        page_moment = HttpApi.page_moment()
        if page_moment is not None:
            like_count = 0
            for i in range(3):
                if HttpApi.like_moment(page_moment["data"]["list"][i]["momentId"], "1") is not None:
                    like_count += 1
            if like_count == 3:
                send_content += f">任务成功: {task_id}-{task_detail}"
                HttpApi.task_complete(task_id)
            else:
                send_content += f">任务失败(点赞异常): {task_id}-{task_detail}"
        else:
            send_content += f">任务失败(动态异常): {task_id}-{task_detail}"
    elif task_id == 30:
        # print("本日浏览资讯5分钟")
        ext_data = [{
            "reportInterval": 5,
            "eventId": 100004,
            "subModuleId": 27,
            "page": 101004,
            "moduleId": 1
        }] * 12
        module_report(ext_data, task_id, task_detail)
    elif task_id == 31:
        # print("本日观看直播5分钟")
        ext_data = [{
            "reportInterval": 5,
            "eventId": 10901001,
            "subModuleId": 1,
            "page": 109002,
            "moduleId": 9
        }] * 12
        module_report(ext_data, task_id, task_detail)
    elif task_id == 33:
        # print("本周启用游戏工具至少一个")
        if HttpApi.game_tool("4", "1") is not None:
            send_content += f">任务成功: {task_id}-{task_detail}"
            HttpApi.task_complete(task_id)
        else:
            send_content += f">任务失败(启用异常): {task_id}-{task_detail}"
    elif task_id == 34:
        # print("本日分享资讯到社交网络")
        if HttpApi.share("shareInfo", "1") is not None:
            send_content += f">任务成功: {task_id}-{task_detail}"
            HttpApi.task_complete(task_id)
        else:
            send_content += f">任务失败(分享异常): {task_id}-{task_detail}"
    elif task_id == 35:
        # print("本周分享战绩周报到社交网络")
        if HttpApi.share("shareH5", "https://c.gp.qq.com/camp/weekly/index") is not None:
            send_content += f">任务成功: {task_id}-{task_detail}"
            HttpApi.task_complete(task_id)
        else:
            send_content += f">任务失败(分享异常): {task_id}-{task_detail}"
    elif task_id == 36:
        # print("观看PEL赛事直播5分钟")
        ext_data = [{
            "reportInterval": 5,
            "eventId": 400016,
            "subModuleId": 26,
            "page": 102004,
            "moduleId": 9
        }] * 12
        module_report(ext_data, task_id, task_detail)
    else:
        send_content += f">未知任务(无法完成): {task_id}-{task_detail}"


def module_report(ext_data, task_id, task_detail):
    global send_content
    report_count = 0
    for _ in range(5):
        if HttpApi.module_report(ext_data) is not None:
            report_count += 1
    if report_count == 5:
        send_content += f">任务成功: {task_id}-{task_detail}"
        HttpApi.task_complete(task_id)
    else:
        send_content += f">任务失败(观看异常): {task_id}-{task_detail}"


def do_gift_list():
    global send_content
    resp_json = HttpApi.task_list()
    if resp_json is not None:
        send_content += ">获取礼包列表成功"
        gift_list = resp_json["data"]["liveness"]["livenessGiftList"]
        for gift in gift_list:
            gift_id = gift["giftId"]
            gift_title = gift["giftTitle"]
            gift_status = gift["status"]
            if gift_status == 1:
                gift_receive(gift_id, gift_title)
    else:
        send_content += ">获取礼包列表失败"


def gift_receive(gift_id, gift_title):
    global send_content
    if gift_id == 1:
        # print("福利币*100")
        if HttpApi.gift_receive(gift_id) is not None:
            send_content += f">已领取礼包: {gift_id}-{gift_title}"
    elif gift_id == 2:
        # print("营地装饰碎片*50")
        if HttpApi.gift_receive(gift_id) is not None:
            send_content += f">已领取礼包: {gift_id}-{gift_title}"
    elif gift_id == 3:
        # print("福利币*200")
        if HttpApi.gift_receive(gift_id) is not None:
            send_content += f">已领取礼包: {gift_id}-{gift_title}"
    else:
        send_content += f">未知礼包(无法领取): {gift_id}-{gift_title}"


def do_like_records():
    resp_json = HttpApi.like_records()
    if resp_json is not None:
        for info in resp_json["data"]["infoList"]:
            info_id = info["iInfoId"]
            HttpApi.like_info(info_id, "0")
        for moment in resp_json["data"]["momentList"]:
            moment_id = moment["momentId"]
            HttpApi.like_moment(moment_id, "0")


def entry():
    if os.environ.get("pg_enable") == "true":
        global send_content
        send_content += "#########################################################"
        send_content += f"# 和平营地 # {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        if Util.check_repo_secrets(
                [
                    "pg_appid",
                    "pg_msdkEncodeParam",
                    "pg_openid",
                    "pg_sig",
                    "pg_timestamp",
                    "pg_roleId",
                    "pg_userId",
                    "pg_token"
                ]
        ):
            send_content += ">环境变量已配置"
            signin()
            do_task_list()
            do_gift_list()
            do_like_records()
        else:
            send_content += ">环境变量未配置"
        send_content += "#########################################################"
        print(send_content)
        PushPlus.send("和平营地", send_content)

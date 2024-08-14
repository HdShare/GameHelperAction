import os
from datetime import datetime

from src.smoba.http import HttpApi
from src.util import Util, ServerChan

send_content = ""


def do_task_list():
    resp_json = HttpApi.task_list()
    if resp_json is not None:
        task_list = resp_json["data"]["taskList"]
        for task in task_list:
            task_id = task["taskId"]
            task_desc = task["desc"]
            task_finish_status = task["finishStatus"]
            if task_finish_status == 0:
                task_complete(task_id, task_desc)


def task_complete(task_id, task_desc):
    global send_content
    if task_id == "2023091500002":
        # print("每天任意点赞营地1条内容")
        list_info_moment = HttpApi.list_info_moment()
        if list_info_moment is not None:
            is_success = False
            for item in reversed(list_info_moment["data"]["list"]):
                if item["type"] == 14:
                    if HttpApi.like_info(item["infoContent"]["infoId"], "1") is not None:
                        is_success = True
                        break
                elif item["type"] == 2:
                    if HttpApi.like_moment(item["momentId"], True) is not None:
                        is_success = True
                        break
            if is_success:
                send_content += ">任务成功: 点赞内容完成\n"
            else:
                send_content += ">任务失败: 点赞内容出错\n"
        else:
            send_content += ">任务失败: 获取列表出错\n"
    elif task_id == "2024010800001":
        # print("当日浏览营地1篇资讯")
        list_info_moment = HttpApi.list_info_moment()
        if list_info_moment is not None:
            is_success = False
            for item in reversed(list_info_moment["data"]["list"]):
                if item["type"] == 14:
                    if HttpApi.detail_info(item["infoContent"]["infoId"]) is not None:
                        is_success = True
                        break
                elif item["type"] == 15:
                    if HttpApi.detail_post(item["postContent"]["postId"]) is not None:
                        is_success = True
                        break
            if is_success:
                send_content += ">任务成功: 浏览资讯完成\n"
            else:
                send_content += ">任务失败: 浏览资讯出错\n"
        else:
            send_content += ">任务失败: 获取列表出错\n"
    elif task_id == "2024010800002":
        # print("限时任务：前往任意游戏专区签到1次")
        if HttpApi.signin() is not None:
            send_content += ">任务成功: 专区签到完成\n"
        else:
            send_content += ">任务失败: 专区签到出错\n"
    elif task_id == "2024010800004":
        # print("分享王者营地任一内容到社交网络")
        if HttpApi.play_task_data("1") is not None:
            send_content += ">任务成功: 分享内容完成\n"
        else:
            send_content += ">任务失败: 分享内容出错\n"
    else:
        send_content += f">未知任务: {task_id}-{task_desc}\n"


def do_task_reward():
    global send_content
    resp_json = HttpApi.task_list()
    if resp_json is not None:
        task_ids = []
        task_list = resp_json["data"]["taskList"]
        for task in task_list:
            task_id = task["taskId"]
            task_finish_status = task["finishStatus"]
            task_package_status = task["packageStatus"]
            if task_finish_status == 1 and task_package_status == 0:
                task_ids.append(task_id)
        if len(task_ids) > 0:
            if HttpApi.task_reward(task_ids) is not None:
                send_content += f">领取成功: {len(task_ids)} / {len(task_list)}\n"
            else:
                send_content += f">领取失败: {len(task_ids)} / {len(task_list)}\n"


def do_clear_like():
    resp_json = HttpApi.records_list(10, "LIKE")
    if resp_json is not None:
        for info in resp_json["data"]["list"]:
            item_id = info["itemId"]
            if item_id.startswith("1_"):
                info_id = item_id.split("_")[1]
                HttpApi.like_info(info_id, "0")
            if item_id.startswith("4_"):
                moment_id = item_id.split("_")[1]
                HttpApi.like_moment(moment_id, False)


def do_camp_list():
    resp_json = HttpApi.camp_get_task_list()
    if resp_json is not None:
        group_tasks = resp_json["data"]["data"]["taskgroup"]["grouptasks"]
        for group_task in group_tasks:
            task_id = group_task["taskid"]
            task_desc = group_task["taskinfo"]["desc"]
            task_is_finished = group_task["taskdata"]["isfinished"]
            if not task_is_finished:
                camp_complete(task_id, task_desc)


def camp_complete(task_id, task_desc):
    global send_content
    if task_id == 1001145:
        # print("今日前往每日福利签到")
        send_content += ">任务失败: 福利签到异常\n"
    elif task_id == 1001159:
        # print("每日在任意圈子签到")
        if HttpApi.bbs_sign(25) is not None:
            send_content += ">任务成功: 圈子签到完成\n"
        else:
            send_content += ">任务失败: 圈子签到出错\n"
    elif task_id == 1001295:
        # print("玩家每日观赛30s")
        send_content += ">任务失败: 每日观赛出错\n"
    else:
        send_content += f">未知任务: {task_id}-{task_desc}\n"


def do_camp_reward():
    global send_content
    resp_json = HttpApi.camp_get_task_reward()
    if resp_json is not None:
        send_content += f">领取成功: 领取奖励完成\n"
    resp_json = HttpApi.camp_set_task_finish_count()
    if resp_json is not None:
        send_content += f">刷新成功: 刷新数量完成\n"


def entry():
    if os.environ.get("smoba_enable") == "true":
        global send_content
        send_content += "#####################################\n"
        send_content += f"# 王者营地 # {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        if Util.check_repo_secrets(
                [
                    "smoba_roleId",
                    "smoba_userId",
                    "smoba_token"
                ]
        ):
            do_task_list()
            do_task_reward()
            do_clear_like()
        else:
            send_content += ">环境变量未配置\n"
        if Util.check_repo_secrets(
                [
                    "smoba_sMSDKUrlParam",
                    "smoba_sOpenId",
                    "smoba_sCampUserId"
                ]
        ):
            do_camp_list()
            do_camp_reward()
        else:
            send_content += ">环境变量未配置\n"
        send_content += "#####################################\n"
        print(send_content)
        ServerChan.send("Action-王者营地", send_content)

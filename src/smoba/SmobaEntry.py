from datetime import datetime

from src.smoba.http import HttpApi


def do_task_list():
    resp_json = HttpApi.task_list()
    if resp_json is not None:
        # print("任务列表获取成功")
        task_list = resp_json["data"]["taskList"]
        for task in task_list:
            task_id = task["taskId"]
            task_desc = task["desc"]
            task_finish_status = task["finishStatus"]
            if task_finish_status == 0:
                print(f"正在完成任务: {task_id}-{task_desc}")
                task_complete(task_id, task_desc)


def task_complete(task_id, task_desc):
    if task_id == "2023091500002":
        # print("每天任意点赞营地1条内容")
        info_list = HttpApi.info_list()
        if info_list is not None:
            count = 0
            for i in range(1):
                if HttpApi.info_like(info_list["data"]["list"][i]["infoContent"]["infoId"], "1") is not None:
                    count += 1
            if count == 1:
                print(f">任务成功: {task_id}-{task_desc}")
            else:
                print(f">任务失败: {task_id}-{task_desc}")
        else:
            print(f">任务失败: {task_id}-{task_desc}")
    elif task_id == "2024010800001":
        # print("当日浏览营地1篇资讯")
        info_list = HttpApi.info_list()
        if info_list is not None:
            count = 0
            for i in range(1):
                if HttpApi.info_detail(info_list["data"]["list"][i]["infoContent"]["infoId"]) is not None:
                    count += 1
            if count == 1:
                print(f">任务成功: {task_id}-{task_desc}")
            else:
                print(f">任务失败: {task_id}-{task_desc}")
        else:
            print(f">任务失败: {task_id}-{task_desc}")
    elif task_id == "2024010800002":
        # print("限时任务：前往任意游戏专区签到1次")
        if HttpApi.signin() is not None:
            print(f">任务成功: {task_id}-{task_desc}")
        else:
            print(f">任务失败: {task_id}-{task_desc}")
    elif task_id == "2024010800004":
        # print("分享王者营地任一内容到社交网络")
        if HttpApi.play_task_data("1") is not None:
            print(f">任务成功: {task_id}-{task_desc}")
        else:
            print(f">任务失败: {task_id}-{task_desc}")
    else:
        print(f">未知任务: {task_id}-{task_desc}")


def do_task_reward():
    resp_json = HttpApi.task_list()
    if resp_json is not None:
        # print("任务列表获取成功")
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
                print(f">领取成功: {len(task_ids)}")
            else:
                print(f">领取失败: {len(task_ids)}")


def entry():
    print("#########################################################")
    print(f"# 王者营地 # {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    do_task_list()
    do_task_reward()
    print("#########################################################")

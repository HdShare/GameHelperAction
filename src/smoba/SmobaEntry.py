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
        list_info_moment = HttpApi.list_info_moment()
        if list_info_moment is not None:
            i = -1
            if list_info_moment["data"]["list"][i]["showType"] == 0:
                if HttpApi.like_info(list_info_moment["data"]["list"][i]["infoContent"]["infoId"], "1") is not None:
                    print(f">任务成功: 点赞资讯完成")
                else:
                    print(f">任务失败: 点赞资讯出错")
            elif list_info_moment["data"]["list"][i]["showType"] == 1:
                if HttpApi.like_moment(list_info_moment["data"]["list"][i]["momentId"], True) is not None:
                    print(f">任务成功: 点赞动态完成")
                else:
                    print(f">任务失败: 点赞动态出错")
            else:
                print(f">任务失败: 未知列表类型")
        else:
            print(f">任务失败: 获取列表出错")
    elif task_id == "2024010800001":
        # print("当日浏览营地1篇资讯")
        list_info_moment = HttpApi.list_info_moment()
        if list_info_moment is not None:
            i = -1
            if list_info_moment["data"]["list"][i]["showType"] == 0:
                if HttpApi.detail_info(list_info_moment["data"]["list"][i]["infoContent"]["infoId"]) is not None:
                    print(f">任务成功: 浏览资讯完成")
                else:
                    print(f">任务失败: 浏览资讯出错")
            elif list_info_moment["data"]["list"][i]["showType"] == 1:
                if HttpApi.detail_moment(list_info_moment["data"]["list"][i]["momentId"]) is not None:
                    print(f">任务成功: 浏览动态完成")
                else:
                    print(f">任务失败: 浏览动态出错")
            else:
                print(f">任务失败: 未知列表类型")
        else:
            print(f">任务失败: 获取列表出错")
    elif task_id == "2024010800002":
        # print("限时任务：前往任意游戏专区签到1次")
        if HttpApi.signin() is not None:
            print(f">任务成功: 专区签到完成")
        else:
            print(f">任务失败: 专区签到出错")
    elif task_id == "2024010800004":
        # print("分享王者营地任一内容到社交网络")
        if HttpApi.play_task_data("1") is not None:
            print(f">任务成功: 分享内容完成")
        else:
            print(f">任务失败: 分享内容出错")
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
                print(f">领取成功: {len(task_ids)}/{len(task_list)}")
            else:
                print(f">领取失败: {len(task_ids)}/{len(task_list)}")


def entry():
    print("#########################################################")
    print(f"# 王者营地 # {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    do_task_list()
    do_task_reward()
    print("#########################################################")

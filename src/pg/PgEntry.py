from datetime import datetime

from src.pg.http import HttpApi


def signin():
    resp_json = HttpApi.signin()
    if resp_json is not None:
        print("签到成功")


def do_like_records():
    resp_json = HttpApi.like_records()
    if resp_json is not None:
        # print("点赞记录获取成功")
        for info in resp_json["data"]["infoList"]:
            info_id = info["iInfoId"]
            print(f"正在清理点赞: {info_id}")
            if HttpApi.like_info(info_id, "0") is not None:
                print(f">清赞成功")
            else:
                print(f">清赞失败:")
        for moment in resp_json["data"]["momentList"]:
            moment_id = moment["momentId"]
            print(f">正在清理点赞: {moment_id}")
            if HttpApi.like_moment(moment_id, "0") is not None:
                print(f">清赞成功")
            else:
                print(f">清赞失败")


def do_task_list():
    resp_json = HttpApi.task_list()
    if resp_json is not None:
        # print("任务列表获取成功")
        task_list = resp_json["data"]["taskList"]
        for task in task_list:
            task_id = task["taskId"]
            task_detail = task["detailDesc"]
            task_status = task["status"]
            if task_status == 0:
                print(f"正在完成任务: {task_id}-{task_detail}")
                task_complete(task_id, task_detail)
            elif task_status == 2:
                HttpApi.task_complete(task_id)


def task_complete(task_id, task_detail):
    if task_id == 26:
        # print("本日通过和平营地启动1次游戏")
        print(f">任务失败: {task_id}-{task_detail}")
    elif task_id == 27:
        # print("本日取胜1局计分模式（前五）")
        print(f">任务失败: {task_id}-{task_detail}")
    elif task_id == 28:
        # print("本日为资讯点赞3次")
        page_info = HttpApi.page_info()
        if page_info is not None:
            like_count = 0
            for i in range(3):
                if HttpApi.like_info(page_info["data"]["list"][i]["iInfoId"], "1") is not None:
                    like_count += 1
            if like_count == 3:
                print(f">任务成功: {task_id}-{task_detail}")
                HttpApi.task_complete(task_id)
            else:
                print(f">任务失败: {task_id}-{task_detail}")
        else:
            print(f">任务失败: {task_id}-{task_detail}")
    elif task_id == 29:
        # print("本日为动态点赞3次")
        page_moment = HttpApi.page_moment()
        if page_moment is not None:
            like_count = 0
            for i in range(3):
                if HttpApi.like_moment(page_moment["data"]["list"][i]["momentId"], "1") is not None:
                    like_count += 1
            if like_count == 3:
                print(f">任务成功: {task_id}-{task_detail}")
                HttpApi.task_complete(task_id)
            else:
                print(f">任务失败: {task_id}-{task_detail}")
        else:
            print(f">任务失败: {task_id}-{task_detail}")
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
            print(f">任务成功: {task_id}-{task_detail}")
            HttpApi.task_complete(task_id)
        else:
            print(f">任务失败: {task_id}-{task_detail}")
    elif task_id == 34:
        # print("本日分享资讯到社交网络")
        if HttpApi.share("shareInfo", "1") is not None:
            print(f">任务成功: {task_id}-{task_detail}")
            HttpApi.task_complete(task_id)
        else:
            print(f">任务失败: {task_id}-{task_detail}")
    elif task_id == 35:
        # print("本周分享战绩周报到社交网络")
        if HttpApi.share("shareH5", "https://c.gp.qq.com/camp/weekly/index") is not None:
            print(f">任务成功: {task_id}-{task_detail}")
            HttpApi.task_complete(task_id)
        else:
            print(f">任务失败: {task_id}-{task_detail}")
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
        print(f">未知任务: {task_id}-{task_detail}")


def module_report(ext_data, task_id, task_detail):
    report_count = 0
    for _ in range(5):
        if HttpApi.module_report(ext_data) is not None:
            report_count += 1
    if report_count == 5:
        print(f">任务成功: {task_id}-{task_detail}")
        HttpApi.task_complete(task_id)
    else:
        print(f">任务失败: {task_id}-{task_detail}")


def do_gift_list():
    resp_json = HttpApi.task_list()
    if resp_json is not None:
        # print("礼物列表获取成功")
        gift_list = resp_json["data"]["liveness"]["livenessGiftList"]
        for gift in gift_list:
            gift_id = gift["giftId"]
            gift_title = gift["giftTitle"]
            gift_status = gift["status"]
            if gift_status == 1:
                print(f"正在领取礼包: {gift_id}-{gift_title}")
                gift_receive(gift_id, gift_title)


def gift_receive(gift_id, gift_title):
    if gift_id == 1:
        # print("福利币*100")
        if HttpApi.gift_receive(gift_id) is not None:
            print(f">已领取礼包: {gift_id}-{gift_title}")
    elif gift_id == 2:
        # print("营地装饰碎片*50")
        if HttpApi.gift_receive(gift_id) is not None:
            print(f">已领取礼包: {gift_id}-{gift_title}")
    elif gift_id == 3:
        # print("福利币*200")
        if HttpApi.gift_receive(gift_id) is not None:
            print(f">已领取礼包: {gift_id}-{gift_title}")
    else:
        print(f">未知礼包: {gift_id}-{gift_title}")


def entry():
    print("#########################################################")
    print(f"# 和平营地 #{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    signin()
    do_like_records()
    do_task_list()
    do_gift_list()
    print("#########################################################")

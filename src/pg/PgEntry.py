import os
from datetime import datetime

from src.pg.http import HttpApi
from src.util import Util, ServerChan

send_content = ""


def signin():
    global send_content
    resp_json = HttpApi.signin()
    if resp_json is not None:
        send_content += ">签到成功\n"
    else:
        send_content += ">签到失败\n"


def do_task_list():
    resp_json = HttpApi.task_list()
    if resp_json is not None:
        task_list = resp_json["data"]["taskList"]
        for task in task_list:
            task_id = task["taskId"]
            task_detail = task["detailDesc"]
            task_status = task["status"]
            if task_status == 0:
                task_complete(task_id, task_detail)
            elif task_status == 2:
                HttpApi.task_complete(task_id)


def task_complete(task_id, task_detail):
    global send_content
    if task_id == 26:
        # print("本日通过和平营地启动1次游戏")
        send_content += ">任务失败: 无法启动游戏\n"
    elif task_id == 27:
        # print("本日取胜1局计分模式（前五）")
        send_content += ">任务失败: 无法取胜前五\n"
    elif task_id == 28:
        # print("本日为资讯点赞3次")
        page_info = HttpApi.page_info()
        if page_info is not None:
            like_count = 0
            for i in range(3):
                if HttpApi.like_info(page_info["data"]["list"][i]["iInfoId"], "1") is not None:
                    like_count += 1
            if like_count == 3:
                send_content += ">任务成功: 点赞资讯完成\n"
                HttpApi.task_complete(task_id)
            else:
                send_content += ">任务失败: 点赞资讯出错\n"
        else:
            send_content += ">任务失败: 获取资讯出错\n"
    elif task_id == 29:
        # print("本日为动态点赞3次")
        page_moment = HttpApi.page_moment()
        if page_moment is not None:
            like_count = 0
            for i in range(3):
                if HttpApi.like_moment(page_moment["data"]["list"][i]["momentId"], "1") is not None:
                    like_count += 1
            if like_count == 3:
                send_content += ">任务成功: 点赞动态完成\n"
                HttpApi.task_complete(task_id)
            else:
                send_content += ">任务失败: 点赞动态出错\n"
        else:
            send_content += ">任务失败: 获取动态出错\n"
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
            send_content += ">任务成功: 启用工具完成\n"
            HttpApi.task_complete(task_id)
        else:
            send_content += ">任务失败: 启用工具出错\n"
    elif task_id == 34:
        # print("本日分享资讯到社交网络")
        if HttpApi.share("shareInfo", "1") is not None:
            send_content += ">任务成功: 分享资讯完成\n"
            HttpApi.task_complete(task_id)
        else:
            send_content += ">任务失败: 分享资讯出错\n"
    elif task_id == 35:
        # print("本周分享战绩周报到社交网络")
        if HttpApi.share("shareH5", "https://c.gp.qq.com/camp/weekly/index") is not None:
            send_content += ">任务成功: 分享周报完成\n"
            HttpApi.task_complete(task_id)
        else:
            send_content += ">任务失败: 分享周报出错\n"
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
        send_content += f">未知任务: {task_id}-{task_detail}\n"


def module_report(ext_data, task_id, task_detail):
    global send_content
    report_count = 0
    for _ in range(5):
        if HttpApi.module_report(ext_data) is not None:
            report_count += 1
    if report_count == 5:
        send_content += f">任务成功: {task_detail}\n"
        HttpApi.task_complete(task_id)
    else:
        send_content += f">任务失败: {task_detail}出错\n"


def do_gift_list():
    resp_json = HttpApi.task_list()
    if resp_json is not None:
        gift_list = resp_json["data"]["liveness"]["livenessGiftList"]
        for gift in gift_list:
            gift_id = gift["giftId"]
            gift_title = gift["giftTitle"]
            gift_status = gift["status"]
            if gift_status == 1:
                gift_receive(gift_id, gift_title)


def gift_receive(gift_id, gift_title):
    global send_content
    if gift_id == 1:
        # print("福利币*100")
        if HttpApi.gift_receive(gift_id) is not None:
            send_content += f">领取成功: {gift_title}\n"
    elif gift_id == 2:
        # print("营地装饰碎片*50")
        if HttpApi.gift_receive(gift_id) is not None:
            send_content += f">领取成功: {gift_title}\n"
    elif gift_id == 3:
        # print("福利币*200")
        if HttpApi.gift_receive(gift_id) is not None:
            send_content += f">领取成功: {gift_title}\n"
    else:
        send_content += f">未知礼包: {gift_id}-{gift_title}\n"


def do_welfare_list():
    resp_json = HttpApi.welfare_list()
    if resp_json is not None:
        tasks = resp_json["data"]["tasks"]
        for task in tasks:
            task_id = task["taskId"]
            task_title = task["title"]
            task_status = task["status"]
            if task_status == 0:
                welfare_complete(task_id, task_title)


def refresh_welfare_list():
    global send_content
    if HttpApi.welfare_refresh_list() is not None:
        send_content += ">任务成功: 刷新任务完成\n"
    else:
        send_content += ">任务失败: 刷新任务出错\n"


def welfare_complete(task_id, task_title):
    global send_content
    if task_id == 1001:
        # print("本日启动1次和平精英")
        send_content += ">任务失败: 无法启动和平\n"
    elif task_id == 1002:
        # print("本日获得一场经典模式比赛胜利")
        send_content += ">任务失败: 无法获得胜利\n"
    elif task_id == 1003:
        # print("本日在营地分享“我的资产”到社交网络")
        if HttpApi.share("shareAssets", "") is not None:
            send_content += ">任务成功: 分享资产完成\n"
        else:
            send_content += ">任务失败: 分享资产出错\n"
    elif task_id == 1004:
        # print("本日分享自己的战绩复盘到社交网络")
        if HttpApi.share("shareH5", "https://c.gp.qq.com/reviewV4/") is not None:
            send_content += ">任务成功: 分享复盘完成\n"
        else:
            send_content += ">任务失败: 分享复盘出错\n"
    elif task_id == 1005:
        # print("本日分享自己的战绩到社交网络")
        if HttpApi.share("shareMatch", "") is not None:
            send_content += ">任务成功: 分享战绩完成\n"
        else:
            send_content += ">任务失败: 分享战绩出错\n"
    elif task_id == 1006:
        # print("本日分享一篇资讯到社交网络")
        if HttpApi.share("shareInfo", "1") is not None:
            send_content += ">任务成功: 分享资讯完成\n"
        else:
            send_content += ">任务失败: 分享资讯出错\n"
    elif task_id == 1007:
        # print("本日在“和平营地”对资讯进行一次充能")
        resp_json = HttpApi.recharge_rank()
        if resp_json is not None:
            recharge_count = 0
            for i in range(3):
                if HttpApi.recharge(resp_json["data"]["list"][i]["iInfoId"], "1") is not None:
                    recharge_count += 1
                    break
            if recharge_count == 1:
                send_content += ">任务成功: 充能资讯完成\n"
            else:
                send_content += ">任务失败: 充能资讯出错\n"
    elif task_id == 1008:
        # print("本日浏览1次攻略专区")
        if HttpApi.station() is not None:
            send_content += ">任务成功: 浏览攻略完成\n"
        else:
            send_content += ">任务失败: 浏览攻略出错\n"
    elif task_id == 1009:
        # print("本日在营地观看1次战绩复盘")
        if HttpApi.replay_data() is not None:
            send_content += ">任务成功: 观看复盘完成\n"
        else:
            send_content += ">任务失败: 观看复盘出错\n"
    elif task_id == 1010:
        # print("本日浏览3分钟资讯")
        ext_data = [{
            "reportInterval": 5,
            "eventId": 100004,
            "subModuleId": 27,
            "page": 101004,
            "moduleId": 1
        }] * 12
        module_report(ext_data, task_id, task_title)
    elif task_id == 1011:
        # print("开启4个营地对局工具（不含游戏加速器）")
        open_count = 0
        for i in range(4):
            if HttpApi.game_tool(i, "1") is not None:
                open_count += 1
        if open_count == 4:
            send_content += ">任务成功: 启用工具完成\n"
        else:
            send_content += ">任务失败: 启用工具出错\n"
    elif task_id == 1012:
        # print("本日为资讯点赞3次")
        page_info = HttpApi.page_info()
        if page_info is not None:
            like_count = 0
            for i in range(3):
                if HttpApi.like_info(page_info["data"]["list"][i]["iInfoId"], "1") is not None:
                    like_count += 1
            if like_count == 3:
                send_content += ">任务成功: 点赞资讯完成\n"
            else:
                send_content += ">任务失败: 点赞资讯出错\n"
        else:
            send_content += ">任务失败: 获取资讯出错\n"
    elif task_id == 1013:
        # print("本日为动态点赞3次")
        page_moment = HttpApi.page_moment()
        if page_moment is not None:
            like_count = 0
            for i in range(3):
                if HttpApi.like_moment(page_moment["data"]["list"][i]["momentId"], "1") is not None:
                    like_count += 1
            if like_count == 3:
                send_content += ">任务成功: 点赞动态完成\n"
            else:
                send_content += ">任务失败: 点赞动态出错\n"
        else:
            send_content += ">任务失败: 获取动态出错\n"
    elif task_id == 1014:
        # print("本日在营地进行一次好友观战")
        send_content += ">任务失败: 无法观战好友\n"
    else:
        send_content += f">未知任务: {task_id}-{task_title}\n"


def do_welfare_reward():
    resp_json = HttpApi.welfare_list()
    if resp_json is not None:
        tasks = resp_json["data"]["tasks"]
        for task in tasks:
            task_index = task["index"]
            task_status = task["status"]
            if task_status == 1:
                # TODO: 领取任务奖励失败，请重试
                HttpApi.welfare_complete(task_index)


def do_clear_like():
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
        send_content += "#####################################\n"
        send_content += f"# 和平营地 # {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
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
            signin()
            do_welfare_list()
            do_welfare_reward()
            refresh_welfare_list()
            do_welfare_list()
            do_welfare_reward()
            do_clear_like()
        else:
            send_content += ">环境变量未配置\n"
        send_content += "#####################################\n"
        print(send_content)
        ServerChan.send("Action-和平营地", send_content)

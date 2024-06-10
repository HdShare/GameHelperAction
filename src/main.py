import os
import sys

if __name__ == '__main__':
    sys.path.append(os.getcwd())

    # # 本地配置
    # from src.env import EnvUtil
    # EnvUtil.init()

    # 和平营地
    from src.pg import PgEntry
    PgEntry.entry()

    # 王者营地
    from src.smoba import SmobaEntry
    SmobaEntry.entry()

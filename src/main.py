import os
import sys

if __name__ == '__main__':
    sys.path.append(os.getcwd())
    # from src.env import EnvUtil
    from src.pg import PgEntry
    from src.smoba import SmobaEntry

    # 本地配置
    # EnvUtil.init()

    # 和平营地
    PgEntry.entry()

    # 王者营地
    SmobaEntry.entry()

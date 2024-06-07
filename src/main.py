import os
import sys

if __name__ == '__main__':
    sys.path.append(os.getcwd())
    from src.env import EnvUtil
    # 本地配置
    # EnvUtil.init()

    from src.pg import PgEntry
    # 和平营地
    PgEntry.entry()

    from src.smoba import SmobaEntry
    # 王者营地
    SmobaEntry.entry()

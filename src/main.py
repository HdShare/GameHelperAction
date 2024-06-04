import os
import sys

if __name__ == '__main__':
    sys.path.append(os.getcwd())
    # from src.env import EnvUtil
    # EnvUtil.init()
    from src.pg import PgEntry
    from src.smoba import SmobaEntry
    PgEntry.entry()
    SmobaEntry.entry()

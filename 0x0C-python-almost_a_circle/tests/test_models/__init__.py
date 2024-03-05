import sys
import os


filedir_path = os.path.dirname(__file__)
join_target_path = os.path.join(filedir_path, '../..')
target_path = os.path.abspath(join_target_path)

sys.path.insert(0, target_path)

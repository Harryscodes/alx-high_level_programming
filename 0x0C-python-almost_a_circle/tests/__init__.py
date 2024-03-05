import os
import sys

# Add the parent directory to the sys.path
absolute_path = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(absolute_path, '../..'))
sys.path.insert(0, parent_dir)

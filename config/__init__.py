import os

import environ

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
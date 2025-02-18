import os

# 修复了环境变量读取方式
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')

if DEEPSEEK_API_KEY is None:
    raise ValueError("DEEPSEEK_API_KEY is not set")

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if GITHUB_TOKEN is None:
    raise ValueError("GITHUB_TOKEN is not set")

# 这里写你的业务逻辑代码

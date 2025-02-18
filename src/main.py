# 设置GitHub Secrets
DEEPSEEK_API_KEY=sk-a6eba5aac549471babca28ae98a95f25

import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if GITHUB_TOKEN is None:
    raise ValueError("GITHUB_TOKEN is not set")

# Your code that uses GITHUB_TOKEN

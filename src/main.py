import os

DEEPSEEK_API_KEY = os.getenv('sk-a6eba5aac549471babca28ae98a95f25')

if DEEPSEEK_API_KEY is None:
    raise ValueError("DEEPSEEK_API_KEY is not set")

# Your code that uses DEEPSEEK_API_KEY

import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if GITHUB_TOKEN is None:
    raise ValueError("GITHUB_TOKEN is not set")

# Your code that uses GITHUB_TOKEN

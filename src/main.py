# src/main.py
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--event', required=True)
    args = parser.parse_args()
    
    # 使用更安全的get方式获取环境变量
    github_token = os.environ.get('GITHUB_TOKEN')
    deepseek_key = os.environ.get('DEEPSEEK_API_KEY')
    
    if not github_token:
        raise ValueError("GITHUB_TOKEN must be set in environment variables")
    
    if not deepseek_key:
        raise ValueError("DEEPSEEK_API_KEY must be set in environment variables")
    
    print(f"Processing {args.event} event...")
    # 后续业务逻辑

if __name__ == "__main__":
    main()

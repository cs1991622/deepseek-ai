# src/handlers/pr_handler.py
from github import Github

def process_pull_request(event):
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(event.repository.full_name)
    pr = repo.get_pull(event.number)
    
    # 获取代码差异
    diffs = [f.file.filename for f in pr.get_files()]
    
    # 生成评审建议
    client = DeepSeekClient()
    prompt = f"请评审以下Python代码的改进建议：\n{diffs}"
    feedback = client.generate_code(prompt)
    
    # 创建评审评论
    pr.create_issue_comment(f"## DeepSeek 代码建议\n{feedback}")

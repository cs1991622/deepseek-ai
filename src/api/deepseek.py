# src/api/deepseek.py
import os
import requests

class DeepSeekClient:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.base_url = "https://api.deepseek.com/v1"
        
    def generate_code(self, prompt, context=None, max_tokens=500):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "prompt": f"[代码上下文]\n{context}\n\n[需求]\n{prompt}",
            "temperature": 0.7,
            "max_tokens": max_tokens,
            "stream": False
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/completions",
                headers=headers,
                json=payload
            )
            return response.json()['choices'][0]['text']
        except Exception as e:
            return f"API调用失败: {str(e)}"

# 示例用法
if __name__ == "__main__":
    client = DeepSeekClient()
    print(client.generate_code("实现快速排序", "def sort(arr):"))

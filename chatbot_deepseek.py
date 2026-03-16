# -*- coding: utf-8 -*-
import requests
import json
import os

# 从环境变量读取敏感信息（避免硬编码）
ACCESS_KEY = os.getenv("VOLC_ACCESSKEY")
SECRET_KEY = os.getenv("VOLC_SECRETKEY")
BOT_ID = os.getenv("VOLC_BOT_ID")  # 火山方舟创建的 Bot ID

# 火山引擎 API 地址（以 DeepSeek R1 为例）
API_URL = "https://ark.cn-beijing.volces.com/api/v3/bots/chat/completions"

def chat_with_deepseek(user_input: str) -> str:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_KEY}:{SECRET_KEY}"
    }
    payload = {
        "bot_id": BOT_ID,
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"调用失败：{str(e)}"

if __name__ == "__main__":
    print("💬 DeepSeek Chatbot（火山引擎版）已启动（输入 'quit' 退出）")
    while True:
        user_input = input("你：")
        if user_input.lower() == "quit":
            print("👋 再见！")
            break
        reply = chat_with_deepseek(user_input)
        print(f"🤖 AI：{reply}")
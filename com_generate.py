import requests
import json
import time
import os
os.environ['DASHSCOPE_API_KEY'] = "sk-1d15858ebcea4802a5a0ebb0b4ed976e"
import dashscope
from http import HTTPStatus
## API_KEY = """eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiLmvZjml63kuJwiLCJVc2VyTmFtZSI6Iua9mOaXreS4nCIsIkFjY291bnQiOiIiLCJTdWJqZWN0SUQiOiIxNzY0Nzg5NTgzMTcxNTU5NDQwIiwiUGhvbmUiOiIxMzc3NjExODI4MSIsIkdyb3VwSUQiOiIxNzY0Nzg5NTgzMTMzODE0ODAwIiwiUGFnZU5hbWUiOiIiLCJNYWlsIjoieGRwYW5AZnVkYW4uZWR1LmNuIiwiQ3JlYXRlVGltZSI6IjIwMjQtMDQtMTggMjE6MTc6MjkiLCJpc3MiOiJtaW5pbWF4In0.N54g6T-NZ_MYPDNzJncBvhswIupWwO7TbLIuOjc0zEJNJ6iB0ZJVg0qOvDTbGeqvWS9OBi-5uKMohHq1TgLl1NJ7pkzfNqd5kufM0SgLdW8ffKAP2Thj1GVXvYJQKPEv_01vMzzwTbIF13XBVv2CAWFrjU6yXXWIUvvJcB9962rndjKpHpbh6FC05Y0yc2szrT0E31CFKqstFRbt2eWyJRdGl1wXiEQrt0k63n1YP1Wh1TrLftd6ZH26inIQfMFvyPXiucK94AUr27c3ngdeHlwjbiLhMcp8KyvzlbotvjeuHhXtYT3vkx3p-GhpbrtyeWRH7Qp3b46_5lbDsgfUow"""
API_KEY = """eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiLmvZjml63kuJwiLCJVc2VyTmFtZSI6IndoaXR6YXJkLUxMTS1zdHVkZW50IiwiQWNjb3VudCI6IndoaXR6YXJkLUxMTS1zdHVkZW50QDE3NjQ3ODk1ODMxMzM4MTQ4MDAiLCJTdWJqZWN0SUQiOiIxNzY2MDI3MTc5OTMxNDc2MDExIiwiUGhvbmUiOiIiLCJHcm91cElEIjoiMTc2NDc4OTU4MzEzMzgxNDgwMCIsIlBhZ2VOYW1lIjoiIiwiTWFpbCI6IiIsIkNyZWF0ZVRpbWUiOiIyMDI0LTA1LTE3IDE0OjM4OjExIiwiaXNzIjoibWluaW1heCJ9.T2cKos7YEk4_IWdkhg6e504LM2H4ftY9zxBJfCn_OutumFfaHU0DS8V1IDpddbQbGG_W3ujhLRcUnhUGLFA5WybBtTRj5Ns9XVpkjWWM020fbrXfEE-zrRZ0w8hjbvzjzZJnPUJlOE2jH4EszIl3aoZe-wGyfbxw3Lh0ZzDunuQ7VfAo-6oJ_c3SAC_dLNnw9aZTmItzAb4h54cv4LJ7wEZu93uAr5CTFHKbaO_KcvqwEIaikb4-3PTo6eXjCXeBJ3ZPQw2jpyppAIA-Bo6G9O7WOUN3AFWNqNKIG1mVt527DM3D3R2K8Vwxxwot063vpmGKSkeMZB-4O4DNXslUWw"""
url = "https://api.minimax.chat/v1/text/chatcompletion_v2"
DEFAULT_PROMPT = "You are a helpful assistant."





def chat_with_history(messages):
    return _qwen15_32b_chat(messages)


def _qwen15_32b_chat(messages):    
    response = dashscope.Generation.call(
        model='qwen1.5-32b-chat',
        messages=messages,
        result_format='message',  # set the result to be "message" format.
    )
    try:
        if response.status_code == HTTPStatus.OK:
            out = response['output']['choices'][0]['message']['content']
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))
            out = '[error]'
    except:
        out = '[error]'
    time.sleep(1)
    messages.append({'role':'assistant', 'content': out})
    return messages



def _minimax(messages):
    payload = json.dumps({
        "model": "abab5.5-chat",
        "messages": messages,
        "stream": False,
        "max_tokens": 6000,
        "temperature": 0.7,
        "top_p": 0.9
    })

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        messages.append(json.loads(response.text)['choices'][0]['message'])
        return messages
    except:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        messages.append({'role':'assistant', 'content':'[error]'})
        return messages

def chat(prompt, sys_prompt=DEFAULT_PROMPT):
    messages = [
        {'role':'system', 'content':sys_prompt},
        {'role':'user', 'content':prompt}
    ]
    return chat_with_history(messages)[-1]['content']


if __name__ == "__main__":
    ans = _minimax([{'role':'user', 'content':"你是谁。"}])
    print(ans)
    pass
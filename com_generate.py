import requests
import json
import time
import os
# your DASHSCOPE_API_KEY
os.environ['DASHSCOPE_API_KEY'] = ""
import dashscope
from http import HTTPStatus

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

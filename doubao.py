

from volcenginesdkarkruntime import Ark
import os

class Doubao(object):
    def __init__(self, mode='doubao-lite', secret='2dc5d6ce-0708-4253-a4d2-43e087160c59', debug=False):
        self.secret = secret
        self.mode = mode
        modes_dict = {
            'doubao-lite': 'ep-20240615110951-8l47t',
            'doubao-pro': 'ep-20240615111019-tl2cz' 
        }
        self.model_key = modes_dict[mode]
        print(self.model_key)
        # exit()
    def info(self):
        return {
            "company": "豆包大模型",
            "version": self.mode
        }
    
    def chat(self, messages)->str:
        client = Ark(base_url="https://ark.cn-beijing.volces.com/api/v3",
                     api_key=self.secret)
        completion = client.chat.completions.create(
            model=self.model_key,
            messages = messages
        )
        if(completion.choices[0].finish_reason == 'content_filter'):
            # return (completion)
            return '[error] 风控拦截'
        else:
            # print(completion)
            return (completion.choices[0].message.content)
        

    
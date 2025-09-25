from openai import OpenAI


"""OpenAi-like API for LM-studio"""
class LLM:
    def __init__(self,
                 url: str = 'http://localhost:1234/v1',
                 api_key: str = 'lm-studio',
                 ):
        self.client = OpenAI(base_url=url, api_key=api_key)
        
    def forward_text(self, 
                     user_msg: str = 'Hello',
                     system_msg: str = '',
                     model_name: str = 'lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF',
                     temperature: float = 0.7,
                     ):
        completion = self.client.chat.completions.create(
			model=model_name,
			messages=[
				{'role': 'system', 'content': system_msg},
				{'role': 'user', 'content': user_msg},
			],
			temperature=temperature,
		)
        
        return dict(completion.choices[0].message)['content']
    
    def forward_image(self,
                      ):
        raise NotImplementedError()


lm = LLM()

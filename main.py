import uvicorn
from fastapi import FastAPI

from utils import gpt3, save_qa
from utils import APIConfig


class FastAPIRunner:
    def __init__(self):        
        pass

    def run(self):
        # API config data type 체크 
        api_info_data = APIConfig().dict()
        uvicorn.run(f"{api_info_data['api_name']}", 
                    host=api_info_data['api_info']['host']
                    ,port=api_info_data['api_info']['port']
                    ,reload=True
                    )

app = FastAPI()
app.include_router(gpt3)
app.include_router(save_qa)

@app.get('/')
def read_results():
    return {'msg' : 'Main'}
    
if __name__ == "__main__":
    # python main.py
    api = FastAPIRunner()
    api.run()
    
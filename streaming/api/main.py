from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/')
async def welcome():
    return 'Hello World'

if __name__ == "__main__":
    uvicorn.run('main:app', port = 8000, host ='0.0.0.0')
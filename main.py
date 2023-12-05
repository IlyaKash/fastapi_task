from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def f_index():
    return 'Кашкаров Илья Игоревич'


@app.get('/tools')
async def f_indexT():
    return '+79836083013'


@app.get('/users')
async def f_indexT():
    return 'Нету'


#if __name__ == '__main__':
#    uvicorn.run(app='main:app', host='127.0.0.1', port=3000)

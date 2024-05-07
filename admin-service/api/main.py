import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import database as sess


from api.routes.svc import svc_router
from api.routes.intro import intro_router
from api.routes.admin import admin_router  # 라우터 모듈 임포트

app = FastAPI()

# CORS 설정
origins = [
    "http://localhost:3000",  # 허용할 프론트엔드 도메인
    "http://3.34.47.148:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# admin_router 라우터 추가
app.include_router(admin_router, prefix='/admin')
app.include_router(svc_router, prefix='/svc')
app.include_router(intro_router, prefix='/intro')

if __name__ == '__main__':
    sess.create_tables()
    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=True)

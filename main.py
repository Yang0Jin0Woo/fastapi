from fastapi import  FastAPI, status
from pydantic import BaseModel
app = FastAPI()

# 서버 실행
@app.get("/")
def root_handler():
    return {"message": "Hello World"}

# 경로 사용
@app.get("/login")
def login_handler():
    return {"message": "로그인 페이지에 오신 것을 환영합니다."}

# 경로 변수 사용
@app.get("/users/{user_id}")
def read_user_handler(user_id: int):
    return {"user_id": user_id, "message": f"사용자 {user_id}"}

# 쿼리 파라미터 사용(None은 선택적 사용할 때)
@app.get("/items")
def read_items_handler(max_price: int | None = None):
    return {"max_price": max_price}


## Pydantic 라이브러리 사용: 데이터 검증

# 아이템 모델 정의
class Item(BaseModel):
    name: str
    price: int
    in_stock: bool = True

# # 새 아이템 등록(요청 본문 다루기)
# @app.post("/items")
# def create_item_handler(item: Item):
#     return {"message": f"아이템 '{item.name}'이(가) 추가되었습니다.", "item": item}

# 새 아이템 등록(응답 본문 다루기)
@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item_handler(item: Item):
    return item

# 경로 변수, 쿼리 파라미터, 요청 본문 혼합 사용
@app.put("/items/{item_id}")
def update_item_handler(item_id: int, assignee: str, item: Item):
    return {"item_id": item_id, "assignee": assignee, "item": item}

# 주문 응답 모델
class OrderResponse(BaseModel):
    order_id: int
    pickup: bool | None = None

# 단일 주문 조회
@app.get("/orders/{order_id}", response_model=OrderResponse)
def get_order_handler(order_id: int, pickup: bool | None = None):
    return {
        "order_id": order_id,
        "pickup": pickup,
    }

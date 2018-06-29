from sqlalchemy import Column, Integer, String

from app.models.base import BaseModel
# 分类标签
class Tag(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #编号
    name=Column(String(100),unique=True) #标题
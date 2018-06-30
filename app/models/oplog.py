from sqlalchemy import Column, Integer, ForeignKey, String

from app.models.base import BaseModel


# 管理员操作日志
class Oplog(BaseModel):
    id=Column(Integer,primary_key=True,autoincrement=True) #id
    admin_id=Column(Integer,ForeignKey('admin.id')) #管理员
    ip=Column(String(100)) #登陆ip
    reason=Column(String(600)) #操作原因
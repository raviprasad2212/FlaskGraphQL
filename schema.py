from graphene import ObjectType, String, Schema
from modules.allbikes import GetAllBikes, AllBikes

class Query(GetAllBikes, AllBikes, ObjectType):
    pass


schema = Schema(query=Query)
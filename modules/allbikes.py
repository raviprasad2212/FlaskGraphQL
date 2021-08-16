import json
import psycopg2
from graphene import ObjectType, String, List, Field, Int

import requests
import pandas as pd

class ShowAllBikes(ObjectType):
    name = String()
    price = Int()

class GetAllBikes(ObjectType):
    
    getAllBikes = Field(ShowAllBikes, bikename=String())
    
    def resolve_getAllBikes(self, info, bikename):
        conn = psycopg2.connect(database="allbikes", user="postgres", password="Ravi@143", host="localhost", port="5432")
        cur = conn.cursor()
        query = 'select * from allbikes where name=%s'
        cur.execute(query, (bikename, ))
        
        result = cur.fetchall()
        if (result):
            for index in result:
                name = index[0]
                price = index[1]
                return ShowAllBikes(name=name, price=price)
            

class AllBikes(ObjectType):
    showbikes = String()
    
    def resolve_showbikes(self, info):
        query = """query{
  allbikes{
    name,
    price
  }
}"""
        
        url = 'http://127.0.0.1:8000/graphql'
        r = requests.post(url, json={'query': query})
        j_data = json.loads(r.text)
        df_data = j_data['data']['allbikes']
        df = pd.DataFrame(df_data)
        print(df)
        
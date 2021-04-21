import sys
sys.setrecursionlimit(10000)
import json
import mysql.connector
from math import sin,acos,cos,radians
from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
  return render_template('dist.html')
@app.route('/dist',methods=['GET','POST'])
def dist():
    lat1=float(request.form['lat1'])
    lon1=float(request.form['lon1'])
    ans=distof(lat1,lon1)
    return render_template('dist_res.html',value=ans)
db = mysql.connector.connect(host="localhost",user="root",passwd="admin",database="mysql")
cursor = db.cursor()
sql="Select name,address,city,state,zip,CAST(latitude AS CHAR),CAST(longitude AS CHAR) from pharmacies";
cursor.execute(sql)
res = cursor.fetchall()
for r in res:
    json_str = json.dumps(res)
    resp = json.loads(json_str)
def distof(lat1,lon1):
    Rm=3960
    Rk=6371
    sql="Select p.latitude,p.longitude from pharmacies p"
    cursor.execute(sql)
    results = list(cursor.fetchall())
    d=[]
    d1=[]
    d2=[]
    dlon=[]
    k=0
    for i in range(0,len(results)):
        dlon.append(lon1-float(results[i][1]))
        d.append(acos(sin(radians(lat1))*sin(radians(float(results[i][0])))+cos(radians(lat1))*cos(radians(float(results[i][0])))*cos(radians(dlon[i]))))
        d1.append(d[i]*Rm)
        d2.append(d[i]*Rk)
        k=d1.index(min(d1))
        x=min(d1)
        y=min(d2)
    return lat1,lon1,x,y,k,resp[k]
if __name__=='__main__':
    app.run(debug=True)

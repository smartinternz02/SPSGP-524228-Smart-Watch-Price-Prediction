
from flask import Flask, render_template, request,redirect,url_for
import pickle as pl
import pandas as pd
app=Flask(__name__,template_folder='template')

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/',methods=['POST'])
def getvalue():
    brand=request.form['brand']
    os=request.form['os']
    conn=request.form['conn'] 
    displayType=request.form['dt']
    displaySize=request.form['ds']
    res=request.form['res']
    waRes=request.form['wres']
    bL=request.form['bl']
    rMo=request.form['hr']
    gps=request.form['gps']
    nfc=request.form['nfc']
    df2=pd.DataFrame({"Brand":brand,
                      "Operating System":os,
                      "Connectivity":conn,
                      "Display Type":displayType,
                      "Display Size (inches)":displaySize,
                      "Resolution":res,
                      "Water Resistance (meters)":waRes,
                      "Battery Life (days)":bL,
                      "Heart Rate Monitor":rMo,
                      "GPS":gps,
                      "NFC":nfc},index=[0])
    mod1=pl.load(open("model1.pkl","rb"))
    mod2=pl.load(open("model2.pkl","rb"))
    f=mod1.transform(df2)
    out=mod2.predict(f)
    return render_template('pass.html',
                           bran=brand,
                           o=os,
                           con=conn,
                           displayTyp=displayType,
                           displaySiz=displaySize,
                           re=res,
                           waRe=waRes,
                           bLk=bL,
                           rM=rMo,
                           gp=gps,
                           nf=nfc,
                           b=round(out[0]))

if __name__=="__main__":
    app.run(debug=True)
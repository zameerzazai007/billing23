#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#RESTAURANT BIILING PROJECT


# In[ ]:


#WEB BASED SOFTWARE


# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def billing():
    return render_template("foodd.html")
@app.route("/order",methods=['POST','GET'])
def mobile():
    if(request.method=='POST'):
        NAME=request.form['v1']
        PHONE=request.form['v2']
        od1=request.form['v3']
        od2=request.form['v4']
        od3=request.form['v5']
        od4=request.form['v6']
        STARTERS={'Kookaburrg Wings (RS 29)':29,'Bloomin Onion (RS 18)':18,'Volcano Shrimpo (RS30)':30,'Chicken Tusconi (RS 12)':12,'Chicken Breasts (RS 28)':28}
        SEA={'Grilled Salmon (RS 40)':40,'Shrimp (RS 31)':31,'Beer Battered Coo (RS 32)':32,'Shrimp Santorini (RS 36)':36}
        BBQ={'Baby Back Ribs (RS 120)':120,'BBQ Beef Breast (RS 180)':180,'BBQ Chicken Breast (RS 160)':160,'Combo Plate (360)':360}
        DESSERTS={'Apple Pie (RS 25)':25,'Peach Cobbler (RS 10)':10,'Peach pie (RS 18)':18,'Cheese Cake (RS 15)':15,'Mud Pie (RS 14)':14,'Milk Shake (RS12)':12,'Ice cream (RS 8)':8}
        #print(NAME,PHONE,od1,od2,od3,od4)
        total=DESSERTS[od4]+BBQ[od3]+SEA[od2]+STARTERS[od1]
        return render_template("foodd.html",zameer=("Your total billing amount is :",total))
if __name__=="__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox

from sklearn.model_selection import train_test_split

import xgboost as xgb
from xgboost import XGBRegressor

def satıs_goruntuleme_islemleri():
    pencere3=tk.Tk()
    pencere3.geometry("1470x700+25+50")
    pencere3.config(bg="#aeb0d1")
    pencere3.title("Sales Management")
    pencere3.resizable(width="FALSE", height="FALSE")

    data=pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
    data=pd.DataFrame(data)
    data = data.drop('seller_type', axis=1)

    label_pen3_sentence=tk.Label(pencere3,text="List of Automobiles Sold",fg="black",bg="#aeb0d1",font="Times 24 bold")
    label_pen3_sentence.place(x=550,y=80)

    frame=tk.Frame(pencere3)
    frame.pack(expand=1)

    tv=ttk.Treeview(frame,columns=(1,2,3,4,5,6,7),show="headings")
    tv.pack()
    tv.heading(1, text="Model")
    tv.heading(2, text="Year")
    tv.heading(3, text="Price")
    tv.heading(4, text="KM-Driven")
    tv.heading(5, text="Fuel")
    tv.heading(6, text="Transmission")
    tv.heading(7, text="Owner")

    df_rows=data.to_numpy().tolist()
    for i in df_rows:
        tv.insert('','end',values=i)



def fiyat_hesaplama_islemleri():
    pencere4=tk.Tk()
    pencere4.geometry("600x600+350+100")
    pencere4.config(bg="#aeb0d1")
    pencere4.title("Sales Management")
    pencere4.resizable(width="FALSE", height="FALSE")


    def dataset_islemler():
        data=pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
        data=pd.DataFrame(data)
        data=data.drop('seller_type', axis=1)
        #data_last=pd.get_dummies(data,columns=['fuel', 'transmission', 'owner'], drop_first=True)
        data['fuel']=(data['fuel'] == "Diesel").astype(int)
        data['transmission'] = (data['transmission'] == "Manual").astype(int)
        data['owner'] = (data['owner'] == "First Owner").astype(int)
        y = data['selling_price']
        X = data.drop('selling_price', axis=1)
        X= X.drop('name',axis=1)
        print(X.head())
        print("\n")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        xgb1 = XGBRegressor(colsample_bytree=0.5, learning_rate=0.09, max_depth=4, n_estimators=2000)
        model_xgb = xgb1.fit(X_train, y_train)
        return  model_xgb

    def fiyat_tahmin():

        if fuel_entry.get() == "diesel" or "Diesel":
            fuel_ent=1
        else:
            fuel_ent=0

        if transmission_entry.get() == "manual" or "Manual":
            trans_ent=1
        else:
            trans_ent=0

        if owner_entry.get() == "first" or "First":
            own_ent=1
        else:
            own_ent=0


        yeni_veri=[[int(year_entry.get())],[int(km_driven_entry.get())],[int(fuel_ent)],[int(trans_ent)],[int(own_ent)]]
        yeni_veri=pd.DataFrame(yeni_veri).T
        df_2=yeni_veri.rename(columns={
            0:"year",
            1:"km_driven",
            2:"fuel",
            3:"transmission",
            4:"owner",
        })
        model_xgb=dataset_islemler()
        pred=model_xgb.predict(df_2)

        if(pred<0):
            pred= -1*pred
        pred=int(pred)

        lbl_fiyat_tahmin.config(text="Price: "+str(pred))

    lbl_predic_sentence=tk.Label(pencere4,text="Sales Price Forecast Calculator",fg="black",bg="#aeb0d1",font="Times 18 bold")
    lbl_predic_sentence.place(x=150,y=50)

    model_entry=tk.Entry(pencere4)
    model_entry.place(x=350,y=150)
    model_lbl=tk.Label(pencere4,text="Model",fg="black",bg="#aeb0d1",font="Times 13 bold")
    model_lbl.place(x=50,y=150)


    year_entry = tk.Entry(pencere4)
    year_entry.place(x=350, y=200)
    year_lbl = tk.Label(pencere4, text="Year (Just Year)",fg="black",bg="#aeb0d1",font="Times 13 bold")
    year_lbl.place(x=50, y=200)

    km_driven_entry = tk.Entry(pencere4)
    km_driven_entry.place(x=350, y=250)
    km_driven_lbl = tk.Label(pencere4, text="KM-Driven",fg="black",bg="#aeb0d1",font="Times 13 bold")
    km_driven_lbl.place(x=50, y=250)

    fuel_entry = tk.Entry(pencere4)
    fuel_entry.place(x=350, y=300)
    fuel_lbl = tk.Label(pencere4, text="Fuel (Petrol-Diesel)",fg="black",bg="#aeb0d1",font="Times 13 bold")
    fuel_lbl.place(x=50, y=300)

    transmission_entry = tk.Entry(pencere4)
    transmission_entry.place(x=350, y=350)
    transmission_lbl = tk.Label(pencere4, text="Transmission (Manual or Automatic)",fg="black",bg="#aeb0d1",font="Times 13 bold")
    transmission_lbl.place(x=50, y=350)

    owner_entry = tk.Entry(pencere4)
    owner_entry.place(x=350, y=400)
    owner_lbl = tk.Label(pencere4, text="Owner (First or Second)",fg="black",bg="#aeb0d1",font="Times 13 bold")
    owner_lbl.place(x=50, y=400)

    btn_fiyat_hesapla=tk.Button(pencere4,text="Make a Price Prediction",bg="#dece95",font="Times 18 bold",command=fiyat_tahmin)
    btn_fiyat_hesapla.place(x=150,y=450)

    lbl_fiyat_tahmin=tk.Label(pencere4,text="Price Prediction",fg="black",bg="#aeb0d1",font="Times 18 bold")
    lbl_fiyat_tahmin.place(x=180,y=500)

def pencere_show_islemler():
    pencere2=tk.Tk()
    pencere2.geometry("360x300+350+100")
    pencere2.config(bg="#aeb0d1")
    pencere2.title("Sales Management")
    pencere2.resizable(width="FALSE", height="FALSE")

    label_yazi=tk.Label(pencere2,text="Transactions",fg="black",bg="#aeb0d1",font="Times 16 bold")
    label_yazi.place(x=125,y=50)

    btn_satıs_goruntuleme=tk.Button(pencere2,text="Viewing Sales",bg="#dece95",font="Times 14 bold",command=satıs_goruntuleme_islemleri)
    btn_satıs_goruntuleme.place(x=120,y=100)

    btn_fiyat_hesaplama=tk.Button(pencere2,text="Price Prediction",bg="#dece95",font="Times 14 bold",command=fiyat_hesaplama_islemleri)
    btn_fiyat_hesaplama.place(x=110,y=160)

def login_check():
    if entry_username.get() == "admin" and entry_parola.get() == "1903":
        messagebox.showinfo("Login Succesfully")
        pencere_show_islemler()
    else:
        messagebox.showinfo("Login Failed")

pencere=tk.Tk()
pencere.geometry("360x300+350+100")
pencere.config(bg="#aeb0d1")
pencere.title("Sales Management")
pencere.resizable(width="FALSE",height="FALSE")

label_giris_sentence=tk.Label(text="Sales Management Information System",fg="black",bg="#aeb0d1",font="Times 14 bold")
label_giris_sentence.place(x=20,y=30)

label_username=tk.Label(text="Username",fg="black",bg="#aeb0d1",font="Times 12 bold")
label_username.place(x=75,y=80)

entry_username=tk.Entry()
entry_username.place(x=150,y=80)

label_parola=tk.Label(text="Password",fg="black",bg="#aeb0d1",font="Times 12 bold")
label_parola.place(x=75,y=120)

entry_parola=tk.Entry()
entry_parola.place(x=150,y=120)

btn_giris_Yap=tk.Button(text="Login",bg="#dece95",font="Times 12 bold",command=login_check)
btn_giris_Yap.place(x=150,y=180)

pencere.mainloop()
#200202100 MUSTAFA CAN ONCU
# importing module
import threading 
import urllib
import time
from concurrent.futures import ThreadPoolExecutor
from pandas import *
import pandas as pd
import re
import string
import numpy as np
import nltk
from nltk.corpus import stopwords
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tkinter as tk
form = tk.Tk()
form.geometry("1000x1500")
stopwords = nltk.corpus.stopwords.words("english")
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',6)
# reading CSV file
# data sayısını bulmak için print(len(data))
data = pd.read_csv('rows.csv', on_bad_lines='skip',low_memory=False)
data.pop('Date received')
data.pop('Sub-product')
data.pop('Sub-issue')
data.pop('Consumer complaint narrative')
data.pop('Company public response')
data.pop('Tags')
data.pop('Consumer consent provided?')
data.pop('Submitted via')
data.pop('Date sent to company')
data.pop('Company response to consumer')
data.pop('Timely response?')
data.pop('Consumer disputed?')
data = data.dropna().reset_index(drop=True)
# converting column data to list
try:
    product = data['Product'].tolist()
except:
    product = "bos"
try:
    issue = data['Issue'].tolist()
except:
    issue = "bos"
try:
    company = data['Company'].tolist()
except:
    company = "bos"
try:
    state = data['State'].tolist()
except:
    state = "bos"
try:
    complaint = data['Complaint ID'].tolist()
except:
    complaint = "bos"
try:
    zipCode = data['ZIP code'].tolist()
except:
    zipCode = "bos"
def remove_punc (txt):
    txt_nopunc = "".join([c for c in txt if c not in string.punctuation])
    return txt_nopunc
def tokenize (txt):
    tokens = re.split("\W+",txt)
    return tokens
def remove_stopwords (txt_tokenized):
    txt_clean = [word for word in txt_tokenized if word not in stopwords]
    return txt_clean

data ["Product"] = data ["Product"].apply(lambda x: remove_punc(x))
data ["Issue"] = data ["Issue"].apply(lambda x: remove_punc(x))
data ["Company"] = data ["Company"].apply(lambda x: remove_punc(x))
#tokenize ayirma
data ["Product_tokenized"] = data ["Product"].apply(lambda x: tokenize(x.lower()))
data ["Issue_tokenized"] = data ["Issue"].apply(lambda x: tokenize(x.lower()))
data ["Company_tokenized"] = data ["Company"].apply(lambda x: tokenize(x.lower()))
#stopword cikarma ve tokenized hali
data ["Product_stopword"] = data ["Product_tokenized"].apply(lambda x: remove_stopwords(x))
data ["Issue_stopword"] = data ["Issue_tokenized"].apply(lambda x: remove_stopwords(x))
data ["Company_stopword"] = data ["Company_tokenized"].apply(lambda x: remove_stopwords(x))
x=0
y=0
print(len(data["Product_stopword"]))
#product function
def product():
    x = entry.get()
    y = entry2.get()
    bir = data["Product_stopword"][float(x)]
    iki = data["Product_stopword"][float(y)]
    benzer_kelime = 0
    payda = 0
    for i in bir:
        if i in iki:
            ortaklar = i
            ortak_controller["text"] = ortaklar
            benzer_kelime = benzer_kelime + 1
            print(benzer_kelime)
    if (len(bir) > len(iki)):
        payda = len(bir)
    elif (len(iki) > len(bir)):
        payda = len(iki)
    else:
        payda = len(bir)
    benzerlik = float(benzer_kelime / payda)
    result_label["text"] = float(benzerlik)

#issue function
def issue():
    x = entry3.get()
    y = entry4.get()
    bir = data["Issue_stopword"][float(x)]
    iki = data["Issue_stopword"][float(y)]
    benzer_kelime = 0
    payda = 0
    for i in bir:
        if i in iki:
            ortaklar = i
            ortak_controller["text"] = ortaklar
            benzer_kelime = benzer_kelime + 1
    if (len(bir) > len(iki)):
        payda = len(bir)
    elif (len(iki) > len(bir)):
        payda = len(iki)
    else:
        payda = len(bir)
    benzerlik = float(benzer_kelime / payda)
    result_label["text"] = float(benzerlik)
#company function
def company():
    x = entry5.get()
    y = entry6.get()
    bir = data["Company_stopword"][float(x)]
    iki = data["Company_stopword"][float(y)]
    benzer_kelime = 0
    payda = 0
    for i in bir:
        if i in iki:
            ortaklar = i
            ortak_controller["text"] = ortaklar
            benzer_kelime = benzer_kelime + 1
    if (len(bir) > len(iki)):
        payda = len(bir)
    elif (len(iki) > len(bir)):
        payda = len(iki)
    else:
        payda = len(bir)
    benzerlik = float(benzer_kelime / payda)
    result_label["text"] = float(benzerlik)

#total icin deneme

def product_kiyas():
    zamaninBaslangici = time.time()
    y = 0
    x = entry7.get()
    oran = entry8.get()
    sayac=0
    for i in range(1167022):
        bir = data["Product_stopword"][float(x)]
        iki = data["Product_stopword"][int(y)]
        benzer_kelime = 0
        payda = 0
        for i in bir:
            if i in iki:
                ortaklar = i
                ortak_controller["text"] = ortaklar
                benzer_kelime = benzer_kelime + 1
        if (len(bir) > len(iki)):
            payda = len(bir)
        elif (len(iki) > len(bir)):
            payda = len(iki)
        else:
            payda = len(bir)
        benzerlik = float(benzer_kelime / payda)
        result_label["text"] = float(benzerlik)
        if float(benzerlik) > float(oran):
            print(sayac)
            print(benzerlik)
        y += 1
        sayac += 1
    zamaninBitisi = time.time()
    print(zamaninBitisi-zamaninBaslangici)

def issue_kiyas():
    zamaninBaslangici = time.time()
    y = 0
    x = entry9.get()
    oran = entry10.get()
    sayac=0
    for i in range(1167022):
        bir = data["Issue_stopword"][float(x)]
        iki = data["Issue_stopword"][int(y)]
        benzer_kelime = 0
        payda = 0
        for i in bir:
            if i in iki:
                ortaklar = i
                ortak_controller["text"] = ortaklar
                benzer_kelime = benzer_kelime + 1
        if (len(bir) > len(iki)):
            payda = len(bir)
        elif (len(iki) > len(bir)):
            payda = len(iki)
        else:
            payda = len(bir)
        benzerlik = float(benzer_kelime / payda)
        result_label["text"] = float(benzerlik)
        if float(benzerlik) > float(oran):
            print(sayac)
            print(benzerlik)
        y += 1
        sayac += 1
    zamaninBitisi = time.time()
    print(zamaninBitisi-zamaninBaslangici)

def company_kiyas():
    zamaninBaslangici = time.time()
    y = 0
    x = entry11.get()
    oran = entry12.get()
    sayac=0
    for i in range(1167022):
        bir = data["Company_stopword"][float(x)]
        iki = data["Company_stopword"][int(y)]
        benzer_kelime = 0
        payda = 0
        for i in bir:
            if i in iki:
                ortaklar = i
                ortak_controller["text"] = ortaklar
                benzer_kelime = benzer_kelime + 1
        if (len(bir) > len(iki)):
            payda = len(bir)
        elif (len(iki) > len(bir)):
            payda = len(iki)
        else:
            payda = len(bir)
        benzerlik = float(benzer_kelime / payda)
        result_label["text"] = float(benzerlik)
        """if float(benzerlik) > float(oran):
            print(sayac)
            print(benzerlik)"""
        y += 1
        sayac += 1
    zamaninBitisi = time.time()
    print(zamaninBitisi-zamaninBaslangici)
       
def yavasThreadlerimProduct():
    print("thread 1 calisiyor")  
    pool = ThreadPoolExecutor(max_workers=20000)
    work1 = pool.submit(product_kiyas)  
    

def ortaThreadlerimProduct():
    print("thread 2 calisiyor")  
    pool = ThreadPoolExecutor(max_workers=200)
    work1 = pool.submit(product_kiyas)
    work2 = pool.submit(product_kiyas)
    work3 = pool.submit(product_kiyas)

def hizliThreadlerimProduct():
    print("thread 3 calisiyor")
    pool = ThreadPoolExecutor(max_workers=2000)
    work1 = pool.submit(product_kiyas)
    work2 = pool.submit(product_kiyas)
    work3 = pool.submit(product_kiyas)
    work4 = pool.submit(product_kiyas)


def yavasThreadlerimIssue():
    pool = ThreadPoolExecutor(max_workers=20000)
    work1 = pool.submit(issue_kiyas)   
    print("thread 1 calisiyor")   

def ortaThreadlerimIssue():
    pool = ThreadPoolExecutor(max_workers=200)
    work1 = pool.submit(issue_kiyas)    
    work2 = pool.submit(issue_kiyas)    
    work3 = pool.submit(issue_kiyas)  
    print("thread 2 calisiyor")    

def hizliThreadlerimIssue():
    print("thread 3 calisiyor")     
    pool = ThreadPoolExecutor(max_workers=2000)
    work1 = pool.submit(issue_kiyas)    
    work2 = pool.submit(issue_kiyas)    
    work3 = pool.submit(issue_kiyas)    
    work4 = pool.submit(issue_kiyas)
       

def yavasThreadlerimCompany():
    pool = ThreadPoolExecutor(max_workers=20)
    work1 = pool.submit(company_kiyas)  
    print("thread 1 calisiyor")  

def ortaThreadlerimCompany():
    pool = ThreadPoolExecutor(max_workers=200)
    work1 = pool.submit(company_kiyas)
    work2 = pool.submit(company_kiyas)
    work3 = pool.submit(company_kiyas)
    print("thread 2 calisiyor")  

def hizliThreadlerimCompany():
    pool = ThreadPoolExecutor(max_workers=2000)
    work1 = pool.submit(company_kiyas)
    work2 = pool.submit(company_kiyas)
    work3 = pool.submit(company_kiyas)
    work4 = pool.submit(company_kiyas)
    print("thread 3 calisiyor")  

def karisikCagirProduct():
    print("thread1")
    hizliThreadlerimProduct()
    print("thread2")
    yavasThreadlerimProduct()
    print("thread3")
    ortaThreadlerimProduct()

def karisikCagirCompany():
    hizliThreadlerimCompany()
    yavasThreadlerimCompany()
    ortaThreadlerimCompany()

def karisikCagirIssue():
    hizliThreadlerimIssue()
    yavasThreadlerimIssue()
    ortaThreadlerimIssue()

form.title("Yazlab-1 PROJE 2 ")
form.config(bg="#F3E9DD")
baslik = tk.Label(text="Data Yönetim Uygulamasına Hoş Geldiniz!",fg="#FDF6EC",bg="#DAB88B",font="Times 20 italic")
baslik.pack()

selection1 = tk.Label(text="1)Product değerlerini kıyaslamak için değer giriniz",fg="#FDF6EC",bg="#DAB88B",font="Times 15 italic")
selection1.pack()
entry = tk.Entry(text="kıyaslamak istediğiniz ilk değeri giriniz",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry.pack()
entry2 = tk.Entry(text="kıyaslamak istediğiniz ikinci değeri giriniz",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry2.pack()
buton = tk.Button(form,text="Product Al",fg="black",bg="#DAB88B",font="Times 15 italic",command=product)
buton.pack()

selection2 = tk.Label(text="2)Issue değerlerini kıyaslamak için değer giriniz",fg="#FDF6EC",bg="#DAB88B",font="Times 15 italic")
selection2.pack()
entry3 = tk.Entry(text="kıyaslamak istediğiniz ilk değer",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry3.pack()
entry4 = tk.Entry(text="kıyaslamak istediğiniz ikinci değer",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry4.pack()
buton2 = tk.Button(form,text="Issue Al",fg="black",bg="#DAB88B",font="Times 15 italic",command=issue)
buton2.pack()

selection3 = tk.Label(text="3)Company değerlerini kıyaslamak için değer giriniz",fg="#FDF6EC",bg="#DAB88B",font="Times 15 italic")
selection3.pack()
entry5 = tk.Entry(text="kıyaslamak istediğiniz ilk değeri girn",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry5.pack()
entry6 = tk.Entry(text="kıyaslamak istediğiniz ikinci değeri girn",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry6.pack()
buton3 = tk.Button(form,text="Company Al",fg="black",bg="#DAB88B",font="Times 15 italic",command=company)
buton3.pack()

selection4 = tk.Label(text="4) Tüm Product Benzerlik oranlarını kıyaslamak için ilk kutucuğa product değerini ikinci kutucuğa benzerlik oranını giriniz(%60 için 0.6 giriniz...)",fg="#FDF6EC",bg="#DAB88B",font="Times 15 italic")
selection4.pack()
entry7 = tk.Entry(text="kıyaslamak istediğiniz ilk deei girin",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry7.pack()
entry8 = tk.Entry(text="kıyaslamak istediğin ikinci deeri girin",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry8.pack()
"""
buton4 = tk.Button(form,text="En çok sayıda thread ile product karşılaştırma için tıklayınız",fg="black",bg="#DAB88B",font="Times 15 italic",command=yavasThreadlerimProduct)
buton4.pack()
ortabuton1 = tk.Button(form,text="Ortalamada sayıda thread ile product karşılaştırma için tıklayınız",fg="black",bg="#DAB88B",font="Times 15 italic",command=ortaThreadlerimProduct)
ortabuton1.pack()
hizlibuton1 = tk.Button(form,text="En az sayıda thread ile product karşılaştırma için tıklayınız",fg="black",bg="#DAB88B",font="Times 15 italic",command=hizliThreadlerimProduct)
hizlibuton1.pack()
tumthreadlerbutonu = tk.Button(form,text="",fg="black",bg="#DAB88B",font="Times 15 italic",command=yavasThreadlerimProduct)
tumthreadlerbutonu = tk.Button(form,text="",fg="black",bg="#DAB88B",font="Times 15 italic",command=hizliThreadlerimProduct)
tumthreadlerbutonu = tk.Button(form,text="",fg="black",bg="#DAB88B",font="Times 15 italic",command=ortaThreadlerimProduct)
tumthreadlerbutonu.pack()"""
tumthreadlerbutonu = tk.Button(form,text="multithreading product",fg="black",bg="#DAB88B",font="Times 15 italic",command=karisikCagirProduct)
tumthreadlerbutonu.pack()

selection5 = tk.Label(text="5) Tüm Issue Benzerlik oranlarını kıyaslamak için ilk kutucuğa issue değerini ikinci kutucuğa benzerlik oranını giriniz(%60 için 0.6 giriniz...)",fg="#FDF6EC",bg="#DAB88B",font="Times 15 italic")
selection5.pack()
entry9 = tk.Entry(text="kıyasistediğiniz ilk deeri grin",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry9.pack()
entry10 = tk.Entry(text="kıyistediğin ikinci değerigirin",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry10.pack()
buton5 = tk.Button(form,text="Issueeee Al",fg="black",bg="#DAB88B",font="Times 15 italic",command=issue_kiyas)
buton5.pack()
tumthreadlerbutonu2 = tk.Button(form,text="multithreading issue",fg="black",bg="#DAB88B",font="Times 15 italic",command=karisikCagirIssue)
tumthreadlerbutonu2.pack()

selection6 = tk.Label(text="6) Tüm Company Benzerlik oranlarını kıyaslamak için ilk kutucuğa company değerini ikinci kutucuğa benzerlik oranını giriniz(%60 için 0.6 giriniz...)",fg="#FDF6EC",bg="#DAB88B",font="Times 15 italic")
selection6.pack()
entry11 = tk.Entry(text="kısistediğiniz ilk deeri girin",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry11.pack()
entry12= tk.Entry(text="Oranınınızı giirlinz lutfen",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry12.pack()
buton6 = tk.Button(form,text="Companyyy Al",fg="black",bg="#DAB88B",font="Times 15 italic",command=company_kiyas)
buton6.pack()
tumthreadlerbutonu3 = tk.Button(form,text="multithreading company",fg="black",bg="#DAB88B",font="Times 15 italic",command=karisikCagirCompany)
tumthreadlerbutonu3.pack()

"""selection5 = tk.Label(text="Kaç tane thread Kullanacağınızı seçmek için değer giriniz",fg="#FDF6EC",bg="#DAB88B",font="Times 15 italic")
selection5.pack()
entry9 = tk.Entry(text="thread sayısı giriniz...",fg="black",bg="#FDF6EC",font="Times 15 italic")
entry9.pack()"""

def veri_sil():
    entry.delete(0,"end")
    entry2.delete(0,"end")
    entry3.delete(0, "end")
    entry4.delete(0, "end")
    entry5.delete(0, "end")
    entry6.delete(0, "end")
    ortak_controller.delete(0,"end")

result_label = tk.Label(text = "Değer",fg="#FDF6EC",bg="#DAB88B",font="Times 20 italic")
result_label.pack()
ortak_controller = tk.Label(text="ortaklarm",fg="black",bg="#FDF6EC",font="Times 20 italic")
ortak_controller.pack()
print(data.head(20).to_string())
form.mainloop()
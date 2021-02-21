# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:40:26 2021

@author: Umut Atakul

"""

#Problem 2 (Even Fibonacci numbers)

EvenFib = [] #Çift Fibonacci Sayılarını biriktireceğimiz Liste
 
a,b= 1,2 #Başlangıç değerlerini (a birinci terim b ikinci terimimiz olacak şekilde) 1 ve 2 olarak atadık
n=4000000 #Üst limitimizi belriledik
while a<=n:  #Sayımız 4 milyonun altı olduğu sürece döngü devam edecek
    if a%2==0:   #Sayı çift ise    
        EvenFib.append(a) #Listeye sayıyı ekleyecek
        
    a,b=b,a+b #Fibonnaci serisini tanımladığımız fonksiyon
toplam=sum (EvenFib) #Çift Fibonacci sayılarını tanımladığımız fonksiyon

print (toplam)
    

    
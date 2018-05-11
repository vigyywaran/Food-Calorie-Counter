#! /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import collections
import csv

def name2():
  carbs=[]
  protein=[]
  fat=[]
  item=[]
  y_pos=0
  width=0.35
  i=0
  f=open('test.txt','r')
  while True:
    st=f.readline()
    l=len(st)
    if l!=0:
      n=st.rfind(' ')
      str1=st[:n].strip()
      item.append(str1)
      i+=1
    else:
      break
  print(item)
  print(i)
  i=0
  y_pos=np.arange(5)
  while True:
    with open('prefinal.csv') as csvfile:
      read=csv.reader(csvfile)
      for row in read:
        str2=str(row[0]).strip()
        if str2 == item[i]:
          print(i,str2)
          carbs.append(float(row[2]))
          protein.append(float(row[3]))
          fat.append(float(row[4]))
          i+=1
          print(i)
          if i>4:
            print('Hey')
            break
    if i>4:
      print('Hey')
      break
  print(item)
  print(carbs)
  print(protein)
  print(fat)
  fig, ax=plt.subplots()
  width=0.25
  fig=plt.Figure()
  fig.set_canvas(plt.gcf().canvas)
  p1=ax.bar(y_pos,carbs,width)
  p2=ax.bar(y_pos+width,protein,width)
  p3=ax.bar(y_pos+2*width,fat,width)
  ax.set_xticks(y_pos+width/3)
  ax.set_xticklabels(item)
  ax.legend((p1[0],p2[0],p3[0]),('Carbs','Protein','Fats'))
  #ax.yaxis.set_units(inch)
  ax.autoscale_view()
  plt.ylabel('Calories')
  ax.set_title('Calories for Food Labels')
  fig.savefig("static/groupedbargraph" + ".png",format='png')
  #plt.show()

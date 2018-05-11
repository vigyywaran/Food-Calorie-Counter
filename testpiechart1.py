#! /usr/bin/python3

# This python script creates a piechart of the various categories displayed as a result of labelling the input image. The piechart is stored as a png file for later use.
import matplotlib.pyplot as plt
import collections
import csv

def name1():
  percentage=[]
  item=[]
  #labels=[]
  calorie={}
  explodearray=[0.0,0.0,0.0,0.0,0.0,0.0]
  i=0
  total=0
  # The following code gets the food labels and their respective accuracy scores and stores them in item[] list and percentage[] list respectively.
  f=open('test.txt','r')
  while True:
    st=f.readline()
    l=len(st)
    if l!=0:
      n=st.rfind(' ')
      num=st[n:-1].strip()
      percentage.append(float(num))
      total=total+float(num)
      str2=st[:n].strip()
      item.append(str2)
      i+=1
    else:
      break
  # The following code gets the calorie values of the food labels in item[] and stores it in calorie{} dictionary.
  i=0
  while True:
    with open('prefinal.csv') as csvfile:
      read=csv.reader(csvfile)
      for row in read:
        str2=str(row[0]).strip()
        if str2 == item[i]:
          calorie.update({item[i]:(row[1])})
          i+=1
          if i>4:
            break
      if i>4:
         break
  print(calorie)
  # Others is used to pad the piechart to get a total of 100% in case the various label accuracies dont add up to 100
  item.append('others')
  percentage.append(1-total)
  print(percentage,item)
  # Shows and Saves piechart created
  fig=plt.Figure()
  fig.set_canvas(plt.gcf().canvas)
  p1=plt.pie(percentage,explode=explodearray,labels=item,autopct='%1.1f%%',rotatelabels=True)
  plt.legend(p1[0],list(calorie.values()),loc='lower left')
  #plt.legend(p1[0],labels,loc='lower left')
  plt.title('CALORIES OF FOOD LABELS')
  fig.savefig("static/piechart" + ".png",format='png')
  #plt.show()

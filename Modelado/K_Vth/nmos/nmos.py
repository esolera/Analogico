import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def derivada(x,y):
	der=np.diff(y) / np.diff(x)
	return der
def puntos_medio(x):
	x2=[]
	for i in range(len(x)-1):
		x2.append((x[i]+x[i+1])/2)
	return x2
def find_point(y,punto):
	for i in range(len(y)):
		if y[i]<punto :
			a=i;
	return a

def pendiente (x,y,index):
	m=(y[index]-y[index+1])/(x[index]-x[index+1])
	return m
def obtener_b(x,y,index,m):
	b=y[index]-m*x[index]
	return b
def lineal(x,m,b):
	lineal=[]
	for i in range(len(x)):
		lineal.append(m*x[i]+b)
	return lineal
df = pd.read_csv("/media/esolera/ExtraDrive1/TEC/cuatri_2/analogico/hspice_Analogico/modelado/Vth_k/nmos.csv",header=None)
x_axis=df[0]
y_axis=df[1]*1e6


#der = derivada(x_axis,y_axis)*1e6
#x2=puntos_medio(x_axis)
#Indexado del mejor punto de la derivada
index=find_point(x_axis,0.88)
m=pendiente(x_axis,y_axis,index)
b=obtener_b(x_axis,y_axis,index,m)
lineal=lineal(x_axis,m,b)


#Resultados
print("la pendiente es %f" %m)
vth=(-b)/m
print("El Vth es %f V" %vth)
k=(m/14)*2
print("El K es igual a %f" %k)
gm=np.sqrt(k*10*(14/2)*2)
print("El gm a 10uA es de %f" %gm)
plt.ylim(ymin=0,ymax=1200)
plt.plot(x_axis,lineal)
plt.plot(x_axis,y_axis)
plt.show()

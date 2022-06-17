import pandas as pd 
import numpy as np 
from pandas_profiling import ProfileReport

n=input("enter name of file")

data=pd.read_csv("heart.csv")

profile=ProfileReport(data)

profile.to_file(output_file= n+".html")

input("press enter for close program")

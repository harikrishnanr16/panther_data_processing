import pandas as pd 
import ast 
import numpy as np
import json
import pandas as pd 
from pandas.io.json import json_normalize
import sys


with open(sys.argv[1]) as f:
    d = json.load(f)

dd=json_normalize(d["overrepresentation"])


print(dd)

dd=dd[["group"]]


works_data = json_normalize(data=d['overrepresentation'], record_path='group')

first=works_data.dropna(subset=["result.input_list.mapped_id_list.mapped_id"])
first=first[["result.term.id","result.term.level","result.input_list.mapped_id_list.mapped_id"]]
first.columns=["GoTerm","Level","mapped_id"]
print(first)

rest=works_data.dropna(subset=["result"])



d=rest["result"].explode().reset_index()




def get_data(x):
    try:
        return(x["term"].values[0],x["term"].values[1],x["input_list"].values[2])
    except IndexError:
        return(x["term"].values[0],x["term"].values[1],np.nan)


xl=[]

for i in d["result"]:
    
    dff=pd.DataFrame.from_dict(i).reset_index()
    l=["id","level","mapped_id_list"]
    dff=dff[dff["index"].isin(l)]
    dff=dff.drop(["number_in_reference"],axis=1)
    try:
        xl.append((dff["term"].values[0],dff["term"].values[1],dff["input_list"].values[2]))
    except IndexError:
        xl.append((dff["term"].values[0],dff["term"].values[1],np.nan))

ddd=pd.DataFrame(xl,columns=["GoTerm","Level","Mappedid"])

ddd[["x","mapped_id"]]=ddd["Mappedid"].apply(pd.Series)
ddd=ddd.drop(["x","Mappedid"],axis=1)
print(ddd)

dfd=pd.concat([first,ddd])

print(dfd)

dfd.to_csv(sys.argv[1].split(".")[0]+".txt",sep="\t")






    

    
    
    
    
    
    

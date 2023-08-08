import Pre_processing as pp 
import emotions as em
import matplotlib.pyplot as plt 


fig= plt.figure()
plt.bar(em.count.keys(),em.count.values())
plt.xlabel("emotions")
plt.ylabel("frequency")
fig.autofmt_xdate()
plt.savefig("Bar_Graph.png")
plt.show()
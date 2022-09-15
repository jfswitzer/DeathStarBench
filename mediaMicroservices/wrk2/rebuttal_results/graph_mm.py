import matplotlib.pyplot as plt
import pandas as pd
import os

FONTSIZE=11
fig, axs = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(hspace=0)
fig.set_size_inches(7,3.5)
markers=["s","s","s","s","s","s","s"]
colors=['black','#FF595E','#FFCA3A','#8AC926','#1982C4','#6A4C93']
directorys=['/home/jen/DeathStarBench/mediaMicroservices/wrk2/results/2phones','/home/jen/DeathStarBench/mediaMicroservices/wrk2/results/3phones']
titles=['2 Phones',"3 Phones"]
labels=['2 Phones',"3 Phones"]
def extract(line):
    si = line.index("%")+1
    se = len(line)-3
    units = line[-3:].strip()
    n = float(line[si:se].strip())
    if units=='ms':
        n = n*1
    elif units=='s':
        n = n*1000
    return n
def fparse(fname):
    with open(fname,"r") as f:
        lines = f.readlines()
        l50 = -1
        l90 = -1
        qps = -1
        for line in lines:
            if "50.000%" in line:
                l50 = extract(line)
            elif "90.000%" in line:
                l90 = extract(line)
            elif "Requests/sec" in line:
                si = line.index(':')+1
                v = line[si:].strip()
                qps=float(v)
        return l50,l90,qps
def extract_qps(fname):
    filename = os.fsdecode(fname)
    if not filename.endswith(".out"):
        return -1
    qps = filename.split('_')[2][1:-4]
    return int(qps)
def extract_dir(directorystr,title,color='black',marker="o"):
    #linestyle="dotted"
    linestyle="solid"
    if title=="Phone Cluster":
        linestyle="solid"
    directory = os.fsencode(directorystr)
    l50s = []
    l90s = []
    qpss = []
    files = [f for f in os.listdir(directory)]
    files.sort(key=lambda x: extract_qps(x))
    for file in files:
        filename = os.fsdecode(file)
        if filename.endswith(".out"):
            l50,l90,qps=fparse(directorystr+'/'+filename)
            #if l50<5 or l90<5:
            #    #outlier,todo make smaerter
            #    continue            
            l50s.append(l50)
            l90s.append(l90)
            qpss.append(qps)
    axs[0].scatter(qpss,l50s,label=title,color=color,marker=marker)
    axs[0].plot(qpss,l50s,linestyle=linestyle,color=color)    
    axs[0].set_ylabel("50% Latency (ms)",fontsize=FONTSIZE)
    axs[1].scatter(qpss,l90s,label=title,color=color,marker=marker)
    axs[1].plot(qpss,l90s,linestyle=linestyle,color=color)    
    axs[1].set_ylabel("90% Latency (ms)",fontsize=FONTSIZE)

for d in range(len(directorys)):
    extract_dir(directorys[d],titles[d],color=colors[d],marker=markers[d])
axs[0].legend(bbox_to_anchor=(1.01, 1.1))
axs[0].set_ylim(0,400)
#axs[0].set_xlim(5,200)
axs[1].set_ylim(0,400)
#axs[1].set_xlim(5,200)
plt.xlabel('Throughput (Requests/sec)',fontsize=FONTSIZE)
axs[0].grid(axis='y',linestyle="dashed")
axs[1].grid(axis='y',linestyle="dashed")
plt.savefig("graph_mm.eps",format="eps")
plt.tight_layout()
plt.show()

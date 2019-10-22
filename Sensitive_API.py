#Android Application Graph Signature 
# © Created By - Devyani Vij and Riya Khan
#Header Files
import optparse
import networkx as nx
import re
import matplotlib.pyplot as plt
import pylab
import warnings
import os
import glob
import fnmatch
import pyfiglet
import warnings

warnings.filterwarnings("ignore")

#Banner
ascii_banner = pyfiglet.figlet_format("Sensitive \t APIs",width=1000)
print(ascii_banner)

#options
parser = optparse.OptionParser()

parser.add_option("-p","--path",dest="path",help="Input the Path of the Graph.")
parser.add_option("-g","--graph",dest="graph",help="Input the Name of the Graph.")
(options,arguments)=parser.parse_args()

if not options.path:
    parser.error("[-] Please specify the Path of the GML using -p or --path")
elif not options.graph:
    parser.error("[-] Please specify the GRAPH name by using -g or --graph")

os.getcwd()
os.chdir(options.path)
os.getcwd()

arr = [x for x in os.listdir() if x.endswith(options.graph)] 


#Reading the Callgraphs created using androguard tool
G2 = nx.read_gml(arr[0],label='label') 

#List containing the names of all the sensitive API classes.
sensitive_api=['TelephonyManager','SmsManager','LocationManager','AudioManager','HttpURLConnection','ConnectivityManager','BroadcastReceiver','Cipher','AccessibleObject','PackageManager']

sensitive_api_malware=[]

count_api_in_malware = 0

#Using Regex to fetch all the sensitive API calls from the call graphs and counting the TOTAL number of sensitive API in Application
for j in sensitive_api:
    for i in G2.nodes():
        data = re.split('[;]',i)
        data1 = re.split('/',data[0])
        for k in data1:
            if k in sensitive_api:
                if i in sensitive_api_malware:
                    continue
                else:
                    sensitive_api_malware.append(i)
                    count_api_in_malware=count_api_in_malware+1

print('\033[93m'+"Total Sensitive API Calls found in the MALWARE: "+str(count_api_in_malware))

#Reading the graph of the Application 
G = nx.read_gml('callgraph.gml',label='id')

data=[]

b=nx.get_node_attributes(G,'label')

for keys,values in b.items():
    splitting = re.split('[[]',values)
    if splitting[0] in sensitive_api_malware:
        data.append(keys)

#Getting the CALLER and CALLEE relationship between the Sensitive API's fetched above.
listing=[]
U = nx.DiGraph()
counter_in_degree=0
for i in data:
        
        a=G.in_edges(i)
        for j in a:
            b=list(j)
            for k in b:
                if k in data:
                    if G.nodes[k]['label'] not in listing:
                        listing.append(G.nodes[k]['label'])
                        counter_in_degree=counter_in_degree+G.in_degree(i)
                    else:
                        continue
                else:
                    continue

#Sorting the API names in ascending order to construct a DiGraph showing a relation between caller and callee.
sensitive_api_in_malware_name=[]
for el in sorted(listing):
    sensitive_api_in_malware_name.append(el)

for i in range(0,len(sensitive_api_in_malware_name)):
    print('\033[96m'+sensitive_api_in_malware_name[i])

print("\n")     

# Extracting Sensitive API Calls of Android Malware Applications

<!-- Library Logo -->
<img height=150 src="https://github.com/devu-62442/Extracting-Sensitive-API-Calls/blob/master/img/images.png" align="left" hspace="1" vspace="1">

<img align="right" height='50' src='https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/dims.jpeg' alt='Buy Me a Coffee at ko-fi.com' /></a>

## Android API
What is Android ? Please read 👉🏻 [**Android**](https://developer.android.com).
An ```Application Programming Interface (API)``` is an interface or communication protocol between a client and a server intended to simplify the building of client-side software. It has been described as a “contract” between the client and the server, such that if the client makes a request in a specific format, it will always get a response in a specific format or initiate a defined action. In building applications, an API simplifies programming by abstracting the underlying implementation and only exposing objects or actions the developer needs. 

[**Android**](https://developer.android.com) is a layered architecture. The APIs lie in the second layer (from the top) called as Application Framework. 

![Python](https://github.com/devu-62442/Extracting-Sensitive-API-Calls/blob/master/img/Architecture.png)

## Application Framework
Application framework layer is on top of native library layer. The application layer provides major Application programming interface (APIs) and higher-level services in the form of java classes. The application developers are allowed to access all the APIs framework for the core programs that make simpler the reuse of APIs components. These APIs are open to everybody to create android applications. There is different type of application components. Each type has a different lifecycle and purpose that describes how the component will be created and destroyed.
</br>

## Sensitive API
There is no definite defination for Sensitive APIs. Sensitive API's are the API's which handles the sensitive information in Android Devices. Now the sensitive information can be personal information rendering, it can be reading of databases, it can be sensing and receiving sms etc. 

In this tool the Sensitive API's are the set of APIs which are used to access ```Sensitive Resources``` on the Android Device. Sensitive Resources such as Devce ID of the Application, Location of the user, getting the information about Network Type.

There are around 20 API classes which comes under Sensitive API category. All these API classes will have different API metods which are used to detected the malicious behaviour in an Application.

E.g.-
- Landroid/telephony/TelephonyManager;->listen(Landroid/telephony/PhoneStateListener; I)V
- Landroid/telephony/TelephonyManager;->getNetworkType()I
- Landroid/net/ConnectivityManager;->getActiveNetworkInfo()Landroid/net/NetworkInfo;
- Landroid/content/pm/PackageManager;->isSafeMode()Z
    
In the above examples ```TelephonyManager, ConnectivityManager, PackageManager``` are the API classes and ```listen(), getNetworkType(), getActiveNetworkInfo(), isSafeMode()``` are the API Methods.




<!-- Packages Used -->
![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6e6574776f726b782e737667-2.svg)
![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f7472617669732d63692e6f72672f6e6574776f726b782f6e6574776f726b782e7376673f6272616e63683d6d6173746572.svg) ![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f6769746875622f6e6574776f726b782f6e6574776f726b783f6272616e63683d6d6173746572267376673d74727565.svg)

## Why Graphs ?
Graphs are mathematical structures that represent pairwise relationships between objects. A graph is a flow structure that represents the relationship between various objects. It can be visualized by using the following two basic components:

Nodes: These are the most important components in any graph. Nodes are entities whose relationships are expressed using edges. 

Edges: Edges are the components that are used to represent the relationships between various nodes in a graph. An edge between two nodes expresses a one-way or two-way relationship between the nodes.

<img height=200 align="center" src="https://github.com/devu-62442/Static_Malware_Family_Classifier_based_on_Graph_Comparison/blob/master/img/200.gif"  hspace="1" vspace="1">


### The Android Application graphs are called as ```Callgraph ```. 

### A call graph (also known as a call multigraph) is a control flow graph, which represents calling relationships between API's in an Android Application. 

Each node represents an API and each edge (a, b) indicates that API a calls API b. Call graphs can be dynamic or static. A dynamic call graph is a record of an execution of the Android Application. Thus, a dynamic call graph can be exact, but only describes one run of the application. A static call graph is a call graph intended to represent every possible execution of the Android Application.

Call graphs can be defined to represent varying degrees of precision. A more precise call graph more precisely approximates the behavior of the real Android Application, at the cost of taking longer to compute and more memory to store. The most precise call graph is fully context-sensitive, which means that for each application, the graph contains a separate node for each call stack that application have in it.

## Working
Written in python ![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6e6574776f726b782e737667-2.svg). 
</br>
</br>
<a href='https://networkx.github.io/documentation/stable/' /><img align='left' height='100' src='https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/networkx_logo_1.png' /></a>
</br>
The main package used is networkx. This package of python helps to work with graphs. Tap the icon to know more.
</br>
</br>
</br>
```It's used to classify an Android Application into its Malware Family```. 

<img height=450 src="https://github.com/devu-62442/Static_Malware_Family_Classifier_based_on_Graph_Comparison/blob/master/img/android-marching-malware.jpg" align="left" hspace="1" vspace="1">

Every family has a characteristics called as ```SENSITIVE API```. These ```Sensitive API's``` set is unique for a Malware Family. Using these a ````Caller-Callee```` relationship is detected and represented as a callgraph (.gml). You can learn more about it in other repository [**Android Application Signature Creator Based on Graphs**](https://github.com/devu-62442/Android_Application_Signature_Creator).

The tool follows the following steps :-

#### Step #1. Clone and Download the code and the given DATASET folder as github says - ![GitHub](https://github.com/devu-62442/Static_Malware_Family_Classifier_based_on_Graph_Comparison/blob/master/img/git.svg)

#### Step #2. Use the below command in the command-prompt to run the program ```MalwareFamily_Classifier.py```

```gradle
python3 MalwareFamily_Classifier.py -p [Path of your GML (Callgraph) Application] -g [Name of the GML (Callgraph)] -d [Path where dataset is stored]
```
<img height=200 src="https://github.com/devu-62442/Static_Malware_Family_Classifier_based_on_Graph_Comparison/blob/master/img/Screenshot%202019-10-21%20at%206.33.43%20PM.png" align="center" hspace="1" vspace="1">

#### Step #3. Output
The code will give you the name of the family it belongs to or will give you that it is ```UNKNOWN/GOODWARE```
</br>
<img height=200 src="https://github.com/devu-62442/Static_Malware_Family_Classifier_based_on_Graph_Comparison/blob/master/img/Screenshot%202019-10-21%20at%206.40.28%20PM.png" align="center" hspace="1" vspace="1">


<img height=200 src="https://github.com/devu-62442/Static_Malware_Family_Classifier_based_on_Graph_Comparison/blob/master/img/Screenshot%202019-10-21%20at%206.41.37%20PM.png" align="center" hspace="1" vspace="1">

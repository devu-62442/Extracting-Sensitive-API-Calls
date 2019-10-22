# Extracting Sensitive API Calls in Malware Applications 
##### Android

<!-- Library Logo -->
<img height=150 src="https://github.com/devu-62442/Extracting-Sensitive-API-Calls/blob/master/img/images.png" align="left" hspace="1" vspace="1">

<img align="right" height='50' src='https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/dims.jpeg' alt='Buy Me a Coffee at ko-fi.com' /></a>
<!-- Packages Used -->
![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6e6574776f726b782e737667-2.svg)
![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f7472617669732d63692e6f72672f6e6574776f726b782f6e6574776f726b782e7376673f6272616e63683d6d6173746572.svg) ![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f6769746875622f6e6574776f726b782f6e6574776f726b783f6272616e63683d6d6173746572267376673d74727565.svg)

An ```Application Programming Interface (API)``` is an interface or communication protocol between a client and a server intended to simplify the building of client-side software. It has been described as a “contract” between the client and the server, such that if the client makes a request in a specific format, it will always get a response in a specific format or initiate a defined action. In building applications, an API simplifies programming by abstracting the underlying implementation and only exposing objects or actions the developer needs. 


[**Android**](https://developer.android.com) uses thousands of APIs to add different functionality in the application. It is a layered architecture. The API lies in the second layer (from the top) called as Application Framework layer. 

![Python](https://github.com/devu-62442/Extracting-Sensitive-API-Calls/blob/master/img/Architecture.png)

## Application Framework
Application framework layer is on top of native library layer. The application layer provides major Application programming interface (APIs) and higher-level services in the form of java classes. The application developers are allowed to access all the APIs framework for the core programs that make simpler the reuse of APIs components. These APIs are open to everybody to create android applications. There is different type of application components. Each type has a different lifecycle and purpose that describes how the component will be created and destroyed.
</br>

## Sensitive API
There is no definite defination for Sensitive APIs. Sensitive API's are the API's which handles the sensitive information in Android Devices. Now the sensitive information can be personal information rendering, it can be reading of databases, it can be sensing and receiving sms etc. 

In this tool the Sensitive API's are the set of APIs which are used to access ```Sensitive Resources``` on the Android Device. Sensitive Resources such as Devce ID of the Application, Location of the user, getting the information about Network Type.

There are 10 API classes used as Sensitive API classes. All these API classes will have different API methods which are used to detect the malicious behaviour in an Application.

E.g.-
- Landroid/telephony/TelephonyManager;->listen(Landroid/telephony/PhoneStateListener; I)V
- Landroid/telephony/TelephonyManager;->getNetworkType()I
- Landroid/net/ConnectivityManager;->getActiveNetworkInfo()Landroid/net/NetworkInfo;
- Landroid/content/pm/PackageManager;->isSafeMode()Z
    
In the above examples ```TelephonyManager, ConnectivityManager, PackageManager``` are the API classes and ```listen(), getNetworkType(), getActiveNetworkInfo(), isSafeMode()``` are the API Methods.

The Tool uses the following Sensitive APIs Classes -

![SensitiveAPIList](https://github.com/devu-62442/Extracting-Sensitive-API-Calls/blob/master/img/Screenshot%202019-10-22%20at%207.31.00%20PM.png)

These classes are used to give the list of all Sensitive API calls as an output.

## Working
Written in python ![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6e6574776f726b782e737667-2.svg). 
</br>
Every Application ```.apk``` is having a set of ```SENSITIVE APIs```.

The tool follows the following steps :-

#### Step #1. Use Androguard to create a callgraph :
```gradle
androguard cg 'Application Name'
```
<img align='right' height='200' src='https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/Screenshot%202019-10-20%20at%2010.31.34%20PM.png' />

</br>
A callgraph.gml is created using the above command in the same folder where application is placed.

#### Step #2. Clone and Download the code as github says - ![GitHub](https://github.com/devu-62442/Static_Malware_Family_Classifier_based_on_Graph_Comparison/blob/master/img/git.svg)

#### Step #3. Use the below command in the command-prompt to run the program ```Sensitive_API.py```

```gradle
python3 Sensitive_API.py -p [Path of your GML (Callgraph) Application] -g [Name of the GML (Callgraph)]
```
<img height=150 src="https://github.com/devu-62442/Extracting-Sensitive-API-Calls/blob/master/img/Screenshot%202019-10-22%20at%209.07.56%20PM.png" align="center" hspace="1" vspace="1">

#### Step #3. Output
The code will give you the set of the ```Sensitive APIs``` of that particular Android Malware Application-
</br>
<img height=300 src="https://github.com/devu-62442/Extracting-Sensitive-API-Calls/blob/master/img/Screenshot%202019-10-22%20at%208.02.33%20PM.png" align="center" hspace="1" vspace="1">


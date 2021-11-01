# News Classifier

#### IIITH Capstone project *( By Krishna Chaitanya and Ranjit Kumar )*

### PROJECT SCOPE
Classify News Articles into categories - With information overload today users are inundated with news articles of all topics, even the ones which may not be relevant to users. So, a system which can classify incoming news articles and appropriately tag the corresponding category is required 
Developing a system as required involves all the following stages of Machine Learning Project Life Cycle – 
1.	Data Ingestion 
2.	Data Preparation 
3.	Data segregation & Model Training 
4.	Model Deployment 
5.	Model Prediction 


### 	ENVIRONMENT
Prepare the system with all the necessary software for the development, testing and deployment. 
#### 	Pre - Requisites
We must ensure the following requirements are available and installed:
|	| Software |	Remarks |
| ------------- | ------------- | ------------- |
| language	| Python, HTML&CSS	 | To write necessary code | 
| ------------- | ------------- | ------------- |
| data store	| MongoDB/MySQL	 | To store the data |
| ------------- | ------------- | ------------- |
| IDE	| PyCharm / Visual code, jupyter notebook	 | To enable faster coding | 
| ------------- | ------------- | ------------- |
| Packages/API	| Kafka, Flask, PySpark, sklearn,  BeautifulSoup, Docker, Git	 | Software packages and APIs required for development |
| ------------- | ------------- | ------------- |


| Operating System	| Windows/Ubuntu |	
| ------------- | ------------- |
| Hardware	| RAM	Minimum:8gb	|
|            | Recommended:16gb |	
| ------------- | ------------- |
| HDD	| Minimum:20gb |
| ------------- | ------------- | ------------- |
	

#### Pre – Development Steps

•	Installing the softwares 

 - 	Download and install the corresponding executable packages for python, mongodb/mysql, pycharm/vs code, docker, git etc. .
  
 - 	Using python pip install flask, pyspark, flask, etc .
  
•	For Kafka 

 - 	Download and extract the corresponding archive file.
  
 - 	Configure kafka and zookeeper properties by editing the corresponding properties files located in kafka/config directory.
  
 - 	To start kafka server, start the zookeeper process first
  
•	For kafka-mongodb sink configuration:
  -	Download mongo-kafka-connect jar file and place it to kafka\libs folder
  -	Create new properties files containing parameters required to connect kafka broker and mongodb database and save the files to kafka\config folder. These properties files are passed as parameters to connect-standalone script file to establish the sink connection
•	For mongodb-spark connection:
  -	Download bson, mongodb driver core, mongo java driver, mongo spark connector jars and place them in a folder in the project working directory
  -	Provide the path of the above jar files location in the python code to load the data from “raw_data” from MongoDB into Spark

 ## Project execution
 #### to execute the data collection, model prediction and web app , find the instructions.txt contaning the commands and other instructions required


## References
•	Kafka windows installation:
  - https://towardsdatascience.com/running-zookeeper-kafka-on-windows-10-14fc70dcc771
  -	https://www.onlinetutorialspoint.com/kafka/install-apache-kafka-on-windows-10.html

•	Kafka mongo sink config:
  -	https://stackoverflow.com/questions/56880527/how-to-stream-data-from-kafka-to-mongodb-by-kafka-connector
  -	https://repo1.maven.org/maven2/org/mongodb/kafka/mongo-kafka-connect/
 
•	Mongo Spark configuration:
  -	https://docs.mongodb.com/spark-connector/current/python-api/
  -	https://www.mongodb.com/blog/post/getting-started-with-mongodb-pyspark-and-jupyter-notebook
  
•	TfidVectorizer
  -	https://stackoverflow.com/questions/44193154/notfittederror-tfidfvectorizer-vocabulary-wasnt-fitted/44194026
	


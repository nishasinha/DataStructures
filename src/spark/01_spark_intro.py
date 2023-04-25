"""
-----------------------------------
Spark installation steps:
----------------------------------------
1. Download tar, extract to a directory.
2. Set SPARK_HOME as the extracted directory.
export SPARK_HOME=/Users/nishakumari/personal/projects/spark/spark-3.3.1-bin-hadoop3
3. Update PATH variable in terminal profile and source it.
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
4. Start processes as needed.
spark-shell

start-master.sh
# see master UI on http://127.0.0.1:8080/

start-worker.sh -c 1 -m 512M spark://nishakumari-mac:7077
# ps aux | grep "java"

stop-all.sh

-----------------------------------
Spark Basic architecture:
-----------------------------------

Spark can run a code on distributed data in any storage.
Components:
1. Cluster manager
keeps account of physical machines available to run the code.
Spark standalone/ YARN/ Mesos

2. Driver
JVM process which keeps track of one spark application.
Sends code to executors.
Takes user inputs, writes to console.

3. Executors
JVM process on cluster nodes.
Runs user code on the data stored in the node.
Sends report to driver.

One spark cluster can run many spark applications.
One spark application would ahve one driver and multiple executors.


-----------------------------------
Spark API:
-----------------------------------
* Spark is written in scala.
Java, Python, R, Scala, SQL are supported languages and has their spark APIs for use.
Code from any language is compiled to one format.

* Core data structures:
Resilient Distributed data sets.
Dataframe
Dataset
SQL tables.

* Lazy evaluation:
The spark data structures are immutable.
We can only create new data structures from the existing ones by applying some function.
There are 2 types of functions:

1. Transformation
do not perform any task
specify the way the data needs to change like filter, sum, sort etc.
Can be narrow transformation:
    - which means that there is 1:1 mapping from partition in input data and output data.
    - no shuffling of data across executors, eg: filter.
Can be wide transformation:
    - which means that one input partition would be used in multiple output partitions.
    - data shuffling happens in cluster. Eg: sort, groupBy
    - by default spark outputs data into 200 shuffle partitions after any shuffle operation.
    - this can be changed by spark.conf.set("spark.sql.shuffle.partitions", "5")
    - this is how spark can modify physical data storage.


2. Actions
trigger the spark job execution.
eg: collect result, write to some output, show on console.
the job progress can be seen on Spark UI at http://localhost:4040

- This delay of execution till an action is asked by user is called Lazy evaluation.
- This helps spark to take user code from start to an action and optimize the query plan.

* Spark session
or spark context is the way of interacting to spark.
allows to invoke spark apis.
provides transformation and actions and returns the same data structure back.

"""

"""
Code examples

/data/flight-data/csv/2015-summary.csv
DEST_COUNTRY_NAME,ORIGIN_COUNTRY_NAME,count
United States,Romania,15
United States,Croatia,1
United States,Ireland,344

In Python, spark code would be :-
```
# read csv
flight_data = spark
    .read \
    .option("inferSchema", "true") \
    .option("header", "true") \
    .csv("/data/flight-data/csv/2015-summary.csv")

# get the max number of flights
from pyspark.sql.functions import max
flight_data \
    .select(max("count")) \
    .take(1)

# find the top five destination countries in the data
flight_data \
    .groupBy("DEST_COUNTRY_NAME") \
    .sum("count") \
    .withColumnRenamed("sum(count)", "destination_total") \
    .sort(desc("destination_total") \
    .limit(5) \
    .show()


# spark SQL code
flightData2015.createOrReplaceTempView("flight_data_2015")
```

maxSql = spark.sql("""
    SELECT DEST_COUNTRY_NAME, sum(count) as destination_total
    FROM flight_data_2015
    GROUP BY DEST_COUNTRY_NAME
    ORDER BY sum(count) DESC
    LIMIT 5
""")


"""



#  Adding custom JSON format output for robot framework 

Repo contains custom code changes to python robot library
which enables converting default xml output to json format.
We get both output.xml and output.json files as a result 
after running our robotframework based tests.

## Getting Started
These instructions will let you to clone and test this changes on your own environment.
I have tested this code on Ubuntu 16.04.1. I intend that you have already installed robotframework.
Below python modules are required to install :

```
pip3 install pymongo
pip3 install xmltodict
```
In order to clone repo:
```
git clone  -b json_output https://github.com/KamilBabayev/bell_robot.git
```

To enable json output writing, new python  json_writer.py named script has been added to
writer directory on top robot library directory.  create_json_output and write_json_todb named two
functions has been added to convert from xml to json and to write json data to MongoDB database.
After cloning repository, json_writer.py file must be copied from repo to python robot package location.

In my OS python3 robot package is located in /usr/local/lib/python3.5/dist-packages/robot directory.

__json_writer.py__ file must exists in __/usr/local/lib/python3.5/dist-packages/robot/writer__  directory.

Below lines were added to writer/_init_.py package initialication file to enable import of these functions
from other python files.

```diff
+from .json_writer import create_json_output
+from .json_writer import write_json_todb
```

To enable json formatting new functions must be imported and executed from the main __run.py__ file of robot library.
Import functions on top of file.

```diff
+from robot.writer import create_json_output, write_json_todb
```

Execute these functions with shown arguments. Lines 453,454,455 must be added just after original write_results()
method on line 452. After this changes, output.json file must be created at the same location with output.xml.

```diff
452                  writer.write_results(settings.get_rebot_settings())
+453                  xml_file, json_file = settings.output, settings.output_directory + "/output.json"
+454                  create_json_output(xml_file, json_file)
+455                  write_json_todb(json_file)
```

> MONGO_DBS named environment variable must be created. json_writer.py will take db instanse info from this variable.
> Example:   user1@localhost:~$ export MONGO_DBS='127.0.0.1:27017,127.0.0.2:27017'

Running test cases will create output.json file beside output.xml file.

```
user1@localhost:~$ pybot  -d logs   test1.robot
==============================================================================
Test1
==============================================================================
Test user defined keywork loaded from resource file                   | PASS |
------------------------------------------------------------------------------
Test1                                                                 | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
Output:  /home/user1/bell/tests/logs/output.xml
Log:     /home/user1/bell/tests/logs/log.html
Report:  /home/user1/bell/tests/logs/report.html
Json:    /home/user1/bell/tests/logs/output.json
Json:    Written successfully to mongoDB
```

JSON output seems like below:
```
user1@localhost:~$ cat  logs/output.json
{"@generator": "Robot 3.0.2 (Python 3.5.2 on linux)", "@generated": "20171107 20:22:50.048", "suite": {"@source": "/home/user1/bell/tests/test1.robot", "@name": "Test1", "@id": "s1", "test": {"@name": "Test user defined keywork loaded from resource file", "@id": "s1-t1", "kw": {"@library": "resource", "@name": "Print welcome message for", "arguments": {"arg": "Mister President"}, "kw": {"@library": "BuiltIn", "@name": "Log", "doc": "Logs the given message with the given level.", "arguments": {"arg": "Welcome ${USER}!"}, "msg": {"@level": "INFO", "@timestamp": "20171107 20:22:50.096", "#text": "Welcome Mister President!"}, "status": {"@status": "PASS", "@starttime": "20171107 20:22:50.095", "@endtime": "20171107 20:22:50.096"}}, "status": {"@status": "PASS", "@starttime": "20171107 20:22:50.095", "@endtime": "20171107 20:22:50.096"}}, "status": {"@status": "PASS", "@critical": "yes", "@starttime": "20171107 20:22:50.094", "@endtime": "20171107 20:22:50.096"}}, "status": {"@status": "PASS", "@starttime": "20171107 20:22:50.050", "@endtime": "20171107 20:22:50.097"}}, "statistics": {"total": {"stat": [{"@pass": "1", "@fail": "0", "#text": "Critical Tests"}, {"@pass": "1", "@fail": "0", "#text": "All Tests"}]}, "tag": null, "suite": {"stat": {"@pass": "1", "@name": "Test1", "@fail": "0", "@id": "s1", "#text": "Test1"}}}, "errors": null}user1@cmtest:~/bell/tests$
```

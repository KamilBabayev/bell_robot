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

Below lines were added to writer/_init_.py package initialication file to enable import of these functions
from other python files.

```
from .json_writer import create_json_output
from .json_writer import write_json_todb
```

To enable json formatting new functions must be imported and executed from the main run.py file of robot library.
Import functions on top of file.

```
from robot.writer import create_json_output, write_json_todb
```

Execute these functions with shown arguments. Lines 453,454,455 must be added just after original write_results()
method on line 452. After this changes, output.json file must be created at the same location with output.xml.

```diff
452                  writer.write_results(settings.get_rebot_settings())
+453                  xml_file, json_file = settings.output, settings.output_directory + "/output.json"
-454                  create_json_output(xml_file, json_file)
455                  write_json_todb(json_file)
```





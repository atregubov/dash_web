# Dash Web Demo Tool
Web user interface for DASH cognitive agent simulation framework. This web demo tool provide UI for running DASH 
experiments and result exploration. 

To start a web application run `server/dash_app.py`
To login in demo mode use username **_dev_**.

Sample data is preloaded in /data/lkml.json file (4 days of data). A longer data sample is available [here](https://drive.google.com/file/d/10Vxllf8bAlKau6lBrqgEWGdhX66DWBrd/view?usp=sharing) (182 days). 
To change a preloaded data file, run `server/dash_app.py` with the following parameter: `-data "../data/new_data_file.json"`. 
For example, `python dash_app.py -data "../data/full_lkml.json"`

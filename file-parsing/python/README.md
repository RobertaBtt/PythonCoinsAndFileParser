File Parsing
============

###### Requirements
 - to have installed python3.6.x
 

##### Prepare
 Install pip if you don't have it,  and then:
 
`cd file-parsing/python`

`python3 -m venv .env`

`source .env/bin/activate`

`pip3 install -r requirements.txt`
 
 ##### Run Test With Coverage
In a terminal, inside the **file-parsing/python**

`python3 -m pytest tests/ -v --cov command`

 ##### Run Test 
 In a terminal, inside the **file-parsing/python**
`python3 -m pytest tests/`

 
### Run App:
In a terminal, inside the **file-parsing/python** folder:
`python3 app.py`
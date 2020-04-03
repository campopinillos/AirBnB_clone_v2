![Holberton school logo](https://github.com/JDorangetree/AirBnB_clone_v2/blob/master/hbnb.png)
# AirBnB clone 2 Project

## Table of Contents
* [Description](#description)
* [File Structure](#file-structure)
* [Requirements](#requirements)
* [Quick Start](#quick-start)
* [Usage](#usage)
* [Bugs](#bugs)
* [Authors](#authors)

## Description
This is collaborative project made by Luz Adriana Ariza and Campo Elias Pinillos, students of Software Engineering at Holberton School. This repository contains the files for Holberton's **AirBnB clone project**. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).

**The Console**

Will help us to:

1. Create your data model
2. Manage (create, update, destroy, etc) objects via a console / command interpreter
3. Store and persist objects to a file (JSON file)

In this case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## File Structure

These are the files with the custom funtions and system calls, each one contains a brief description:



|   ***File***    |  ***Description***                   |
|---------------|---------------------------------------|
|  [`console.py`](./console.py)	|  Console file	|
|  [`models`](./models) |  Contains all the classes |
|  [`models/__init__`](./models/__init__.py) |  Connects with filestorage |
|  [`models/base_model`](./models/base_model.py) |  Base Model class |
|  [`models/user`](./models/user.py) |  User class |
|  [`models/state`](./models/state.py) |  State class |
|  [`models/city`](./models/city.py) |  City class |
|  [`models/place`](./models/place.py) |  Place class |
|  [`models/amenity`](./models/amenity.py) |  Amenity class |
|  [`models/review`](./models/review.py) |  Review class |
|  [`models/engine`](./models/engine) |  Contains File Storage engine |
|  [`models/engine/file_storage`](./models/engine/file_storage.py) |  File Storage module |
|  [`models/engine/db_storage`](./models/engine/db_storage.py) |  MySQL Storage module |
|  [`tests`](./tests) |  Prompt and getline file	|
|  [`AUTHORS`](./AUTHORS)	|  AUTHORS file|
|  [`README.md`](./README.md) | README.md file |

## Requirements
* All files will be interpreted/compiled on Ubuntu 14.04 LTS using python3
* Code should use the PEP 8 style (version 1.7 or more)
* Your code should use the PEP 8 style (version 1.7 or more)


## Quick Start
1. Install python
```
> sudo apt-get install python3
```
2. Clone repo
```
> git clone https://github.com/campopinillos/AirBnB_clone.git
```
3. Change directory to simple_shell
```
> cd AirBnB_clone/
``` 
4. Execute ./console.py
```
> ./console.py

(hbnb) 
```

## Usage

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`
```
(hbnb) quit
> 
```

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

(hbnb) help
```
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`


## Bugs
No known bugs. Please contact any of the authors if a bug appears.


## Authors
* **Julian David Naranjo** - [JDorangetree](https://github.com/JDorangetree) 

* **Campo Elias Pinillos** - [campopinillos](https://github.com/campopinillos)
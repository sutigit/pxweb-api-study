# PxWeb API study

## Table of content
- [Overview](#overview)
- [Introduction](#introduction)
- [Modules](#modules)

# Overview
This project is about studying the API endpoints within the PxWeb API Statistics ecosystem. Especially what the endpoints provide, which endpoints can be useful to your project, response object structures, automating tasks and packaging results.
More closely, this documentation will list the different processess and the software components related to each step. In the end of this documentation is an overview of related research to this project.

# Prerequisites
1. Knowledge of how to use PxWeb API's and their URL structures. See [here](https://pxdata.stat.fi/api1.html).
2. Jupyter notebook (optionaly: jupyter notebook as VScode plug-in)
3. Python 3
4. Optional: Virtual environment recommended

# Introduction
Each module serves a different purpose in the steps to examine and produce reusable data suited to your needs from a PxWeb API endpoint. Go through each module and inspect the purpose of it, to gain understanding of each step, and what the end goal is.
The modules are introduced and described in the Modules section below. The section includes a usage section for each module and also the files produced from that module. The files produced are to be used in the next step, to achieve the desired end goal of packaging insights into a resuable collection of data.
Read the Usage instructions here in README, but a more detailed step-by-step instruction is provided in the Jupyter notebooks markdown sections.


# Modules

## 1. `endpoint_study.ipynb`
### Overview
This module can examine the results of an PxWeb API endpoint call in each of it state. By state, I mean the different phases in which the endpoint URL will take form when we nest down the database structure. The first state of the endpoint ends with a versioning label: `v0`, `v1`, etc. The endpoint url is in its full state, when it ends with the suffix `.px`. 
In each state we can choose how we nest down the database structure or give new parameters how any intermediate of final state is called by changing slugs in the endpoint on the fly.

For example:

```
1st state: 'https://pxdata.stat.fi:443/PxWeb/api/v1/'
2nd state: 'https://pxdata.stat.fi:443/PxWeb/api/v1/fi/'
3rd state: 'https://pxdata.stat.fi:443/PxWeb/api/v1/fi/Kuntien_avainluvut/'
4th state: 'https://pxdata.stat.fi:443/PxWeb/api/v1/fi/Kuntien_avainluvut/uusin/'
Full state: 'https://pxdata.stat.fi:443/PxWeb/api/v1/fi/Kuntien_avainluvut/uusin/142h.px/'
```

### Usage
1. Initiate Endpoint instance and give it the URL to be inspected
2. View the results of each state.
3. Choose what to do with the results   

### Output

## 2. `endpoint_values_inspector.ipynb`
### Overview
### Usage
### Output

## 3. `endpoint_values_list_generator.ipynb`
### Overview
### Usage
### Output

## 4. `endpoint_values_list_testing.ipynb`
### Overview
### Usage
### Output


# Classes

## `Endpoint`
### Overview
### Methods

## `File`
### Overview
### Methods

## `PostBody`
### Overview
### Methods

## `PxWeb`
### Overview
### Methods


# Current Research
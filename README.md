# sample-function-app

## Overview
This GitHub repo contains a sample Azure Function App with a function name "SampleFunction" written in Python. The aim of the SampleFunction is to test running pg_dump command using os.system(). This function app has been tested locally and the pg_dump command is working without issues. However, once deployed this function app, we observe that running the pg_dump command using os.system() does not work. 

## How to run
To run it locally, simply clone the repo. Navigate to the sample-function-app directory and run ```func start``` command. Once the function app has been started locally, on a browser, go to ```http://localhost:7071/api/SampleFunction```. Observe the logs being printed out in the terminal.

To test this function app when being hosted on Azure Function, this function app needs to be deployed to Azure Function then use Code + Test menu to run the function. 

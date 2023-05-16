# Simple Flask app with Docker

## Install

This is a simple api to sum to numbers withing the query.

Ports: 80:5000 (host/docker)


To install the api run  

```py
docker-compose up -d 
```

In the folder where the docker-compose.yaml is located


<p>Parameters<br>
            ----------<br>

```py
GET: get two numbers through query parameters.
        Example: curl -X GET "localhost/sum?num1=1&num2=2"
POST: get two numbers through a json file.
        Example: curl -X POST -H "Content-type: application/json" -d "{\"num1\" : 1, \"num2\" : 2}" "localhost/sum"
        
Returns
-------
JSON response with the result
            
```
</p>


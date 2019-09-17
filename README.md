# Flask-Restful-API-Calculator
FLASK RESTFUL API FOR ARITHMATIC OPERATIONS

This rest-api takes two values(Binary Data) "x" and "y" as an input and Performs an arithmatic operation on them. 
The arithmatic operation include addition, subtraction, multiplication, and division.
Input is given in a dictionary format(Json) from the Postman -in post method at body section, and output of each operation can be seen in the response 
of Postman(Body Section).

Example of input:

  {
  
    "x":20,
    
    "y":25
    
  }

# Links to post values in json object from postman

1. http://127.0.0.1:5000/add
2. http://127.0.0.1:5000/sub
3. http://127.0.0.1:5000/mul
4. http://127.0.0.1:5000/div

# Stage 1 Backend- Number Classification API

## Task Description

Create an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Requirements

Programming Language/Framework: Python - (FastAPI)
Deployment: The API must be deployed to a publicly accessible endpoint: Used <Render.com>
CORS Handling: Ensure the API handles Cross-Origin Resource Sharing (CORS) appropriately.
Response Format: All responses must be in JSON format.
API Specification
Endpoint: ```GET** <your-domain.com>/api/classify-number?number=371```
Required JSON Response Format (200 OK):

```json
    {
        "number": 371,
        "is_prime": false,
        "is_perfect": false,
        "properties": ["armstrong", "odd"],
        "digit_sum": 11,  // sum of its digits
        "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
}
```

Required JSON Response Format (400 Bad Request)

```json

    {
        "number": "alphabet",
        "error": true
    }
```

## Running the project Locally

- Create a python virtual environment

```bash
    python -m venv
```

- Install the necessary requirements

```bash
    pip install -r requirements.txt
    pip install pydantic
```

- Run the FastAPI Application
You can run the FastAPI application using Uvicorn:

    ```uvicorn main:app --reload```

- Access the API
Once the server is running, you can access the API at <http://127.0.0.1:8000/api/classify-number?number=5>.
You can also view the interactive API documentation at <http://127.0.0.1:8000/docs> or <http://127.0.0.1:8000/redoc>.

- Test the API
You can test the API using curl, httpie, or any other HTTP client.

```bash
    curl -X GET "http://127.0.0.1:8000/api/classify-number?number=5" -H "accept: application/json"
```

The response should look like this:

Endpoint: GET** ```<your-url>```
Required JSON Response Format (200 OK):

```json
   {
        "number": 5,
        "is_prime": true,
        "is_perfect": false,
        "properties": [
            "odd"
        ],
        "digit_sum": 5,
        "fun_fact": "5 is also the number of Platonic solids."
    }
```

## Backlink

One backlink related to your chosen programming language/stack:

<https://hng.tech/hire/python-developers>

## Functionality

- Accepts GET requests with a number parameter.
- Returns JSON in the specified format.
- Accepts all valid integers as the only possible inputs
- Provides appropriate HTTP status codes.

## Code Quality

- Organized code structure.
- Basic error handling and input validation.
- Avoids hardcoded values.
- Documentation
- Complete README.
- Deployment
- Publicly accessible and stable API.
- Fast response time (< 500ms).

## Additional Note

Use the math type from the Numbers API to get the fun fact.
The possible combinations for the properties field:

**["armstrong", "odd"] - if the number is both an Armstrong number and odd**
**["armstrong", “even”] - if the number is an Armstrong number and even**
**["odd"] - if the number is not an Armstrong number but is odd**
**[”even”] - if the number is not an Armstrong number but is even**

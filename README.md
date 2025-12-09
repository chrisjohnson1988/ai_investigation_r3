# ai_investigation_r1
This is a dummy repo. I am going to put something in here for AI to look at

## Flask Hello World Application

A simple Python Flask REST API that returns a "Hello World" response.

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the Flask server:
```bash
python app.py
```

The server will start on `http://localhost:5000`

### API Endpoints

- **GET /hello** - Returns a "Hello World" JSON response

Example:
```bash
curl http://localhost:5000/hello
```

Response:
```json
{
  "message": "Hello World"
}
```

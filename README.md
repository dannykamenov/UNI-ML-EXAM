# My ML App - Daniel Kamenov F97131

## Steps to create Docker image and run the container

1.  **Build the Docker image:**

    ```sh
    docker build -t UNI-ML-EXAM .
    ```

2.  **Run the Docker container:**

    ```sh
    docker run -p 80:80 UNI-ML-EXAM
    ```

3.  **Access the API:** - The API will be accessible at `http://localhost:80` - Use Postman to send a POST request to `http://localhost:80/predict` with the following JSON body:
    ```json
    {
        "data": [
            [5.1, 3.5, 1.4, 0.2],
            [6.7, 3.1, 4.7, 1.5],
            [5.9, 3.0, 5.1, 1.8]
        ]
    }
    ```

## Running Tests

1. **Install pytest:**

   ```sh
   pip install pytest
   ```

2. **Run the tests:**
   ```sh
   pytest tests/
   ```

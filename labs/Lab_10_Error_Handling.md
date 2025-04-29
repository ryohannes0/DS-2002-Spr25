# Lab 10 - Python Error Handling

First read [this page](https://docs.python.org/3/library/exceptions.html) from Python documentation.

The basics:

- The `try` block lets you test a block of code for errors.
- The `except` block lets you handle the error.
- The `else` block lets you execute code when there is no error.
- The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

When an error (aka exception) occurs, Python normally stops and generates an error message.

These exceptions can be handled using `try`/`except` statements:

```
try:
  print(x)
except:
  print("An exception occurred")
```

Notice, however, that while python detects the exception, the developer has simply programmed a simple message instead of any detail about WHY the exception occurred.

To improve upon this, a generic exception handler can pull out such detail. Here the exception error message is captured into a variable `e` that can be printed and parsed.

```
try:
  sum = "word" + 7
except Exception as e:
  print(e)
```
```
can only concatenate str (not "int") to str
```
The error indicates that strings and ints cannot be added or concatenated.

<br>

## Setup
- Start up any IDE of your choosing, this should work fine for Google Cloud Shell, VS Code, Google Collab, your CLI, whatever you are most comfortable with.
- Create a Gist, and format it as such:
```
Part 1:
<paste code here>

Part 2:
<type your response to the question here>

Part 3:
<paste your code here>
```

<br>

## Why Are We Learning This?
Beyond just a program that you may write in Python for a class, or bad input you may expect a user to provide, there 
are all kinds of instances where it will be important for you to handle errors and exceptions when it comes to 
your data pipelines and data science systems. For the sake of this lab, I encourage you to read through the examples 
and complete the three (3) simple exercises below.

### Data Pipeline Examples

1. **Data Ingestion Failures:**
    - `Scenario`: A pipeline pulls data from an external API. The API might be temporarily unavailable due to network issues, server maintenance, or rate limiting.
    - `Error Handling`: Implement retry mechanisms with exponential backoff. Log the failure with details (timestamp, API endpoint, error message). Potentially send alerts to operations teams. Have a "dead letter queue" to store failed records for later investigation and reprocessing.

2. **Data Format or Schema Mismatches:**
    - `Scenario`: An upstream system changes the format or schema of the data it produces without notifying the downstream pipeline. This could lead to parsing errors.
    - `Error Handling`: Implement schema validation steps in the pipeline. If a mismatch occurs, quarantine the invalid data, log the schema violation, and potentially trigger an alert for the data engineering team to investigate and update the pipeline.

3. **Data Transformation Errors:**
    - `Scenario`: During data cleaning or transformation steps (e.g., converting data types, applying business logic), invalid or unexpected data values might cause errors in the transformation logic (e.g., trying to convert a non-numeric string to an integer).
    - `Error Handling`: Implement robust data validation within the transformation steps. Use try-except blocks to catch potential errors. Log the problematic data records and the specific transformation error. Depending on the severity, either skip the invalid record (with proper logging) or halt the pipeline and trigger an alert.

4. **Database Connection Issues:**
    - `Scenario`: A pipeline needs to write processed data to a database. The database server might be down, temporarily overloaded, or there might be network connectivity problems.
    - `Error Handling`: Implement retry mechanisms for database connections and write operations. Use connection pooling to manage connections efficiently. Log connection errors and trigger alerts if the issue persists. Implement mechanisms to buffer data temporarily if the database is unavailable to prevent data loss.

5. **Resource Exhaustion:**
    - `Scenario`: A pipeline running on a cloud platform might temporarily exceed resource limits (CPU, memory, disk space), leading to process crashes.
    - `Error Handling`: Implement monitoring of resource utilization. Configure auto-scaling if possible to handle spikes in demand. Implement mechanisms to gracefully handle resource exhaustion errors, such as releasing resources and retrying the operation later.

### System Architecture Examples

1. **Service-to-Service Communication Failures:**
    - `Scenario`: In a microservices architecture, services communicate with each other over a network. Network issues, service unavailability, or incorrect API calls can lead to communication failures.
    - `Error Handling`: Implement circuit breaker patterns to prevent cascading failures. Use retry mechanisms with appropriate backoff strategies. Implement timeouts to prevent indefinite blocking. Log communication errors with relevant details. Implement robust API design with clear error codes and messages.

2. **Message Queue Issues:**
    - `Scenario`: Systems relying on message queues (like Kafka, RabbitMQ) might encounter issues such as the queue being down, message corruption, or failure to process messages by consumers.
    - `Error Handling`: Implement dead letter queues for messages that cannot be processed. Implement monitoring of queue health and consumer lag. Ensure consumers are idempotent to handle potential message redelivery. Implement mechanisms for manual inspection and reprocessing of failed messages.

3. **External Service Dependencies:**
    - `Scenario`: A system might depend on external services (e.g., payment gateways, mapping services). These services might experience downtime or changes in their APIs.
    - `Error Handling`: Implement fallback mechanisms or alternative providers if critical external services are unavailable. Implement health checks for external dependencies. Use appropriate timeouts and error handling for API calls.

4. **Configuration Errors:**
    - `Scenario`: Incorrect configuration settings (e.g., database credentials, API keys, network addresses) can prevent components from functioning correctly.
    - `Error Handling`: Implement robust configuration management with validation checks. Log configuration loading and any errors encountered. Implement mechanisms to revert to default or previous working configurations in case of critical errors.

5. **Security Breaches or Authentication/Authorization Failures:**
    - `Scenario`: Attempts to access resources without proper authorization or during a security breach need to be handled securely.
    - `Error Handling`: Implement robust authentication and authorization mechanisms. Log all security-related events and failures. Implement rate limiting and intrusion detection systems. Provide informative but not overly revealing error messages to prevent information leakage.

<br>

## 1. Error Handling - Built-in

Review the code below:

```
def throw_me_an_error():
  val1 = 14
  val2 = 0
  return val1 / val2

throw_me_an_error()
```
This function is designed to deliberately throw an error.

Create a new version of the function but add `try` and `except` statements correctly. Your exception should print out the type of error this function created. There are a couple of different ways you could do this.

<br>

## 2. Error Handling - `finally`

Look at the error handling within this more complex example:

```
def write_data_to_file(data, filename):
  try:
    with open(filename, 'w', encoding='utf-8') as file:
      file.write(data)
  except FileNotFoundError as e:
    print(f"Error: File {filename} not found.")
  except PermissionError as e:
    print(f"Error: Permission denied to write to {filename}.")
  finally:
    if 'file' in locals():  # Check if 'file' variable exists (was opened)
      file.close()  # Close the file if it was opened

# Example usage
data = "This is some data to write to the file."
filename = "my_data.txt"
write_data_to_file(data, filename)
```
Explain the function of the `finally` block in this snippet. What purpose does it serve?

<br>

## 3. Error Handling - Imported Library

Look at this snippet of code, which triggers a specific error from the `json` library:

```
import json

# Invalid JSON data
data = "{invalid_json_key: 'value'}"

try:
  # Attempt to load the JSON data
  json.loads(data)
except json.JSONDecodeError as e:
  # Print the JSON import error
  print(f"JSON import error: {e}")
```
Rewrite this snippet so that it works correctly and does not trigger an exception.

<br>

## 4. Submit your work
Submit the URL to your Gist in Canvas for grading.

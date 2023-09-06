# Document Analyzer Python Script

This Python script is designed to analyze CSV documents and determine the most common words in them. It provides the flexibility to specify a custom path to the documents or use a default path. The script utilizes popular libraries like pandas, os, glob, and collections to perform the analysis.

## Prerequisites

Before using this script, ensure you have the following prerequisites installed:

- Python (version 3.x)
- pandas
- pytimedinput
- inputimeout

You can install the required libraries using pip:

```bash
pip install pandas pytimedinput inputimeout
```

## Usage

1. Clone or download this repository to your local machine.

2. Navigate to the directory where the script is located.

3. Open your terminal or command prompt.

4. Run the script using the following command:

```bash
python document_analyzer.py
```

## Configuration

- `TIMEOUT`: The number of seconds allowed for user input during path selection.

- `docsPath`: The default path to the documents. You can change this to your preferred default directory.

## How It Works

1. The script starts by importing the necessary libraries and setting up signal handling for timeouts.

2. It prompts the user to enter the path to the documents within a specific time frame (defined by `TIMEOUT`).

3. If a valid path is provided, it checks if the path exists and switches the working directory to the specified path.

4. If the user does not provide a path or provides an invalid path, the script continues with the default `docsPath`.

5. It then searches for CSV files in the specified directory and sorts them by creation time in descending order.

6. The script iterates through the top 4 most recently created CSV files (you can adjust this number) and counts the occurrence of words in each document.

7. The most common words across all documents are collected and displayed, along with their frequencies.

## Example Output

Here is an example of what the script's output might look like:

```plaintext
You have 30 seconds to enter the path to documents.
Path exists.
Entered path is: /path/to/your/documents
[('word1', 123), ('word2', 98), ('word3', 76), ...]
Total unique words: 543
```

The script will show you the most common words found in the CSV documents and the total number of unique words.

## How to use it step-by-step:

**Step 1: Set the Application Name**

Before you begin, make sure to set the `appName` variable in the Makefile to the name of your Python demo application.

```bash
export appName=python_demo_app
```

Replace `'python_demo_app'` with your desired application name.

**Step 2: Build the Docker Image**

To build the Docker image for your application, open your terminal and navigate to the directory containing your project's files, including the Makefile. Then, run the following command:

```bash
make build
```

This command will build the Docker image using the Dockerfile located in the current directory and tag it with the specified image name.

**Step 3: Push the Docker Image to a Repository**

If you want to push the Docker image to a container registry (e.g., Docker Hub), use the following command:

```bash
make push
```

This will push the Docker image to the specified repository with the tag "latest."

**Step 4: Compose and Convert Docker Compose File (Optional)**

If you have a Docker Compose file and want to use it to create Kubernetes manifests, run the following command:

```bash
make compose
```

This command will start your application using Docker Compose and then use Kompose to convert the Docker Compose file into Kubernetes manifests.

**Step 5: Deploy the Application to Kubernetes**

To deploy your application to Kubernetes, run the following command:

```bash
make deploy
```

This command will apply the Kubernetes manifests located in the "manifests" directory to your Kubernetes cluster. Make sure your `kubectl` configuration is set up correctly.

**Step 6: Destroy the Deployed Application (Optional)**

If you want to delete the deployed application and its resources from your Kubernetes cluster, run the following command:

```bash
make destroy
```

This command will delete the resources defined in the Kubernetes manifests from your cluster.

**Step 7: Clean Up Docker Images (Optional)**

To clean up Docker images on your local machine and free up disk space, you can use the following command:

```bash
make clean
```

This command will remove unused Docker images.

With these steps, you can easily build, push, deploy, destroy, and clean your Python demo application using the provided Makefile and Docker/Kubernetes tools. Remember to adjust the `appName` variable and other configurations as needed for your specific project.

## Notes

- Make sure the CSV documents you want to analyze are in the specified directory.

- You can adjust the number of documents to analyze by changing the `doc < 4` condition.

- If you want to change the default path, update the `docsPath` variable to your desired directory.

- This script assumes that the CSV documents contain textual data, and it counts words based on spaces and punctuation. You can further customize the word extraction process if needed.

- You should have installed next tool/apps:
  - docker
  - docker-compose
  - kubectl
  - minikube (additionaly)
  - make
  - python
  - pip
Feel free to customize and use this script for your specific document analysis needs.
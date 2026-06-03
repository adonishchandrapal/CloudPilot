# ☁️ CloudPilot

CloudPilot is a Cloud Infrastructure Recommendation System built using Python and Streamlit.

It helps users choose the right cloud architecture based on their application type, expected traffic, and cloud provider.

## Features

* Multi-Cloud Support

  * AWS
  * Microsoft Azure
  * Google Cloud

* Application Recommendations

  * Chat Applications
  * E-commerce Platforms
  * Blogs
  * Video Streaming Platforms

* Cost Estimation

* Scale Classification

  * Small
  * Medium
  * Large

* Architecture Summary Generation

## Technologies Used

* Python
* Streamlit
* Git
* GitHub

## Project Structure

CloudPilot/

├── app.py

├── web_app.py

├── cloud_recommender.py

├── requirements.txt

├── README.md

└── history.txt

## How to Run

1. Clone the repository

git clone https://github.com/adonishchandrapal/CloudPilot.git

2. Move into the project directory

cd CloudPilot

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run web_app.py


## 🚀 Live Demo

[Open CloudPilot](https://cloudpilot-ivftzrcdbfnc6qmsoz4fk8.streamlit.app/)


## Example Output

Cloud Provider: Google Cloud

Frontend: Cloud CDN

Backend: Cloud Run

Database: Firestore

Estimated Cost: 45$/month

Scale: Medium

## Docker Support

Build Docker Image:

```bash
docker build -t cloudpilot .
```

Run Docker Container:

```bash
docker run -p 8501:8501 cloudpilot
```

## Future Improvements

* Terraform Generator
* Docker Support
* Real Cloud Pricing APIs
* AI Application Recommendations
* Kubernetes Recommendations

## Author

Adonish Chandrapal
Aspiring Cloud Engineer

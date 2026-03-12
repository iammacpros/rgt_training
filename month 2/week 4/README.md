# Churn Prediction API

A production-ready FastAPI application for predicting customer churn using a pre-trained scikit-learn model. This project supports both single prediction requests and batch processing via CSV uploads, fully containerized with Docker.

## 🚀 Features

- **Single Prediction**: Predict churn probability for an individual customer via a JSON request.
- **Batch Prediction**: Upload a CSV file and receive a downloadable CSV with churn predictions and probabilities.
- **Auto-Documentation**: Integrated Swagger (OpenAPI) and ReDoc for easy API testing and exploration.
- **Containerized**: Ready for deployment using Docker and Docker Compose.

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Machine Learning**: [scikit-learn](https://scikit-learn.org/), [joblib](https://joblib.readthedocs.io/)
- **Data Handling**: [pandas](https://pandas.pydata.org/), [Pydantic](https://docs.pydantic.dev/)
- **Containerization**: [Docker](https://www.docker.com/)

## 📋 Prerequisites

- Python 3.9+
- Docker & Docker Compose (optional, for containerized execution)

## 🔧 Installation & Setup

### Local Setup
1. Clone the repository and navigate to the project directory:
   ```bash
   cd "month 2/week 4"
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   fastapi dev main.py
   ```
   The API will be available at `http://localhost:8000`.

### Running with Docker
1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```
   The API will be available at `http://localhost:8000`.

## 📖 API Documentation

Once the server is running, you can access the interactive documentation:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Endpoints

#### `POST /predict`
Predicts churn for a single customer.
- **Request Body**: JSON object containing customer features (gender, tenure, MonthlyCharges, etc.).
- **Response**: JSON object with `prediction` ("Yes"/"No") and `probability`.

#### `POST /predict/batch`
Processes multiple customers via a CSV file.
- **Request**: Multipart/form-data with a `.csv` file.
- **Response**: A downloadable CSV file containing the original data plus `prediction` and `probability` columns.

## 📁 Project Structure

- `main.py`: Entry point for the FastAPI application.
- `predict.py`: Core logic for loading the model and making predictions.
- `models.py`: Pydantic schemas for request and response validation.
- `model.pkl`: Pre-trained machine learning model.
- `Dockerfile` & `docker-compose.yml`: Containerization configuration.
- `requirements.txt`: Python dependencies.

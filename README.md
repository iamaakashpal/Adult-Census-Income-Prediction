# Adult-Census-Income-Prediction

# Machine Learning Project Directory Structure

    Machine Learning Project/
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── venv
    ├── requirements.txt
    ├── app.py
    ├── Dockerfile
    ├── .dockerignore
    ├── .github/workflow
            ├── main.yaml  (Deployment related code i.e. heruko, aws and azure)
    ├── setup.py
    ├── census
            ├── __init__.py
            ├── exception
                    ├── __init__.py
            ├── logger
                    ├── __init__.py
            ├── pipeline
                    ├── pipeline.py
                    ├── __init__.py
            ├── component
                    ├── data_ingestion.py
                    ├── data_validation.py
                    ├── data_transformation.py
                    ├── model_training.py
                    ├── model_evaluation.py
                    ├── model_pusher.py
                    ├── __init__.py
            ├── config
                    ├── __init__.py
            ├── entity
                    ├── config_entity.py
                    ├── artifact_entity.py
                    ├── __init__.py
            ├── constant
                    ├── __init__.py
            ├── utils
                    ├── __init__.py
    ├── notebook
            ├── testing.ipynb
    ├── config
            ├── config.yaml
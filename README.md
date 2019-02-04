# risks-api

This is the backend application, created using DJANGO Rest Framework, that serves the [Risks Frontend App](https://github.com/catalinaperalta/risks-front). The backend application returns information about the Risks and RiskFields models. There is another incomplete Insurer model, which in the future can be linked to the Risks model. 

## Important project components:

* Entity Relationship Diagram - the diagram only depicts the Risk section of the application. The file is in the main project directory and is called [ER_RisksApp.png](https://github.com/catalinaperalta/risks-api/blob/master/ER_RisksApp.png).
* The ORM classes of the tables implemented can be found in the api/ folder in [models.py](https://github.com/catalinaperalta/risks-api/blob/master/api/models.py).
* Tests can be found in the api/ folder in [tests.py](https://github.com/catalinaperalta/risks-api/blob/master/api/tests.py)
* The [quiz.py](https://github.com/catalinaperalta/risks-api/blob/master/quiz.py) file that was used to find the project description can be found in the main directory. 

## Getting Started with risks-api

In order to install and run this application please follow these steps:

Clone the repository

Create a virtual environment with ```python 3.6.7```

Install the pip modules needed by the project

```
pip install -r requirements.txt
```
Create your local database by running

```
python manage.py makemigrations
```
then perform the migration
```
python manage.py migrate
```

You can now run the application with the following command
```
python manage.py runserver
```

That's it! 

## API Endpoints

Risks API Endpoint to return a list of all current Risks: 
```
/api/risks
```

Risks API Endpoing to return a single Risk:
```
/api/risks/<id>
```

Risks API Endpoint to return a single Risk Field:
```
/api/riskfields/?search=<risk_field name>
```

Risks API Endpoint to return all additional Risk Fields:
```
/api/riskfields
```

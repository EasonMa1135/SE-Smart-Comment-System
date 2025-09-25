# Local operation instructions

## Required environment

1. Node.js
2. npm (cnpm)
3. python3.x
4. conda
5. MySQL80

## File structure

1. backend is the backend program folder
2. database is the database table creation script folder
3. frontend is the frontend folder

## Technology Stack

1. Database: MySQL
1. Backend: Flask framework + SQLAlchemy ORM
1. Frontend: Vue framework + Vuex state management + Vuetify UI component library + Vite build tool + Axios HTTP client + ECharts visualization library

## Running steps

1. Database Creation

* In MySQL Workbench 8.0 CE, use the password to log in as needed. You will need to modify the username and password in ./backend/config.py later.
* Execute the ./database/create.sql script.
2. Backend Startup
* Run `cd backend` to navigate to the backend folder.
* Modify the database username and password in config.py as needed.
* Run `conda create --name bs_flask python=3.10.13`. You can change the Python version as needed.
* Restart the terminal and run `conda activate bs_flask` to open the virtual environment.
* Run `pip3 install -r requirements.txt` to download the required libraries.
* Run `python app.py` to run the backend application.
3. Frontend Startup
* Run `cd frontend` to navigate to the frontend folder.
* `npm install` to install the required libraries.
* `npm run dev` can be run locally on the host machine at <http://localhost:8888> Visit this website
* Alternatively, use `npm run build` and `npm run preview` to view the production build. Follow the prompts in the terminal output to determine the port to access this website.
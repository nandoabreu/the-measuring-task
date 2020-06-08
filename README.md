# A Python Task

This task was developed for a Python Dev position I applied for a while ago. It runs a Flask web server to list some data and log request os that page. Jinja handles the templates.

## Development

This project was developed inside a customised slim debian docker container with Python 3.6 and virtualenv.

## Dependencies

Python 3.6 (tested OK on 3.7 / must work on any 3+)  
Python pip 20.1.1 (tested OK on 19.2.3 and 20.0.2)  
\+ requirements.txt

## Instructions

**Install project's requirements:**

    $ pip install -r requirements.txt

**Check if 'task/data/config.py' exists. If doesn't, copy from 'task/data/config.py.tpl':**

    $ cp -i task/data/config.py.tpl task/data/config.py

**Structure a SQLite3 database and transfer data from csv:**  
&#x1F538; *SQLite database will be replaced, if exists.*

    $ python task/sqlite3_prepare_and_transfer_data.py

**Serve the database data in a web application:**  
&#x1F539; *Run the next line and browse http on port 8080 (default).*

    $ python task/web_application.py 8080

**Browse http at the used port to view data. The second URL will show logs:**  
&#x1F539; [http://localhost:8080/list](http://localhost:8080/list)  
&#x1F539; [http://localhost:8080/log](http://localhost:8080/log)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  


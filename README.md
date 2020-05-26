# "SST" Task

![Task Logo](docs/static/64x64.png "Task Logo")

This task was developed for the Python Backend Dev position I've applied for in May/2020. Thank you for verifying this solution.

## Development

This project was developed inside a customized slim debian docker container with Python 3.6 and virtualenv.

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
&#x1F539; http://localhost:8080/list  
&#x1F539; http://localhost:8080/log

## Info and justification

The task is straight forward and should take a little time for most people, as described. Once I already had the necessary basic environment at my disposal, I took more time to do some testing and a little makeup.

The chosen database for the task is SQLite because it's simple and light enough to be embedded and should not create trouble to setup and run. I also prefer SQLite for fewer data that could be embedded and processed into simple statistics and graphics. The CSV is also normalized enough to be in a relational DB.

Flask is being used to serve the web pages because it is great and because the job description mentions it. Also, I worked with PHP+Smarty for a long time and I got used to (and trust) templates, and Jinja is a fast and simple option.

The http responses (html pages) should answer fine to a desktop browser and a landscaped mobile phone. They were tested in Chrome (Ubuntu and Android), in Safari (iPad), Edge (MS Windows) and Lynx (Bash). A second web page is available with the logs, but naturally the sqlite3 client can be used to check the database in 'task/data/task_data.sqlite3.db'.

I hope this solution is somehow you expect. Bis bald!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
"Task Logo" is a free icon from [Icon Shop](https://freeiconshop.com/icon/task-complete-icon-flat/), as described by the site's [license](https://freeiconshop.com/icon-shop-license/).

## Virtualenv basics, if needed

    $ virtualenv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    $ python task/sqlite3_prepare_and_transfer_data.py
    $ python task/web_application.py 8080


## [Flask Portfolio Starter](https://nighthawkcodingsociety.com/projectsearch/details/Flask%20Portfolio%20Starter)
Runtime link: https://portfolio.nighthawkcodingsociety.com/


##Intermission
[Github Repository](https://github.com/samayass/flask_portfolio)   

[Scrum Board](https://github.com/samayass/flask_portfolio/projects/1)  

[Github Contributors](https://github.com/samayass/flask_portfolio/graphs/contributors)

[Samaya and Divya Pair Jorunal ](https://docs.google.com/document/d/1p35PYstj0w8IxgT5jy2UJo5Z-XcBAF0ucNkWZ-UMmBA/edit?usp=sharing)  

[Krish and Kamryn Pair Jorunal](https://docs.google.com/document/d/1Gl6Cy5CF-b2_k-oHFSUnkzDc9XEHm89nCQ6-IjJqATQ/edit?usp=sharing)


|   Names 	|  Github ID 	                                     |   Commits     	                                                                         | Assigned Issues  |
|---	    |---	                                             |---	                                                                                     |---	            |
|Samaya   	|[Samayass](https://github.com/samayass)             |[Samaya's Commits](https://github.com/samayass/flask_portfolio/commits?author=samayass)    |[Samaya's Assigned Issues](https://github.com/samayass/flask_portfolio/issues/assigned/samayass)   	|
|Divya 	    |[Divyanshisuri](https://github.com/Divyanshisuri)   |[Divya's Commits](https://github.com/samayass/flask_portfolio/commits?author=divyanshisuri)|[Divya's Assigned Issues](https://github.com/samayass/flask_portfolio/issues/assigned/divyanshisuri)  |  
|Kamryn 	|[Kamryns](https://github.com/Kamryns)	             |[Kamryn's Commits](https://github.com/samayass/flask_portfolio/commits?author=kamryns)   	 |[Kamryn's Assigned Issues](https://github.com/samayass/flask_portfolio/issues/assigned/kamryns)  	    | 
|Krish      |[Krishnadevl](https://github.com/Krishnadevl)       |[Krish's Commits](https://github.com/samayass/flask_portfolio/commits?author=KrishnadevL)  |[Krish's Assigned Issues](https://github.com/samayass/flask_portfolio/issues/assigned/krishnadevl)   	|

---

### PBL 1,2
Hi! this will be our scoring for the assignments for PBL 1,2 
We have fully completed 7 assignments and have one assignment in progress

Assignment 1: Scrum Board 1/1

Assignment 2:  Integration of greet into a mini-lab page 0.5/1 (greet is able to be added to navbar, however seperate mini-lab page integration has not been made) 

Assignment 3+4: The TPT program has been completed for 2/2 points



###Individual progress

Assignments: Commits (1 point)

Assignment 2: Video Notes (1 point) 

Assignment 3: Greet file (1 point) 

Assignment 4: Tool declare (1 point) 


---

### Idea
Starter code should be fun and practical.
### Visual thoughts
#### Organize with Bootstrap menu 
#### Add some color and fun through VANTA Visuals (birds, halo, solar, net)
#### Show some practical and fun links (hrefs) like Twitter, Git, Youtube
#### Show project specific links (hrefs) per page

### Implementation progress (August 13th, 2021)
#### Project entry point is main.py, this enables Flask Web App and provides capability to renders templates (HTML files)
#### The main.py is the  Web Server Gateway Interface, essentially it contains a HTTP route and HTML file relationship.  The Python code constructs WSGI relationships for index, kangaroos, walruses, and hawkers.
#### The project structure contains many directories and files.  The template directory (containing html files) and static directory (containing js files) are common standards for HTML coding.  Static files can be pictures and videos, in this project they are mostly javascript backgrounds.
#### WSGI templates: index.html, kangaroos.html, ... are aligned with routes in main.py.
#### Other templates support WSGI templates.  The base.html template contains common Head, Style, Body, Script definitions.  WSGI templates often "include" or "extend" these templates.  This is a way to reuse code.
#### The VANTA javascript statics (backgrounds) are shown and defaulted in base.html (birds), but are block replaced as needed in other templates (solar, net, ...)
#### The Bootstrap Navbar code is in navbar.html. The base.html code includes navbar.html.  The WSGI html files extend base.html files.  This is a process of management and correlation to optimize code management.  For instance, if the menu changes discovery of navbar.html is easy, one change reflects on all WSGI html files. 
#### Jinja2 variables usage is to isolate data and allow redefinitions of attributes in templates.  Observe "{% set variable = %}" syntax for definition and "{{ variable }}" for reference.
#### The base.html uses combination of Bootstrap grid styling and custom CSS styling.  Grid styling in observe with the "<Col-3>" markers.  A Bootstrap Grid has a width of 12, thus four "Col-3" markers could fit on a Grid row.
#### A key purpose of this project is to embed links to other content.  The "href=" definition embeds hyperlinks into the rendered HTML.  The base.html file shows usage of "href={{github}}", the "{{github}}" is a Jinja2 variable.  Jinja2 variables are pre-processed by Python, a variable swap with value, before being sent to the browser.

### IDE management (things that happened beyond plan)
#### Recall on ".gitignore" solution to the pains of temporary files.  Start a ".gitignore" and avoid promoting temporary files to Git, for instance IDE xml files.
#### A project needs to establish a "requirements.txt" to keep track of Python packages used by the project.  This help in other IDEs and Deployment.  IntelliJ has menu Tool -> Sync Python Requirements to start file. 

# Doctor K House

## There is are admin users
## run pipenv install
## run pipenv shell
## run python server/app.py
## run npm install --prefix client
## run npm strat --prefix client
## in pipenv cd server and run python seed.py
## option one   username: userOne@doctork.com   password:pass
## other options userTwo@doctork.com , userThree@doctork.com , userFour@doctork.com  all same password

## attemted deployment
front- https://one0-01-2023-phase-5-client.onrender.com
back - https://phase-5-api-o5ni.onrender.com
youtube - https://youtu.be/pkqrBfaMP3Q

## Project requirements 
You must meet the following Phase 5 Project Minimum Requirements:

- Use a Flask/SQLAlchemy API backend with a React frontend.
- Have at least 4 models on the backend, that include the following:
    - At least 1 many-to-many relationship.
    - Full CRUD actions for at least one resource, following REST conventions.
    - User can interact with all models, directly or indirectly (no unused models).
- Have at least 3 different client-side routes using React Router. Be sure to include a nav bar or other UI element that allows users to navigate between routes.
- Implement password hashing and authentication.
- Validations implemented on frontend and backend
    - Use SQLAlchemy validations to verify and protect data on the backend.
    - Use forms and validation through Formik on all input.
        - At least one data type validation.
        - At least one string/number format validation.
- Connect the client and server using fetch().
- [optional/highly recommended] Implement something new not taught in the curriculum. (Check in with your instructor to ensure the scope of your idea is appropriate.)
- [optional/highly recommended] Implement useContext or Redux.
- [optional/highly recommended] Fully deploy and host your project.

## Creating project
Downloaded the python-p4-project-template and modified the name and deleted the metadata git github and canvas. I created a new repo on github and connected my local repo to my github. 

## Started my project
Downloaded the dependencies for my back end

    $pipenv install

and entered the pip enviroment with

    $pipenv shell
Ran 

    $python server/app

to test that my back end project was working

For the front end i downloaded the depencies

    $npm install --prefix client

Ran

    $npm start --prefix client

to start the project and see if it was running

To generate my my database i enetered my pip enviroment with pipenv shell
I enetered my server file by with a cd server command
Created my instance and migrations 

    $flask db init
    $ flask db upgrade head

## functionality

## application
When the page loads are two options.
option one is to log in to start the application with the correct user information. the user must input he correct username and password combination in order to enter the program. If the user inputs incorrect inforamtion they are greeted with a error message that they are unathorized. The user inputs are sent for authentication to the back end. If the inputs provided are correct then the user is allowed entry to the homepage. 

    function handleSubmitLogin(event) {
    event.preventDefault();
    const loginForm = Object.fromEntries(new FormData(event.target).entries());
    fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(loginForm),
    }).then((r) => {
      if (r.ok) {
        r.json().then((data) => onLogin(data));
      } else {
        r.json().then((err) => setError(err));
      }
    });
    }
The other option is rigth bellow and it aloows the user to created a new account with there user name and own password. The email is validated by both the front end part of the project and the back end that it must have the format of an email. None of the fields can be left empty in oder for the inputs be valid and a user to be put into the database. 

      function handleSubmitSignup(event) {
    event.preventDefault();
    const signupform = Object.fromEntries(new FormData(event.target).entries());
    fetch("/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: signupform.name,
        username: signupform.username,
        password: signupform.password,
      }),
    }).then((r) => {
      if (r.ok) {
        r.json().then((data) => onLogin(data));
      } else {
        r.json().then((err) => setError(err));
      }
    })}

once the user is allowed into the app there is a navigation bar that list all the options that will lead to all routes in the project.

### list of clients 
In this part of the app the user(aka the employee) is given a list of options. Each is a link to individual clients. I used 

    import { Link } from "react-router-dom/cjs/react-router-dom.min";

in order to use the link element. A useEffect and a fetch method where used to aquire the reuired information to give the user the informaton reuired to be able to follow the links. 

Depending on the link clicked the user is then routed to the ClientInfo component. When the page loads the employee can see a client profile with information about the client along with there doctor. This is possible because of useParams. 

    import { useParams } from "react-router-dom/cjs/react-router-dom.min";

I am able to ge the user id number from the route. Again i used a useEffect and fetch method combination. 

### Medication Schedule
When the user chooses the medication schedule link the are routed to the corresponding page. At the top there are to buttons.

*Add time slot*

If the user selects to add a time slot, a form is then shown. The form has three inputs that user need to  choose inputs for for the requet to go threw. The  time slot option has a range form 00:00 to 23:00. These option represent time slots. The next field list is the client. The options for this field are a list of names all that belong to a specific client. The final field is the medication poptions. Names of the different medications are all listed and the user must select one of these. There is some validations in the front end that prevent he user from leaving any of the fields empty. 

*Remove time slot*

When the user selects this button they are prompted to choose any of the selected times to delete in both my database and from the clients view. 

The rest of the page is a chart that shows all the medication schedules with all the clients time shedules and the medication required. There is a button under signed off section that will say not sigmned off if the time slot has not been fufilled. When clicked the button is filled with tyhe users name. When the user is logged in only that user name is used for the sign off. This enforces and protects all other user from using any name except there own for accountability. 

### Inventory
This link routes the user to the inventory page. This page has a table that lists all the medical equipmenmt in the building. There are two buttons under the number of storage column.

*decrease by 1*

When the user selects this option there a patch request sent to the backend that decreases the number by one and modifies the database. Also the effect is seen instanly for the user.

*restock*

This button sends a patch request to the backend that resets the number in stoclk to ten. This modifies the database and can also be seen on the frontend by the user instanly. 

### List of Doctors
This link routes the user to a page that displays doctor information. This is a contact information page. Each card hold the information of the doctor including a list clients that they attend to. This is done by using a fetch request to my backend. 

### List of Employees 
The list of employees route is very similar to the doctors one. It gives you a information for every employee displayed in cards. The only main diference from this part of the project from the rest is that its only allowed to be viewed by people with permisions. This can be seen when a user with no permisiions get an accessed denied message and people with the correct permisions can see the the employee information. This works because the user that logs is automatically saved into a session in the backend. The backend then determines what information is passed to the front end so that whoever wants to see the information must be the correct user. 

      return (
    <div className="cards">
      <h1>List of Employees</h1>
      {errors.errors != "Access denied" ? (
        employees.map((empl, index) => {
          return (
            <div key={index}>
              <EmployeeInfo employee={empl} />
            </div>
          );
        })
      ) : (
        <h1 style={{ backgroundColor: "red" }}>{errors.errors}</h1>
      )}
    </div>
  );
  
### List of medications 
This page is very simple and similar to the medication schedule. Its a table that shows the name of the medications and what they do. A fetch request is made to the backend and received json data is stored into a state variable and dispayed by using table and mapping. 

### REPORTS
This part of my front end is shown when the user selects reports link on the navigation. At the top there is a button that allows the user to view past reports or reports just made. 

*view reports button*

Each option is a link that redirects the user to a route that displays the report that they choose.

Once a report is selected they are taken to a page that shows the title, the date of the report, and the comtext of the report. This is viewable by any employee in the database. The information is obtained when the fetch request is made when loading that page. The way the request knows what specific report is selected is by using params 

  
    useEffect(() => {
      fetch(`/reports/${params.id}`)
        .then((r) => r.json())
        .then((data) => setReport((report) => (report = data)));
    }, [params.id]);

### logout
The final choice in the mavigation bar is a button that sets 

    const [isLogged, setIsLogged] = useState(null);

  to null and redirects the user to the login page where the next user/employee needs to input there credentials to log in as use the aplications with there selected restrictions if any are set. 

## Models.py
For my models I created classes that repesented each table I wanted to include for my project. 

Doctor

For this class i had columns that described the doctor and also established a relationship with the client table. The doctors table has a one to many relationship, meaning that one doctor can have many clients. The validations include ceratin columns not being able to be empty in any way. The email column was put a validation that it had to be in the style an email. 

client

The client table just like the doctor has columns that describe and have informaton about the client. Retrictions and validations where set on the client class. Certain field are not allowed to have an empty field in any way. The relationships for the clients are a few more than the doctor class. There is a column that represents the raltionship between the client and the doctor. This relationship is a one to many since every client only has one doctor. The medication relationship is a many to many since one client can have many medications and many a medicatios can have many clients. For the reports relationship its a one to many.

Medication

The medication class columns that represent the information i need to display on my application for medication. There is a many to many relationship with the client class. there a few restrictions and validations hat restrict certain fields being left empty.

Med_times

This class has the most relationships of the backend. It has its own columns that describe what this table holds but the mojority of the inforamtion is realtionships with other tables. The signed off column has a many to one relationship meaning many times can have a single employee. The client id column has a similar relationship that links many times to one client. The medication id is a many to one relationship because one many time slots can one one medication scheduled. 

The next to relationships are a little different. the clients and medications values are not only used in the med times class but also help link the  clients and the medications table. With these variables the many to many elationship was able to be established. This is just one way to do this. I choose this way because i was able to create the useful table of med times with all thhis information. 

Inventory

This table is like the other tables. The only main difference is that there is no link for thsi class and any other class. No classes are dependent on this  class and visa versa. Validations where set that the amount of items could e negative. The was also validations that some of the columns could not have null or emty string information. 

Reports

The reports class is like other classes. it has columns specific to itself. Some of the columns have restrictions and validations that do not allow the informationnot to exist or not have an empty field. Another validation is that the content field has to be as least 25 chracters long in order for the session commit to happen, other wise an error is returned to the front end. The relationships made in this field are between the client and also the employee class. These both are many to one relationships because both these columns can only have one id each, but one id can belong to many fields. 

Employee 

This class has the same thig as other classes with the columns and the relationships. The restrictions and validations are similar to the doctor class where there can be no null values or empty strings. 

In the employee class is where I used authentication with Bcrypt. I used this librabry to hash the passwords of users passwords and make it hard for anyone to be able to hack the passwords.

### app.py
In this file i took all the information from my models and  turned the desired information from specific classes and turning it into json data. Once a request is received from the front end the process begings and the json data is returned as a reponse along with an http code. 

    user = request.get_json()
        user_info = Employee.query.filter(Employee.username == user['username']).first()
        if user_info:
            if user_info.authenticate(user['password']) == True:
                user_dict = {
                    'name': user_info.name,
                    'id': user_info.id,
                }
                session["user_id"] = user_info.id
                return user_dict, 200
            else:
                return {"errors":"Unathorized"}, 401
        else:
                return {"errors":"Unathorized"}, 401

One route that was not was not displayed as an option for the program wa sthe check session. This route checked if the user was logged in and gave values to certain fields when the request, post requests, where made. 

    class CheckSession(Resource):
    def get(self):
        user = Employee.query.filter(Employee.id == session.get("user_id")).first()
        if user:
            user_info = {
                'username': user.username,
                'name': user.name, 
                'id': user.id
            }
            return user.to_dict(), 200
        else:
            return {'errors': 'Unathorized'}, 401 

example of a post method that uses the session['user_id']


     try: 
            client_name = Client.query.filter(Client.name == json['client_name']).first()
            print(client_name.name)
            new_report = Report(
                type_of_report= json['type_of_report'],
                context= json['context'],
                client_name= client_name.name,
                employee_id= session.get('user_id')
            )
            db.session.add(new_report)
            db.session.commit()
            return {'message': 'object created'}, 201
        except Exception:
            return {'errors': 'Unprcessible '}


## Contributations
Pull request are appreciated. Any feed back on improving the project(do's and dont's).

## Citations
All medications exept adderal:
- Brennan, D. (2021, October 4). What are the top 10 most prescribed drugs?. MedicineNet. https://www.medicinenet.com/what_are_the_top_10_most_prescribed_drugs/article.htm 

luffy image
- Luffy Gear 5 ! by ranshiiki on DeviantArt. by Ranshiiki on DeviantArt. (n.d.). https://www.deviantart.com/ranshiiki/art/Luffy-Gear-5-975671847 

Adderal description and name:
- Durbin, K. (n.d.). Adderall: Uses, dosage, Side Effects &amp; Safety Info. Drugs.com. https://www.drugs.com/adderall.html 


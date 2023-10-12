import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import NavBar from "./NavBar";
import Inventory from "./Inventory";
import MedicationTimes from "./MedicationTimes";
import Clients from "./Clients";
import Medications from "./Medications";
import Doctors from "./Doctors";
import Employees from "./Employees";
import Report from "./Report";
import Login from "./Login";
import ReportInfo from "./ReportInfo";
import ClientInfo from "./ClientInfo";
import Home from "./Home";

function App() {
  //set a is logged in state to check if im logged in and display correct page
  //set name from login page and display at top for the welcome
  const [isLogged, setIsLogged] = useState(null);

  //chech session to see if the user is logged in to set the state of is logged
  //used for auto logged in
  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((data) => setIsLogged((isLogged) => (isLogged = data)));
      }
    });
  }, []);

  //check if logged in, if yes go to app page, if not display login page
  if (!isLogged) {
    return <Login onLogin={setIsLogged} />;
  }

  return (
    <div className="App" class="text-center">
      <h1>Dr.Kevins House</h1>
      <NavBar onLogout={setIsLogged} />
      <Switch>
        <Route exact path="/">
          <Home employee={isLogged}/>
        </Route>
        <Route exact path="/inventory">
          <Inventory />
        </Route>
        <Route exact path="/medication_times">
          <MedicationTimes userInfo={isLogged} />
        </Route>
        <Route exact path="/clients">
          <Clients />
        </Route>
        <Route exact path={`/clients/:id`}>
          <ClientInfo />
        </Route>
        <Route exact path="/medications">
          <Medications />
        </Route>
        <Route exact path="/doctors">
          <Doctors />
        </Route>
        <Route exact path="/employees">
          <Employees />
        </Route>
        <Route exact path="/reports">
          <Report />
        </Route>
        <Route exact path={`/reports/:id`}>
          <ReportInfo />
        </Route>
      </Switch>
    </div>
  );
}

export default App;

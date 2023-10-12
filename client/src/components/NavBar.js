import React from "react";
import { NavLink } from "react-router-dom";

//returns a navigation bar with links to a desired path
function NavBar({ onLogout }) {
  function onHandleLogout() {
    fetch("/logout", {
      method: "DELETE",
    }).then((r) => onLogout(null));
  }

  return (
    <div className="navbar" class="inline-block">
      <NavLink to="/" exact className="navlink">
        Home
      </NavLink>
      <NavLink to="/clients" exact className="navlink">
        List of Clients
      </NavLink>
      <NavLink to="/medication_times" exact className="navlink">
        Medication Schedule
      </NavLink>
      <NavLink to="/inventory" exact className="navlink">
        Inventory
      </NavLink>
      <NavLink to="/medications" exact className="navlink">
        Medications
      </NavLink>
      <NavLink to="/doctors" exact className="navlink">
        List of Doctors
      </NavLink>
      <NavLink to="/employees" exact className="navlink">
        List of Employees
      </NavLink>
      <NavLink to="/reports" exact className="navlink">
        REPORTS
      </NavLink>
      <NavLink to="/" className="navlink" onClick={onHandleLogout}>
        LOG-OUT
      </NavLink>
    </div>
  );
}
export default NavBar;

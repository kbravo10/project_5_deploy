import React, { useEffect, useState } from "react";
import EmployeeInfo from "./EmployeeInfo";

function Employees() {
  //declare usestate to assign json data
  const [employees, setEmployees] = useState([]);
  const [errors, setErrors] = useState([]);

  //useeffect to only render once
  useEffect(() => {
    fetch("/employees").then((r) => {
      if (r.ok) {
        r.json().then((data) =>
          setEmployees((employees) => (employees = data))
        );
      } else {
        r.json().then((err) => setErrors(err));
      }
    });
  }, []);

  return (
    <div className="cards">
      <h1>List of Employees</h1>
      {errors.errors !== "Access denied" ? (
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
}

export default Employees;

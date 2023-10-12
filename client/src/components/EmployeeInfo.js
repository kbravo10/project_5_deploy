import React from "react";

function EmployeeInfo({ employee }) {
  return (
    <div className="cardInfo">
      <div className="employeeCardDiv">
        <h2>{employee.name}</h2>
        <br></br>
        <h3>username/email:</h3>
        <p>{employee.username}</p>
        <h3>phone number:</h3>
        <p>{employee.number}</p>
        <h3>ADMIN:</h3>
        {employee.admin === 1 ? <p>YES</p> : <p>NO</p>}
      </div>
    </div>
  );
}

export default EmployeeInfo;

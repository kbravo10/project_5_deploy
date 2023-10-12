import React, { useEffect, useState } from "react";
import DoctorInfo from "./DoctorInfo";

function Doctors() {
  //declare usestate to assign json data
  const [doctors, setDoctors] = useState([]);

  //useeffect to only render once
  useEffect(() => {
    fetch("/doctors")
      .then((r) => r.json())
      .then((data) => setDoctors((doctors) => (doctors = data)));
  }, []);

  return (
    <div className="cards">
      <h1>Doctors</h1>
      {doctors.map((doc, index) => {
        return (
          <div key={index} className="doctorDisplay">
            <DoctorInfo key={index} docInfo={doc} />
          </div>
        );
      })}
    </div>
  );
}

export default Doctors;

import React, { useEffect, useState } from "react";
import MedInfo from "./MedInfo";

function Medications() {
  //declare usestate to assign json data
  const [medications, setMedication] = useState([]);

  //useeffect to only render once
  useEffect(() => {
    fetch("/medications")
      .then((r) => r.json())
      .then((data) => setMedication((medications) => (medications = data)));
  }, []);

  return (
    <div className="cards">
      <h1>List Medications</h1>
      <table class="container">
        <thead>
          <tr class="text-start">
            <th scope="col">Medication Name</th>
            <th scope="col">Description</th>
          </tr>
        </thead>
        {medications.map((med, index) => {
          return <MedInfo key={index} med={med} />;
        })}
      </table>
    </div>
  );
}

export default Medications;

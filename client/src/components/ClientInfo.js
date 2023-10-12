import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom/cjs/react-router-dom.min";

function ClientInfo() {
  const [client, setClient] = useState([]);
  const [meds, setMeds] = useState([]);
  const params = useParams();

  useEffect(() => {
    fetch(`/clients/${params.id}`)
      .then((r) => r.json())
      .then((data) => {
        setClient(data);
        setMeds(data.medications);
      });
  }, [params.id]);
  return (
    <div className="cardInfo">
      <div className="descriptionDiv">
        <div className="descriptionCard">
          <h3>Name: {client.name}</h3>
          <h2>Age: {client.age}</h2>
        </div>
        <img className="cardImage" alt="oops" src={client.image} />
      </div>
      <br></br>
      <div className="bioDiv">
        <h3>Summary/bio: </h3>
        <p>{client.bio}</p>
      </div>
      <br></br>
      <div className="medicalContactDiv">
        <h3>Doctor: {client.doctor}</h3>
        <h3>phone #: {client.doctor_phone}</h3>
      </div>
      <br></br>
      <div className="medicationDiv">
        <h3>Medications:</h3>
        {meds.map((med, index) => {
          return(
            <p key={index}>
              {med}
            </p>
          )
        })}
      </div>
    </div>
  );
}

export default ClientInfo;

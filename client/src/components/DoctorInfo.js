import React from "react";

function DoctorInfo({ docInfo }) {
  return (
    <div className="cardInfo">
      <h2>{docInfo.name}</h2>
      <h3>E-mail: {docInfo.email}</h3>
      <h3>Phone #: {docInfo.number}</h3>
      <h3>Clients: </h3>

      {docInfo.clients.map((client, index) => {
        return (
          <li key={index} className="listRelationship">
            Name: {client.name}, ID: {client.id}
          </li>
        );
      })}
    </div>
  );
}

export default DoctorInfo;

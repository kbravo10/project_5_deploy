import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom/cjs/react-router-dom.min";

function Clients() {
  //declare usestate to get data from backend
  const [clients, setClients] = useState([]);

  //useeffect to only render once fetch
  useEffect(() => {
    fetch("/clients")
      .then((r) => r.json())
      .then((data) => setClients((clients) => (clients = data)));
  }, []);

  return (
    <div className="cards">
      <h1>Clients</h1>
      {clients.map((client, index) => {
        return (
          <div key={index} className="clientDisplay">
            <Link className="link" to={`/clients/${client.id}`}>
              ID:{client.id} - {client.name}
            </Link>
          </div>
        );
      })}
    </div>
  );
}

export default Clients;

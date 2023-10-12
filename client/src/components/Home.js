import React from "react";

function Home({ employee }) {
  return (
    <div>
      <h1>Welcome</h1>
      <h1>{employee.name}</h1>
      <h2>LET'S HAVE A GOOD DAY!!!</h2>
    </div>
  );
}

export default Home;

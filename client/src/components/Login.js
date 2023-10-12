import React, { useState } from "react";

function Login({ onLogin }) {
  const [error, setError] = useState([]);
  function handleSubmitLogin(event) {
    event.preventDefault();
    const loginForm = Object.fromEntries(new FormData(event.target).entries());
    fetch("https://phase-5-api-o5ni.onrender.com/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(loginForm),
    }).then((r) => {
      if (r.ok) {
        r.json().then((data) => onLogin(data));
      } else {
        r.json().then((err) => setError(err));
      }
    });
  }
  function handleSubmitSignup(event) {
    event.preventDefault();
    const signupform = Object.fromEntries(new FormData(event.target).entries());
    fetch("https://phase-5-api-o5ni.onrender.com/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: signupform.name,
        username: signupform.username,
        password: signupform.password,
      }),
    }).then((r) => {
      if (r.ok) {
        r.json().then((data) => onLogin(data));
      } else {
        r.json().then((err) => setError(err));
      }
    });
  }
  return (
    <div class="text-center">
      <form className="loginForm" onSubmit={handleSubmitLogin}>
        <div class="form-outline mb-4" className="username">
          <label class="form-label">UserName:</label>
          <input type="text" name="username"></input>
        </div>
        <div>
          <label class="form-label">Password:</label>
          <input type="password" name="password"></input>
        </div>
        <div className="submit">
          <button type="submit">Login</button>
        </div>
      </form>
      <p style={{ color: "red" }}>{error.errors}</p>
      <br></br>
      <br></br>
      <form className="signupForm" onSubmit={handleSubmitSignup}>
        <label>New employee?</label>
        <div>
          <label>Enter name: </label>
          <input type="text" name="name"></input>
        </div>
        <div>
          <label>Enter email: </label>
          <input type="email" name="username"></input>
        </div>
        <div>
          <label>Enter new password:</label>
          <input type="password" name="password"></input>
        </div>
        <button type="submit">Make Account</button>
      </form>
      <p style={{ color: "red" }}>{error.errors}</p>
    </div>
  );
}

export default Login;

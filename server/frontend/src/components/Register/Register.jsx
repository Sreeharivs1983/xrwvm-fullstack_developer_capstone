import React, { useState } from "react";
import "./Register.css";
import user_icon from "../assets/person.png";
import email_icon from "../assets/email.png";
import password_icon from "../assets/password.png";
import close_icon from "../assets/close.png";

const Register = () => {

  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");

  const gohome = () => {
    window.location.href = window.location.origin;
  };

  const register = async (e) => {
    e.preventDefault();

    let register_url = window.location.origin + "/djangoapp/register";

    const res = await fetch(register_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userName: userName,
        password: password,
        firstName: firstName,
        lastName: lastName,
        email: email
      }),
    });

    const json = await res.json();

    if (json.status) {
      sessionStorage.setItem('username', json.userName);
      window.location.href = window.location.origin;
    } 
    else if (json.error === "Already Registered") {
      alert("The user with same username is already registered");
    }
  };

  return (
    <div className="register_container" style={{ width: "50%" }}>
      <div className="header" style={{ display: "flex", flexDirection: "row", justifyContent: "space-between" }}>
        <span className="text" style={{ flexGrow: "1" }}>SignUp</span>
        <div>
          <a href="/" onClick={gohome}>
            <img style={{ width: "1cm" }} src={close_icon} alt="X" />
          </a>
        </div>
      </div>

      <form onSubmit={register}>
        <div className="inputs">

          <div>
            <img src={user_icon} className="img_icon" alt="Username" />
            <input type="text" placeholder="Username"
              onChange={(e) => setUserName(e.target.value)} />
          </div>

          <div>
            <img src={user_icon} className="img_icon" alt="First Name" />
            <input type="text" placeholder="First Name"
              onChange={(e) => setFirstName(e.target.value)} />
          </div>

          <div>
            <img src={user_icon} className="img_icon" alt="Last Name" />
            <input type="text" placeholder="Last Name"
              onChange={(e) => setLastName(e.target.value)} />
          </div>

          <div>
            <img src={email_icon} className="img_icon" alt="Email" />
            <input type="email" placeholder="Email"
              onChange={(e) => setEmail(e.target.value)} />
          </div>

          <div>
            <img src={password_icon} className="img_icon" alt="Password" />
            <input type="password" placeholder="Password"
              onChange={(e) => setPassword(e.target.value)} />
          </div>

        </div>

        <div className="submit_panel">
          <input className="submit" type="submit" value="Register" />
        </div>
      </form>
    </div>
  );
};

export default Register;
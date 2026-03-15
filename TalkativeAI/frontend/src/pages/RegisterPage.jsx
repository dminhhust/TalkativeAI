import { useState } from "react";
import { register } from "../api/api";

export default function RegisterPage({ setPage }) {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {

    try {

      await register({
        username,
        password
      });

      alert("Registration successful");

      setPage("login");

    } catch (err) {

      alert("Registration failed");

    }

  };

  return (
    <div className="auth-container">

      <h2>Create Account</h2>

      <input
        placeholder="Username"
        value={username}
        onChange={(e) =>
          setUsername(e.target.value)
        }
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) =>
          setPassword(e.target.value)
        }
      />

      <button onClick={handleRegister}>
        Register
      </button>

      <p>
        Already have an account?
      </p>

      <button onClick={() => setPage("login")}>
        Go to Login
      </button>

    </div>
  );
}

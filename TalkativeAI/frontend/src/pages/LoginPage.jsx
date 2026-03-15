import { useState } from "react";
import { login } from "../api/api";

export default function LoginPage({ setToken, setPage }) {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {

    try {

      const res = await login({
        username,
        password
      });

      setToken(res.data.access_token);

    } catch {

      alert("Login failed");

    }

  };

  return (
    <div className="auth-container">

      <h2>Login</h2>

      <input
        placeholder="Username"
        onChange={(e) =>
          setUsername(e.target.value)
        }
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) =>
          setPassword(e.target.value)
        }
      />

      <button onClick={handleLogin}>
        Login
      </button>

      <p>No account?</p>

      <button onClick={() => setPage("register")}>
        Register
      </button>

    </div>
  );
}

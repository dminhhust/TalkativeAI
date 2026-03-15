import { useState } from "react";
import LoginPage from "./src/pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import Dashboard from "./pages/Dashboard";

export default function App() {

  const [token, setToken] = useState(null);
  const [page, setPage] = useState("login");

  if (!token) {

    if (page === "login") {
      return <LoginPage setToken={setToken} setPage={setPage} />;
    }

    return <RegisterPage setPage={setPage} />;
  }

  return <Dashboard token={token} />;
}

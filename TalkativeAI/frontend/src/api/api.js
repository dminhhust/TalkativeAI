import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000"
});

export const register = (data) =>
  API.post("/auth/register", data);

export const login = (data) =>
  API.post("/auth/login", data);

export const sendMessage = (data, token) =>
  API.post("/conversation/message", data, {
    headers: { Authorization: `Bearer ${token}` }
  });

export const getHistory = (token) =>
  API.get("/session/history", {
    headers: { Authorization: `Bearer ${token}` }
  });

import axios from "axios";

const http = axios.create({
  baseURL: "http://localhost:8000/",
});

// @ts-ignore
http.interceptors.response.use((response) => {
  return { data: response.data, status: response.status };
});

const camelToSnakeCase = (str: string) =>
  str.replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`);

http.interceptors.request.use((config) => {
  if (config.method?.toLowerCase() === "post") {
    const updatedBody = {};
    Object.keys(config.data).forEach((key) => {
      const snakeCaseKey = camelToSnakeCase(key);
      // @ts-ignore
      updatedBody[snakeCaseKey] = config.data[key];
    });
    config.data = updatedBody;
  }
  return config;
});

http.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");

  if (token) {
    config.headers.Authorization = "Token " + token;
  }

  return config;
});

export default http;

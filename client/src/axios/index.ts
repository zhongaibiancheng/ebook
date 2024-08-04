import axios from "axios";

const apiClient = axios.create({
  // APIのURI
  baseURL: "http://localhost:5002",
  // リクエストヘッダ
  headers: {
    "Content-type": "application/json",
  },
});

export default apiClient;

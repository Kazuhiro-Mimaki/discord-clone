import * as express from "express";
import * as http from "http";
import * as cors from "cors";

require("dotenv").config();

const PORT = process.env.PORT || process.env.API_PORT;

const app = express();
app.use(express.json());
app.use(cors());

// register the routes
app.get("/test", (req, res) => {
  res.send("Success test response!");
});

// signup
app.post("/signup", (req, res) => {});

// signin

const server = http.createServer(app);

server.listen(PORT, () => {
  console.log(`Example app listening on port ${PORT}`);
});

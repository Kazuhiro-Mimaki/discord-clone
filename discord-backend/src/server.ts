import * as express from "express";
// const cors = require("cors");
require("dotenv").config();

const PORT = process.env.PORT || process.env.API_PORT;

const app = express();
app.use(express.json());
// app.use(cors());

// register the routes
app.get("/test", (req, res) => {
  res.send("Success test response!");
});

app.listen(PORT, () => {
  console.log(`Example app listening on port ${PORT}`);
});

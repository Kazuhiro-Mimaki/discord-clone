import type { NextPage } from "next";
import { useEffect, useState } from "react";
import styles from "../styles/Home.module.css";

const Home: NextPage = () => {
  const [count, setCount] = useState(0);

  let ws: WebSocket | null = null;

  useEffect(() => {
    console.log("Start websocket connection");
    ws = new WebSocket("ws://localhost:8000/ws");
    ws.onopen = () => ws!.send("Connected to Server");
    console.log(ws);
  }, []);

  return (
    <div className={styles.container}>
      <button onClick={() => setCount(count + 1)}>+</button>
      <div>{count}</div>
    </div>
  );
};

export default Home;

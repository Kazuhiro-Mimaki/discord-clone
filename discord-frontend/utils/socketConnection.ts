export const connectWithSocketServer = () => {
  const ws = new WebSocket("ws://localhost:8000/ws");
  ws.onopen = () => {
    ws!.send("Connected to Server");
  };
  ws.onmessage = (event) => {
    console.log(event);
  };
};

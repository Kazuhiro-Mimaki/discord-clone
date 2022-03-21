import { useState, useEffect, KeyboardEvent, ChangeEvent } from "react";
import styles from "./component.module.css";

type Props = {
  setMessageList: Function;
};

const NewMessageInput = ({ setMessageList }: Props) => {
  const [message, setMessage] = useState("");

  const handleMessageValueChange = (event: ChangeEvent<HTMLInputElement>) => {
    setMessage(event.target.value);
  };

  const handleKeyPressed = (event: KeyboardEvent<HTMLElement>): void => {
    if (event.key === "Enter") {
      handleSendMessage();
    }
  };

  const handleSendMessage = () => {
    if (message.length > 0) {
      const ws = new WebSocket("ws://localhost:8000/ws");
      ws.onopen = (event) => {
        const request = {
          route: "create-message",
          content: message,
        };
        ws!.send(JSON.stringify(request));
      };
      ws.onmessage = (event) => {
        console.log(JSON.parse(event.data));
        setMessageList(JSON.parse(event.data));
      };
      setMessage("");
    }
  };

  return (
    <div className={styles.container}>
      <input
        placeholder="Write message"
        value={message}
        onChange={handleMessageValueChange}
        onKeyDown={handleKeyPressed}
      />
    </div>
  );
};

export default NewMessageInput;

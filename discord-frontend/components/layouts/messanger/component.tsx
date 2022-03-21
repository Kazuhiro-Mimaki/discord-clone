import styles from "./component.module.css";
import NewMessageInput from "./new-message-input/component";
import Messages from "./messages/component";
import { useEffect, useState } from "react";

const Messanger = () => {
  const [messageList, setMessageList] = useState<object[]>([]);
  // const updateMessageList = () => {
  //   setMessageList(newMessageList)
  // };
  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws");
    ws.onmessage = (event) => {
      console.log(JSON.parse(event.data));
    };
  }, [messageList]);

  const handleSetMessageList = (newMessageList: object[]) => {
    setMessageList(newMessageList);
  };

  return (
    <div className={styles.container}>
      <Messages messageList={messageList} />
      <NewMessageInput setMessageList={handleSetMessageList} />
    </div>
  );
};

export default Messanger;

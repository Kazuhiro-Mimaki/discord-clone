import styles from "./component.module.css";

type Props = {
  messageList: any[];
};

const Messages = ({ messageList }: Props) => {
  return (
    <div className={styles.container}>
      {messageList.map((message, i) => {
        return <div key={i}>{message.content}</div>;
      })}
    </div>
  );
};

export default Messages;

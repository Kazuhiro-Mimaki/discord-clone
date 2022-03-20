import Button from "@mui/material/Button";

type Props = {
  onClick: VoidFunction;
};

const AddFriendButton = ({ onClick }: Props) => {
  return (
    <Button
      onClick={onClick}
      style={{
        width: "80%",
        height: "30px",
        margin: "1rem",
        textTransform: "none",
        fontWeight: 500,
        fontSize: "16px",
        color: "#fff",
        background: "#3ba55d",
      }}
    >
      Add friend
    </Button>
  );
};

export default AddFriendButton;

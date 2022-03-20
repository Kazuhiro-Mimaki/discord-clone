import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import Typography from "@mui/material/Typography";

type Props = {
  isDialogOpen: boolean;
  closeDialogHandler: VoidFunction;
};

const AddFriendDialog = ({ isDialogOpen, closeDialogHandler }: Props) => {
  return (
    <Dialog open={isDialogOpen} onClose={closeDialogHandler}>
      <DialogTitle>
        <Typography>Invite a Friend</Typography>
      </DialogTitle>
      <DialogContent>
        <DialogContentText>
          <Typography>
            Enter e-mail address of friend which you would like to invite
          </Typography>
        </DialogContentText>
        <input type="text" />
      </DialogContent>
      <DialogActions>
        <Button
          onClick={closeDialogHandler}
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
          Send
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default AddFriendDialog;

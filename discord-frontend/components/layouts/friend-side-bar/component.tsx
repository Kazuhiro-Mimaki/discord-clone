import { useState } from "react";
import { AddFriendButton, AddFriendDialog } from "../../componentProvider";
import styles from "./component.module.css";

const FriendSideBar = () => {
  const [isDialogOpen, setIsDialogOpen] = useState(false);

  const handleOpenAddFriendDialog = () => {
    setIsDialogOpen(true);
  };

  const handleCloseAddFriendDialog = () => {
    setIsDialogOpen(false);
  };

  return (
    <div className={styles.container}>
      <AddFriendButton onClick={handleOpenAddFriendDialog} />
      <AddFriendDialog
        isDialogOpen={isDialogOpen}
        closeDialogHandler={handleCloseAddFriendDialog}
      />
    </div>
  );
};

export default FriendSideBar;

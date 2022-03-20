import type { NextComponentType } from "next";
import styles from "./component.module.css";
import { Button } from "../../componentProvider";

const SideBar: NextComponentType = () => {
  return (
    <div className={styles.container}>
      <Button />
    </div>
  );
};

export default SideBar;

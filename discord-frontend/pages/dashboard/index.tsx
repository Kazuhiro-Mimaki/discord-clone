import type { NextPage } from "next";
import styles from "./index.module.css";
import {
  SideBar,
  FriendSideBar,
  AppBar,
  Messanger,
} from "../../components/componentProvider";
import { useEffect } from "react";

const Dashboard: NextPage = () => {
  useEffect(() => {}, []);

  return (
    <div className={styles.container}>
      <section className={styles.sidebar}>
        <SideBar />
        <FriendSideBar />
      </section>
      <section className={styles.main}>
        <AppBar />
        <Messanger />
      </section>
    </div>
  );
};

export default Dashboard;

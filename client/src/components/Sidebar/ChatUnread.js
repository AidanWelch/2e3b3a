import React from "react";
import { Badge } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  root: {
    marginRight: 35,
    height: 20
  },
}));

const ChatUnread = ({ unread }) => {
  const classes = useStyles();

  return (
    <Badge
      badgeContent={unread}
      color="primary"
      transformorigin={{ horizontal: "left", vertical: "center" }}	
      className={classes.root}
    />
  );
};

export default ChatUnread;

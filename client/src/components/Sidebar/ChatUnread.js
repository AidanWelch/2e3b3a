import React from "react";
import { Box, Badge } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  root: {
	marginRight: 35,
	height: 20
  },
}));

const ChatUnread = ({ unread }) => {
  const classes = useStyles();

  if(!unread)
	return null;

  return (
    <Badge
	  badgeContent={unread}
	  color="primary"
	  anchorOrigin={{ horizontal: "right", vertical: "center" }}
	  transformOrigin={{ horizontal: "left", vertical: "center" }}	
	  className={classes.root}
	  invisible={true}
	/>
  );
};

export default ChatUnread;

import React from 'react';
import { Box, makeStyles } from '@material-ui/core';
import { SenderBubble, OtherUserBubble } from '.';
import moment from 'moment';

const useStyles = makeStyles(() => ({
  messageContainer: {
    display: 'flex',
	flexDirection: 'column-reverse',
  },
}));

const Messages = (props) => {
  const classes = useStyles();
  const { messages, otherUser, userId } = props;
  return (
    <Box className={classes.messageContainer}>
      {messages.map((message) => {
        const time = moment(message.createdAt).format('h:mm');

        return message.senderId === userId ? (
          <SenderBubble key={message.id} text={message.text} time={time} />
        ) : (
          <OtherUserBubble
            key={message.id}
            text={message.text}
            time={time}
            otherUser={otherUser}
          />
        );
      })}
    </Box>
  );
};

export default Messages;

import React from "react";
import ReactPlayer from "react-player";

export default function Page() {
  return (
    <div>
      <br />
      <br />
      <br />
      <br />
      <ReactPlayer
        url="https://www.youtube.com/watch?v=63GPzSIAPMI&ab_channel=TrapMusicHDTV"
        controls={false}
      />
      <br />
      <br />
      <br />
      <br />
      <ReactPlayer url="./static/todo.mp4" controls={true} />
    </div>
  );
}

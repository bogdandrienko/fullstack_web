import React from "react";

export function Button1({
  color,
  children,
}: {
  color: string;
  children: any;
}): JSX.Element {
  function Click1() {
    window.alert("Угроза!");
  }

  return (
    <div
      onClick={Click1}
      className={color === "orange" ? "bg-orange-500" : "bg-amber-800"}
    >
      {children}
    </div>
  );
}

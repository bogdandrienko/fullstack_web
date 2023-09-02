import React from "react";

export function Base1({ children }: { children: any }): JSX.Element {
  return (
    <div>
      <div>header</div>
      {children}
      <div>footer</div>
    </div>
  );
}

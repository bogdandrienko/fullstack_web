import React from "react";

export default function Page() {
  return (
    <div>
      <div className="text-center">
        <h1 className="display-4 fw-bold">Todo list app</h1>
        <div className="overflow-hidden">
          <div className="container px-5">
            <img
              src="./static/img/to-do-list-apps.png"
              className="img-fluid img-thumbnail border rounded-3 shadow-lg mb-1"
              alt="Example image"
              width="600"
              height="400"
              loading="lazy"
            />
          </div>
        </div>
      </div>
    </div>
  );
}

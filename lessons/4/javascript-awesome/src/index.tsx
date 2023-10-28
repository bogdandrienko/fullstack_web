import React from 'react';
import { createRoot } from 'react-dom/client';
import Data from './app/6Exceptions'

const container = document.getElementById('root')!;
const root = createRoot(container);

function App (){
    return <div>JS</div>
}


root.render(
  // <React.StrictMode>
      <Data />
  // </React.StrictMode>
);

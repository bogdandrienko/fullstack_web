import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from './components/store';
import Router from './components/router';
import './index.css';

const container = document.getElementById('root')!;
const root = createRoot(container);

function App(){
    return <div>App</div>
}

root.render(
  // <React.StrictMode>
    <Provider store={store}>
      <Router />
    </Provider>
  // </React.StrictMode>
);

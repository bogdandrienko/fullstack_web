import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from './app/store';
import {Counter1, Counter2} from './components/counter';
import './index.css';

const container = document.getElementById('root')!;
const root = createRoot(container);

root.render(
  // <React.StrictMode>
    <Provider store={store}>
      {/*<Counter1 counter={888} />*/}
      <Counter2 />
    </Provider>
  // </React.StrictMode>
);

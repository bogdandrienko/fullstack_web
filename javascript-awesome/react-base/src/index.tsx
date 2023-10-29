import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from './app/store';
import App from './App';
import './index.css';

const container = document.getElementById('root')!;
const root = createRoot(container);

const docs = `
1) Элементы и компоненты. Проброс "пропсов" и параметров, children.
2) 
3) Подключение стилей: cdn(bootsrtap) / native(custom css) / libs(material ui).
4) Реакт хуки: useState, useEffect...
5) React + Redux.
`

root.render(
  // <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  // </React.StrictMode>
);

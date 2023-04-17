import React from 'react';
import App from './App';
import "./styles.css";
import { render } from 'react-dom';

const container = document.getElementById('root');

render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  container
);

import React from 'react';
import { render } from 'react-dom';
import thunk from 'redux-thunk';
import createLogger from 'redux-logger';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux'

import App from './components/App';
import Routes from './routes';
import mainReducer from './reducers/mainReducer';

import mainCSS from './components/main.scss'


const store = createStore(
    mainReducer,
    applyMiddleware(thunk, createLogger())
);

const rootElement = document.getElementById('root');

render(
    <Provider store={store}>
        <Routes />
    </Provider>,
    rootElement
);
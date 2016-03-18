import React from 'react';
import { render } from 'react-dom';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux'
import thunk from 'redux-thunk';

import App from './components/App';
import Routes from './routes';

import mainReducer from './reducers/mainReducer';

import mainCSS from './components/main.scss'

const store = createStore(
    mainReducer,
    applyMiddleware(thunk)
);

const rootElement = document.getElementById('root');

render(
    <Provider store={store}>
        <Routes />
    </Provider>,
    rootElement
);
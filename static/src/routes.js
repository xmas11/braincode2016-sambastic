import React, { Component } from 'react'
import { Router, Route, IndexRoute, browserHistory } from 'react-router';

import App from './components/App';
import Hello from './components/Hello';

export default class Routes extends Component {
    render() {
        return (
            <Router history={browserHistory}>
                <Route path="*" component={App}>
                    <IndexRoute component={Hello}/>
                </Route>
            </Router>
        );
    }
}

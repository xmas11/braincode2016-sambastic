import React from 'react';
import { Button } from 'react-bootstrap';

export default class Hello extends React.Component {
    constructor(...args) {
        super(...args);
    }
    render() {
        return (
            <Button>
                Hello
            </Button>
        );
    }
}
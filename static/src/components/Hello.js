import React from 'react';
import { Button, Card, Row, Col } from 'react-materialize';

export default class Hello extends React.Component {
    constructor(...args) {
        super(...args);

        this.getContent = this.getContent.bind(this);
    }

    getContent() {
        return (
            <Card>
                Hej
            </Card>
        )
    }

    render() {
        return (
            <Row>
                <Col s={12} className="">
                    {this.getContent()}
                </Col>
            </Row>
        );
    }
}
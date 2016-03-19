import React from 'react';
import { Button, Card, Row, Col } from 'react-materialize';

export default class TrackerCard extends React.Component {
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
}

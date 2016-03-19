import React from 'react';
import { Button, Card, CardTitle, Row, Col } from 'react-materialize';

export default class TrackerCard extends React.Component {
    constructor(...args) {
        super(...args);
    }

    render() {
        let tracker = this.props.tracker;
        return (
            <Card header={<CardTitle image={tracker.img_src}>{tracker.name}</CardTitle>}>
                {tracker.query_string}
            </Card>
        )
    }
}

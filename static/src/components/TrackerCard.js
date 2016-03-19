import React from 'react';
import { Button, Card, CardTitle, Row, Col } from 'react-materialize';

let getTrackerForId = id => {
    switch (id) {
        case 0:
            return {
                name: 'iMac',
                min_price: 5200,
                max_price: 7200,
                query_string: 'iMac display',
                img_src: '//mac-technical-support.com/wp-content/uploads/2015/12/imac-error-support.jpg'
            };
        case 1:
            return {
                name: 'MacBook',
                min_price: 1600,
                max_price: 2100,
                query_string: 'MacBookPro 12\'',
                img_src: '//tctechcrunch2011.files.wordpress.com/2015/04/macbook-front.jpg?w=1279&h=727&crop=1'
            }
    }
};

export default class TrackerCard extends React.Component {
    constructor(...args) {
        super(...args);
    }

    render() {
        let tracker = getTrackerForId(this.props.id);
        return (
            <Card header={<CardTitle image={tracker.img_src}>{tracker.name}</CardTitle>}>
                {tracker.query_string}
            </Card>
        )
    }
}

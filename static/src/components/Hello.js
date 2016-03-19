import React from 'react';
import TrackerCard from './TrackerCard';
import { Button, Card, Col, Footer, Navbar, NavItem, Row } from 'react-materialize';

export default class Hello extends React.Component {
    constructor(...args) {
        super(...args);

        this.getContent = this.getContent.bind(this);
    }

    getContent() {
        return (
            <div>
                <TrackerCard id={0} />
                <TrackerCard id={1} />
            </div>
        )
    }

    render() {
        return (
            <div>
                <Navbar brand="Sambastic" right>
                    <NavItem href='#'>Refresh</NavItem>
                </Navbar>
                <div className="container">
                    <Row>
                        <Col s={6} className="">
                            <TrackerCard id={0} />
                        </Col>
                        <Col s={6} className="">
                            <TrackerCard id={1} />
                        </Col>
                    </Row>
                </div>
                <Footer copyrights="&copy; 2016 Sambastic"
                        moreLinks={
                            <a className="grey-text text-lighten-4 right" href="#!">See our blog</a>
                        }
                        links={
                            <ul>
                              <li><a className="grey-text text-lighten-3" href="//allegro.pl">Sponsor</a></li>
                              <li><a className="grey-text text-lighten-3" href="//allegro.tech/braincode/">Braincode 2016</a></li>
                              <li><a className="grey-text text-lighten-3" href="//allegro.pl">allegro.pl</a></li>
                            </ul>
                        }
                        className='example'>
                    <h5 className="white-text">Pricemize</h5>
                    <p className="grey-text text-lighten-4">Find best deals without effort</p>
                </Footer>
            </div>
        );
    }
}
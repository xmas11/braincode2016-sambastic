import React from 'react';
import { fetchTrackers } from '../actions/actions';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import TrackerCard from './TrackerCard';
import { Button, Card, Col, Footer, Navbar, NavItem, Row } from 'react-materialize';

let tfi = id => {
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

class Hello extends React.Component {
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
        console.log(this.props.state);
        return (
            <div>
                <Navbar brand="Sambastic" right>
                    <NavItem>
                        <Button onClick={this.props.onClick}>
                            Click me!
                        </Button>
                    </NavItem>
                </Navbar>
                <div className="container">
                    <Row>
                        <Col s={6} className="">
                            <TrackerCard tracker={tfi(0)}/>
                        </Col>
                        <Col s={6} className="">
                            <TrackerCard tracker={tfi(1)} />
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

const mapStateToProps = state => ({
    state: state
});

const mapDispatchToProps = dispatch => ({
    onClick: () => dispatch(fetchTrackers())
});

export default connect(mapStateToProps, mapDispatchToProps)(Hello);
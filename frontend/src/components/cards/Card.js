import React, { Component } from 'react';
import { Button,Jumbotron,Row, Col } from 'reactstrap';

const Card = () => {
  return (
    <Jumbotron className="custom">
    <Row>
     <Col>
       <article class="mw5 bg-white br3 pa2 ma3 pa4-ns mv3 ba b--black-10 shadow-5">
       <div class="tc">
         <h1 class="f3 mb2">UPSC</h1>
         <h2 class="f5 fw4 gray mt0">Jobs Available(2)</h2>
       </div>
       </article>
     </Col>
   </Row>
    </Jumbotron>
  )
}

export default Card;

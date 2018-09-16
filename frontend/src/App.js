import React, { Component } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import Route from 'react-router-dom/Route';
import { Button,Jumbotron,Row, Col } from 'reactstrap';
import 'tachyons';
import './app.css'
import CardList from 'components/cardList/CardList';

class App extends Component {

  componentDidMount() {
   fetch('https://jsonplaceholder.typicode.com/users')
   .then(response => response.json())
   .then(users => this.setState({ robots: users }))
    console.log(response.json())
 }


  render() {
    return (
      <div>
        <CardList />
      </div>
    );
  }
}

export default App;

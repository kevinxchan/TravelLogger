import React from 'react';
import { Link, NavLink, Route, Switch } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap';
import githubImg from './assets/github-circle.png';
import Home from './components/Home';
import Login from './components/Login';
import SignUp from './components/SignUp';
import About from './components/About';
import './App.css';

class App extends React.Component {
  render() {
    const personalWebsite = 'https://www.github.com/kevinxchan';

    return (
      <div>
        <Navbar bg={"light"}>
          <Navbar.Brand as={Link} to={"/"}>Travel Logger</Navbar.Brand>
            <Nav className={"ml-auto"}>
              <Nav.Link as={NavLink} to={"/login"}>Login</Nav.Link>
              <Nav.Link as={NavLink} to={"/signup"}>Sign up</Nav.Link>
              <Nav.Link as={NavLink} to={"/about"}>About</Nav.Link>
            </Nav>
          <a href={personalWebsite}><img src={githubImg} /> </a>
         </Navbar>

        <Switch>
          <Route exact={true} path={"/"} component={Home}/>
          <Route path={"/login"} component={Login}/>
          <Route path={"/signup"} component={SignUp}/>
          <Route path={"/about"} component={About}/>
        </Switch>

      </div>
    )
  }
}

export default App;

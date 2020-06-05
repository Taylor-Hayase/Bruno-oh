import React from "react";
import { Nav, Navbar, Form, FormControl } from "react-bootstrap";
import { NavLink } from "react-router-dom";

const Navigation = () => {
  return (
    <Navbar expand="lg">
      <Navbar.Brand href="/">JustDoIt</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="ml-auto">
          <Nav.Item>
            <Nav.Link href="/">Login</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/home">Home</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/about">About</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/contact">Contact</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/list">List</Nav.Link>
          </Nav.Item>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
  /*  return (
    <div>
      <NavLink to="/"> Login </NavLink>
      <NavLink to="/home"> Home </NavLink>
      <NavLink to="/about"> About </NavLink>
      <NavLink to="/contact"> Contact </NavLink>
      <NavLink to="/list"> Lists </NavLink>
    </div>
  );*/
};

export default Navigation;

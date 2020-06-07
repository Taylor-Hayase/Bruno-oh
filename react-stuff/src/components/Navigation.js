import React from "react";
import { Nav, Navbar } from "react-bootstrap";

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
};

export default Navigation;

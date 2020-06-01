import React from "react";

import { NavLink } from "react-router-dom";

const Navigation = () => {
  return (
    <div>
      <NavLink to="/"> Login </NavLink>
      <NavLink to="/home"> Home </NavLink>
      <NavLink to="/about"> About </NavLink>
      <NavLink to="/contact"> Contact </NavLink>
      <NavLink to="/list"> List </NavLink>
    </div>
  );
};

export default Navigation;

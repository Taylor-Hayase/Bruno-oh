import React, { Component } from "react";
import { Redirect } from "react-router-dom";
import MuiThemeProvider from "material-ui/styles/MuiThemeProvider";
import AppBar from "material-ui/AppBar";
import RaisedButton from "material-ui/RaisedButton";
import TextField from "material-ui/TextField";
//import DropDownMenu from 'material-ui/DropDownMenu';
//import MenuItem from 'material-ui/MenuItem';
import axios from "axios";

class Login extends Component {
  constructor(props) {
    super(props);
    var localloginComponent = [];
    localloginComponent.push(
      <MuiThemeProvider key={"theme"}>
        <div>
          <TextField
            hintText="Enter your username"
            floatingLabelText="Username"
            onChange={(event, newValue) =>
              this.setState({ username: newValue })
            }
          />
          <br />
          <TextField
            type="password"
            hintText="Enter your Password"
            floatingLabelText="Password"
            onChange={(event, newValue) =>
              this.setState({ password: newValue })
            }
          />
          <br />
          <RaisedButton
            label="Submit"
            primary={true}
            style={style}
            onClick={(event) => this.handleClick(event)}
          />
        </div>
      </MuiThemeProvider>
    );
    this.state = {
      username: "",
      password: "",
      menuValue: 1,
      loginsucc: false,
      loginComponent: localloginComponent,
    };
    this.onSubmit = this.onSubmit.bind(this);
  }
  componentWillMount() {
    // console.log("willmount prop values",this.props);
    var localloginComponent = [];
    localloginComponent.push(
      <MuiThemeProvider key={"start"}>
        <div>
          <TextField
            hintText="Enter your username"
            floatingLabelText="Username"
            onChange={(event, newValue) =>
              this.setState({ username: newValue })
            }
          />
          <br />
          <TextField
            type="password"
            hintText="Enter your Password"
            floatingLabelText="Password"
            onChange={(event, newValue) =>
              this.setState({ password: newValue })
            }
          />
          <br />
          <RaisedButton
            label="Submit"
            primary={true}
            style={style}
            onClick={(event) => this.handleClick(event)}
          />
        </div>
      </MuiThemeProvider>
    );
    this.setState({ menuValue: 1, loginComponent: localloginComponent });
  }
  handleClick(event) {
    var self = this;
    var payload = {
      username: this.state.username,
      password: this.state.password,
    };
    axios
      .post("http://localhost:5000/", payload)
      .then(function (response) {
        console.log(response);
        if (response.status === 200) {
          console.log("Login successful");
          //here we retrieve the _id from response to save
          window.user_id = response.data._id;
          self.setState({ loginsucc: true });
        } else if (response.status === 204) {
          console.log("Username password do not match");
          alert(response.data.success);
        } else {
          console.log("Username does not exists");
          alert("Username does not exist");
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  handleMenuChange(value) {
    console.log("menuvalue", value);
    var localloginComponent = [];
    if (value === 1) {
      localloginComponent.push(
        <MuiThemeProvider key={"menu"}>
          <div>
            <TextField
              hintText="Enter your username"
              floatingLabelText="Username"
              onChange={(event, newValue) =>
                this.setState({ username: newValue })
              }
            />
            <br />
            <TextField
              type="password"
              hintText="Enter your Password"
              floatingLabelText="Password"
              onChange={(event, newValue) =>
                this.setState({ password: newValue })
              }
            />
            <br />
            <RaisedButton
              label="Submit"
              primary={true}
              style={style}
              onClick={(event) => this.handleClick(event)}
            />
          </div>
        </MuiThemeProvider>
      );
    }
    this.setState({ menuValue: value, loginComponent: localloginComponent });
  }
  render() {
    if (this.state.loginsucc === true) {
      return <Redirect to="/home/" />;
    }
    return (
      <div>
        <MuiThemeProvider>
          <AppBar title="Login" />
        </MuiThemeProvider>
        {this.state.loginComponent}
      </div>
    );
  }
  onSubmit = () => {
    return <Redirect to="/home" />;
  };
}

const style = {
  margin: 15,
};

export default Login;

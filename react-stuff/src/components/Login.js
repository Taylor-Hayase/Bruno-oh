import React, { Component } from "react";
import MuiThemeProvider from "material-ui/styles/MuiThemeProvider";
import AppBar from "material-ui/AppBar";
import RaisedButton from "material-ui/RaisedButton";
import TextField from "material-ui/TextField";
//import DropDownMenu from 'material-ui/DropDownMenu';
//import MenuItem from 'material-ui/MenuItem';
import axios from "axios";
import Home from "./Home";
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
      loginComponent: localloginComponent,
    };
  }
  componentWillMount() {
    // console.log("willmount prop values",this.props);
    var localloginComponent = [];
    console.log("in login componentWillMount");
    localloginComponent.push(
      <MuiThemeProvider>
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
        if (response.data.code === 200) {
          console.log("Login successful");
          var uploadScreen = [];
          uploadScreen.push(<Home appContext={self.props.appContext} />);
          self.props.appContext.setState({
            loginPage: [],
            uploadScreen: uploadScreen,
          });
        } else if (response.data.code === 204) {
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
        <MuiThemeProvider>
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
    return (
      <div>
        <MuiThemeProvider>
          <AppBar title="Login" />
        </MuiThemeProvider>
        {this.state.loginComponent}
      </div>
    );
  }
}

const style = {
  margin: 15,
};

export default Login;

import React, { Component } from "react";
import MuiThemeProvider from "material-ui/styles/MuiThemeProvider";
import AppBar from "material-ui/AppBar";
import RaisedButton from "material-ui/RaisedButton";
import TextField from "material-ui/TextField";
import axios from "axios";
import { Redirect } from "react-router-dom";

class Register extends Component {
  constructor(props) {
    super(props);
    this.state = {
      first_name: "",
      last_name: "",
      username: "",
      password: "",
      loginsucc: false,
    };
  }

  handleClick(event) {
    var apiBaseUrl = "http://localhost:5000";
    // console.log("values in register handler");
    var self = this;
    //To be done:check for empty values before hitting submit
    if (
      this.state.first_name.length > 0 &&
      this.state.last_name.length > 0 &&
      this.state.username.length > 0 &&
      this.state.password.length > 0
    ) {
      var payload = {
        first_name: this.state.first_name,
        last_name: this.state.last_name,
        username: this.state.username,
        password: this.state.password,
      };
      console.log(payload);
      axios
        .post(apiBaseUrl + "/signup", payload)
        .then(function (response) {
          console.log(response);
          if (response.status === 200) {
            var loginscreen = [];
            console.log("registration successful");
            self.setState({ loginsucc: true });
            console.log(response.data._id);
            window.user_id = response.data._id;
            console.log(window.user_id);
            var loginmessage = "Not Registered yet. Go to registration";
            self.props.parentContext.setState({
              loginscreen: loginscreen,
              loginmessage: loginmessage,
              buttonLabel: "Register",
              isLogin: true,
            });
          } else {
            console.log("some error ocurred", response.data.code);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    } else {
      alert("Input field value is missing");
    }
  }
  render() {
    // console.log("props",this.props);
    if (this.state.loginsucc === true) {
      return <Redirect to="/home/" />;
    }
    return (
      <div>
        <MuiThemeProvider>
          <div>
            <AppBar title="Register" />
            <TextField
              hintText="Enter your First Name"
              floatingLabelText="First Name"
              onChange={(event, newValue) =>
                this.setState({ first_name: newValue })
              }
            />
            <br />
            <TextField
              hintText="Enter your Last Name"
              floatingLabelText="Last Name"
              onChange={(event, newValue) =>
                this.setState({ last_name: newValue })
              }
            />
            <br />
            <TextField
              hintText="Enter a username"
              floatingLabelText="Username"
              onChange={(event, newValue) =>
                this.setState({ username: newValue })
              }
            />
            <br />
            <TextField
              type="password"
              hintText="Enter a Password"
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
      </div>
    );
  }
}

const style = {
  margin: 15,
};

export default Register;

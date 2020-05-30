import React, { Component } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Home from "./components/Home";
import About from "./components/About";
import Contact from "./components/Contact";
import Error from "./components/Error";
import Navigation from "./components/Navigation";
import List from "./components/List";
import Loginscreen from "./components/Loginscreen";

class App extends Component {
  /*constructor(props){
    super(props);
    this.state={
      loginPage:[],
      uploadScreen:[]
    }
  }
  componentWillMount(){
    var loginPage =[];
    loginPage.push(<Loginscreen parentContext={this}/>);
    this.setState({
                  loginPage:loginPage
                    })
  } **/

  render() {
    return (
      <BrowserRouter>
        {/*<div className="App">
          {this.state.loginPage}
          {this.state.uploadScreen}
        </div>*/}
        <div>
          <Navigation />
          <Switch>
            <Route path="/" component={Loginscreen} exact />
            <Route path="/about" component={About} />
            <Route path="/contact" component={Contact} />
            <Route path="/list" component={List} />
            <Route component={Error} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;

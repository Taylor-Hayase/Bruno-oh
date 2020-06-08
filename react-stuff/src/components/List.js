import React, { Component } from "react";
import TodoList from "./TodoList";
import axios from "axios";
import "./TodoList.css";
import "./DataStore.js";

class List extends Component {
  constructor(props) {
    super(props);

    this.state = {
      rend: false,
      lists: [],
      numLists: 0,
      idCount: 1,
      user: "",
    };

    this.handleClickNew = this.handleClickNew.bind(this);
    this.handleClickDel = this.handleClickDel.bind(this);
    this.forceUpdateHandler = this.forceUpdateHandler.bind(this);
  }

  forceUpdateHandler() {
    this.forceUpdate();
  }

  handleClickNew() {
    this.setState({
      rend: true,
    });
    var newList = {
      idCount: this.state.idCount,
      lName: "List " + this.state.idCount,
    };
    this.makePostCall(newList);
    this.setState((prevState) => ({
      numLists: prevState.numLists + 1,
    }));
    this.setState({
      lists: [...this.state.lists, "List " + this.state.idCount],
    });
    this.setState((prevState) => ({
      idCount: prevState.idCount + 1,
    }));
    this.forceUpdateHandler();
  }
  makePostCall(newList) {
    var html = "http://localhost:5000/list/";
    return axios
      .post(html, newList)
      .then(function (response) {
        return response;
      })
      .catch(function (error) {
        return false;
      });
  }

  handleClickDel() {
    this.makeDeleteCall();
    this.setState((prevState) => ({
      numLists: prevState.numLists - 1,
    }));
    this.state.lists.shift();

    if (this.state.numLists === 0) {
      this.setState({
        rend: false,
      });
    }
    this.forceUpdate();
  }

  makeDeleteCall(key) {
    //for item
    var html = "http://localhost:5000/list/";
    return axios
      .delete(html.concat(key))
      .then(function (response) {
        return response;
      })
      .catch(function (error) {
        return false;
      });
  }

  componentDidMount() {
    this.setState({ user: window.user_id });
    //once get multiple lists on backend, will retrieve any lists connected to user
    var html = "http://localhost:5000/list/";
    axios
      .get(html)
      .then((res) => {
        const listsFromData = res.data;
        this.setState({ numLists: listsFromData.numLists });
        this.setState({ idCount: listsFromData.idCount });
        this.setState({ lists: listsFromData.lists });
        if (this.state.numLists > 0) {
          //copy over lists to lists state
          this.setState({ lists: listsFromData.lists });
          this.setState({ rend: true });
        } else {
          //nothing
        }
      })
      .catch(function (error) {
        //Not handling the error. Just logging into the console.
        console.log(error);
      });
  }

  render() {
    return (
      <div>
        <h2>Your Lists</h2>

        {this.state.lists.map((lname) => (
          <TodoList
            name={lname}
            key={lname}
            id={lname.substr(-1)}
            rend={this.state.rend}
          />
        ))}

        <button className="button" onClick={this.handleClickNew}>
          {"Make new list"}
        </button>
      </div>
    );
  }
}

export default List;

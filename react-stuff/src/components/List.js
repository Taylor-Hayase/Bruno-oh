import React, { Component } from "react";
import TodoList from "./TodoList";
import axios from "axios";
import "./TodoList.css";
import "./DataStore.js";

//fix globals
class List extends Component {
  constructor(props) {
    super(props);

    this.state = {
      rend: false,
      lists: [],
      numLists: 0,
      idCount: 1,
      user: "",
      //need to update user from login
    };

    this.handleClickNew = this.handleClickNew.bind(this);
    this.handleClickDel = this.handleClickDel.bind(this);
    this.forceUpdateHandler = this.forceUpdateHandler.bind(this);
  }
  forceUpdateHandler() {
    this.forceUpdate();
  }
  //need to create functions to call backend make post/delete calls
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
    console.log(this.state.numLists);
  }
  makePostCall(newList) {
    //html is now ... this.state.user + list + this.props.id
    //for list
    var html = "http://localhost:5000/list/";
    console.log(newList);
    return axios
      .post(html, newList)
      .then(function (response) {
        console.log(response);
        return response;
      })
      .catch(function (error) {
        console.log(error);
        return false;
      });
  }

  //never used delete button is on TodoList for lists
  handleClickDel() {
    console.log("clicked");
    console.log("here");
    //need a way to get the listId that was clicked on
    this.makeDeleteCall();
    this.setState((prevState) => ({
      numLists: prevState.numLists - 1,
    }));
    console.log(this.state.numLists);
    this.state.lists.shift();

    if (this.state.numLists === 0) {
      this.setState({
        rend: false,
      });
    }
    this.forceUpdate();
    console.log(this.state.lists);
  }
  makeDeleteCall(key) {
    //for item
    var html = "http://localhost:5000/list/";
    return axios
      .delete(html.concat(key))
      .then(function (response) {
        console.log(response);
        return response;
      })
      .catch(function (error) {
        console.log(error);
        return false;
      });
  }

  componentDidMount() {
    this.setState({ user: window.user_id });
    if (this.state.user !== "") {
      console.log("A logged in user");
    } else {
      console.log("A guest user");
    }
    //once get multiple lists on backend, will retrieve any lists connected to user
    var html = "http://localhost:5000/list/";
    axios
      .get(html)
      .then((res) => {
        const listsFromData = res.data;
        console.log(listsFromData);
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

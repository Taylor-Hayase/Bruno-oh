import React, { Component } from "react";
import TodoList from "./TodoList";

class List extends Component {
  constructor(props) {
    super(props);

    this.state = {
      rend: false,
      lists: [],
      numLists: 0,
      idCount: 1,
    };

    this.handleClickNew = this.handleClickNew.bind(this);
    this.handleClickDel = this.handleClickDel.bind(this);
  }

  handleClickNew() {
    this.setState({
      rend: true,
    });
    this.setState((prevState) => ({
      numLists: prevState.numLists + 1,
    }));
    this.setState({
      lists: [...this.state.lists, "List " + this.state.idCount],
    });
    this.setState((prevState) => ({
      idCount: prevState.idCount + 1,
    }));
    console.log(this.state.numLists);
  }

  handleClickDel() {
    console.log("clicked");
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

  render() {
    return (
      <div>
        <h1>User 1: Lists</h1>

        <button onClick={this.handleClickNew}>{"Make new list"}</button>
        <button onClick={this.handleClickDel}>{"Delete top list"}</button>

        {this.state.lists.map((lname) => (
          <TodoList
            name={lname}
            key={lname}
            id={lname.substr(-1)}
            rend={this.state.rend}
          />
        ))}
      </div>
    );
  }
}

export default List;

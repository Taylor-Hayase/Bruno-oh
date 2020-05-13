import React, { Component } from "react";
import TodoItems from "./TodoItems";
import "./TodoList.css";
import axios from "axios";

class TodoList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      items: [],
    };

    this.addItem = this.addItem.bind(this);
    this.deleteItem = this.deleteItem.bind(this);
  }
  addItem(e) {
    if (this._inputElement.value !== "") {
      var newItem = {
        text: this._inputElement.value,
        key: Date.now(),
      };
      this.makePostCall(newItem).then((callResult) => {
        this.setState((prevState) => {
          return {
            items: prevState.items.concat(newItem),
          };
        });
        this._inputElement.value = "";
      });
      console.log(this.state.items);
      e.preventDefault();
    }
  }
  makePostCall(item) {
    return axios
      .post("http://localhost:5000/list/1", item)
      .then(function (response) {
        console.log(response);
        return response;
      })
      .catch(function (error) {
        console.log(error);
        return false;
      });
  }

  deleteItem(key) {
    var filteredItems = this.state.items.filter(function (item) {
      return item.key !== key;
    });
    this.setState({
      items: filteredItems,
    });
  }
  componentDidMount() {
    axios
      .get("http://localhost:5000/list/1")
      .then((res) => {
        const items = res.data.users_list;
        this.setState({ items });
      })
      .catch(function (error) {
        //Not handling the error. Just logging into the console.
        console.log(error);
      });
  }

  render() {
    return (
      <div className="todoListMain">
        <div className="header">
          <form onSubmit={this.addItem}>
            <input
              ref={(a) => (this._inputElement = a)}
              placeholder="enter task"
            ></input>
            <button type="submit">Add</button>
          </form>
        </div>
        <TodoItems entries={this.state.items} delete={this.deleteItem} />
      </div>
    );
  }
}

export default TodoList;

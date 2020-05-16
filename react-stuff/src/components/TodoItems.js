import React, { Component } from "react";
import axios from "axios";

class TodoItems extends Component {
  constructor(props) {
    super(props);
    this.createTasks = this.createTasks.bind(this);
    this.forceUpdateHandler = this.forceUpdateHandler.bind(this);
  }

  delete(key) {
    this.makeDeleteCall(key).then((callResult) => {
      this.props.delete(key);
    });
  }
  forceUpdateHandler() {
    this.forceUpdate();
  }
  handleClick = (key) => {
    var i;
    for (i = 0; i < this.props.entries.length; i++) {
      if (this.props.entries[i].key === key) {
        if (this.props.entries[i].checked === true) {
          this.props.entries[i].checked = false;
        } else {
          this.props.entries[i].checked = true;
        }
      }
    }
    this.forceUpdateHandler();
  };
  createTasks(item) {
    if (item.checked === true) {
      return (
        <div>
          <li
            onClick={() => this.handleClick(item.key)}
            className="checked"
            key={item.key}
          >
            {item.text}
          </li>
          <button
            onClick={() => this.delete(item.key)}
            className="btn btn-lg btn-outline-danger ml-4"
          >
            Remove
          </button>
        </div>
      );
    } else {
      return (
        <div>
          <li onClick={() => this.handleClick(item.key)} key={item.key}>
            {item.text}
          </li>
          <button
            onClick={() => this.delete(item.key)}
            className="btn btn-lg btn-outline-danger ml-4"
          >
            Remove
          </button>
        </div>
      );
    }
  }
  makeDeleteCall(key) {
    return axios
      .delete("http://localhost:5000/list/1/".concat(key))
      .then(function (response) {
        console.log(response);
        return response;
      })
      .catch(function (error) {
        console.log(error);
        return false;
      });
  }

  render() {
    var todoEntries = this.props.entries;
    var listItems = todoEntries.map(this.createTasks);

    return <ul className="theList">{listItems}</ul>;
  }
}

export default TodoItems;

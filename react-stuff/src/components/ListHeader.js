import React from "react";
import TodoList from "./TodoList";

class ListHeader extends React.Component {
  state = {
    rend: false,
  };

  handleClick = () => {
    this.setState({
      rend: !this.state.rend,
    });
  };

  render() {
    return (
      <div>
        <button onClick={this.handleClick}>
          {this.state.rend ? "Delete List" : "New List"}
        </button>
        {this.state.rend && <h1>List #1</h1> && <TodoList />}
      </div>
    );
  }
}
export default ListHeader;

import React, { Component } from "react";
import TodoList from "./TodoList";

const lists = [
	"List 1"
];


class List extends Component {

	constructor(props) {
		super(props);

		this.state = {
			rend: false,
		}

		this.handleClickNew = this.handleClickNew.bind(this);
		this.handleClickDel = this.handleClickDel.bind(this);
	}

	handleClickNew() {
		console.log("clicked")
		this.setState({
      		rend: true,
    	});
	}

	handleClickDel() {
		console.log("clicked")
		this.setState({
      		rend: false,
    	});
	}

	render() {
  		return (
    		<div>
      		<h1>User 1: Lists</h1>

			<button onClick={this.handleClickNew}>
          		{"Make new list"}
        	</button>
        	<button onClick={this.handleClickDel}>
          		{"Delete top list"}
        	</button>
      		{lists.map(lname => (
      			<TodoList name={lname} key={lname} rend={this.state.rend}/>))}
    		</div>
  		);
	};
}

export default List;

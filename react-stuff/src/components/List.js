import React, { Component } from "react";
import TodoList from "./TodoList";
import "./TodoList.css";

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

  /*componentDidMount() {
    this.setState({ user: window.user_id });
    if (this.state.user !== "") {
      console.log("A logged in user");
    } else {
      console.log("A guest user");
    }
    //once get multiple lists on backend, will retrieve any lists connected to user
    var html = "http://localhost:5000/list/" + this.props.id;
    axios
      .get(html)
      .then((res) => {
        const listsFromData = res.data.users_list;
        this.setState({ numLists : listsFromData.length });
        if (this.state.numLists > 0) {
          //copy over lists to lists state
          this.setStare({ lists: listsFromData });
        } else {
          //nothing
        }
      })
      .catch(function (error) {
        //Not handling the error. Just logging into the console.
        console.log(error);
      });
  }*/

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

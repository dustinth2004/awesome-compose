import React from "react";
import axios from "axios";
import "./App.scss";
import AddTodo from "./components/AddTodo";
import TodoList from "./components/TodoList";

/**
 * The main application component.
 * @extends React.Component
 */
export default class App extends React.Component {
  /**
   * Creates an instance of App.
   * @param {object} props - The props for the component.
   */
  constructor(props) {
    super(props);

    this.state = {
      todos: [],
    };
  }

  /**
   * Fetches the todos from the API when the component mounts.
   */
  componentDidMount() {
    axios
      .get("/api")
      .then((response) => {
        this.setState({
          todos: response.data.data,
        });
      })
      .catch((e) => console.log("Error : ", e));
  }

  /**
   * Adds a new todo to the list.
   * @param {string} value - The text of the new todo.
   */
  handleAddTodo = (value) => {
    axios
      .post("/api/todos", { text: value })
      .then(() => {
        this.setState({
          todos: [...this.state.todos, { text: value }],
        });
      })
      .catch((e) => console.log("Error : ", e));
  };

  render() {
    return (
      <div className="App container">
        <div className="container-fluid">
          <div className="row">
            <div className="col-xs-12 col-sm-8 col-md-8 offset-md-2">
              <h1>Todos</h1>
              <div className="todo-app">
                <AddTodo handleAddTodo={this.handleAddTodo} />
                <TodoList todos={this.state.todos} />
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

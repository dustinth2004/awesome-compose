import React from "react";

/**
 * A component that displays a list of todos.
 * @extends React.Component
 */
export default class TodoList extends React.Component {
  /**
   * Creates an instance of TodoList.
   * @param {object} props - The props for the component.
   */
  constructor(props) {
    super(props);

    this.state = {
      activeIndex: 0,
    };
  }

  /**
   * Sets the active todo item.
   * @param {number} index - The index of the todo item to set as active.
   */
  handleActive(index) {
    this.setState({
      activeIndex: index,
    });
  }

  /**
   * Renders a list of todos.
   * @param {Array<object>} todos - The list of todos to render.
   * @returns {JSX.Element} The rendered list of todos.
   */
  renderTodos(todos) {
    return (
      <ul className="list-group">
        {todos.map((todo, i) => (
          <li
            className={
              "list-group-item cursor-pointer " +
              (i === this.state.activeIndex ? "active" : "")
            }
            key={i}
            onClick={() => {
              this.handleActive(i);
            }}
          >
            {todo.text}
          </li>
        ))}
      </ul>
    );
  }

  /**
   * Renders the component.
   *
   * @returns {JSX.Element} The rendered component.
   */
  render() {
    let { todos } = this.props;
    return todos.length > 0 ? (
      this.renderTodos(todos)
    ) : (
      <div className="alert alert-primary" role="alert">
        No Todos to display
      </div>
    );
  }
}

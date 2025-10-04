import React from "react";

/**
 * A component that provides a form to add a new todo.
 * @extends React.Component
 */
export default class AddTodo extends React.Component {
  /**
   * Handles the form submission.
   * @param {object} e - The form submission event.
   */
  handleSubmit = (e) => {
    e.preventDefault();
    const { value } = e.target.elements.value;
    if (value.length > 0) {
      this.props.handleAddTodo(value);
      e.target.reset();
    }
  };

  render() {
    return (
      <form
        noValidate
        onSubmit={this.handleSubmit}
        className="new-todo form-group"
      >
        <input
          type="text"
          name="value"
          required
          minLength={1}
          className="form-control"
        />
        <button className="btn btn-primary" type="submit">
          Add Todo
        </button>
      </form>
    );
  }
}

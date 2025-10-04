package com.company.project.entity;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 * Represents a greeting entity.
 */
@Entity
@Table(name = "GREETINGS")
public class Greeting {

    @Id
    private int id;
    private String name;

    /**
     * Default constructor.
     */
    public Greeting() {
    }

    /**
     * Creates a new greeting with the given name.
     *
     * @param name The name for the greeting.
     */
    public Greeting(String name) {
        this.name = name;
    }

    /**
     * Creates a new greeting with the given id and name.
     *
     * @param id   The id for the greeting.
     * @param name The name for the greeting.
     */
    public Greeting(int id, String name) {
        this.id = id;
        this.name = name;
    }

    /**
     * Gets the id of the greeting.
     *
     * @return The id of the greeting.
     */
    public int getId() {
        return id;
    }

    /**
     * Sets the id of the greeting.
     *
     * @param id The id of the greeting.
     */
    public void setId(int id) {
        this.id = id;
    }

    /**
     * Gets the name of the greeting.
     *
     * @return The name of the greeting.
     */
    public String getName() {
        return name;
    }

    /**
     * Sets the name of the greeting.
     *
     * @param name The name of the greeting.
     */
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Greeting greeting = (Greeting) o;

        return name.equals(greeting.name);
    }

    @Override
    public int hashCode() {
        return name.hashCode();
    }
}

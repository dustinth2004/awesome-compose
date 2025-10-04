package com.company.project;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

/**
 * The main application class for the Spring Boot application.
 */
@SpringBootApplication
@EnableAutoConfiguration
@ComponentScan(basePackages = {"com.company.project"})
public class Application {

    /**
     * The main entry point for the application.
     *
     * @param args The command line arguments.
     */
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

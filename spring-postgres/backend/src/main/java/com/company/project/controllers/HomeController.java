package com.company.project.controllers;

import com.company.project.entity.Greeting;
import com.company.project.repository.GreetingRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

/**
 * The main controller for the application.
 */
@Controller
public class HomeController {

    @Autowired
    private GreetingRepository repository;

    /**
     * Shows the home page.
     *
     * @param name  The name to display.
     * @param model The model to add attributes to.
     * @return The name of the view to render.
     */
    @GetMapping("/")
    public String showHome(String name, Model model) {
        Greeting dockerGreeting = repository.findById(1).orElse(new Greeting("Not Found 😕"));
        model = model.addAttribute("name", dockerGreeting.getName());
        return "home";
    }

}

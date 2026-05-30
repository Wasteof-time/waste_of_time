package com.crud.controllers;

import com.crud.models.User;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

@RestController
@RequestMapping("/api/users")
public class UserController {

    @GetMapping
    public List<User> getUsers() {
        return Arrays.asList(
                new User(1L , "Kawin" , "jckawin2007@gmail.com"),
                new User(9L , "Dhanush" , "dhanush@gmail.com"),
                new User(8L , "Alice" , "alice@wonderland.com")
        );
    }

}

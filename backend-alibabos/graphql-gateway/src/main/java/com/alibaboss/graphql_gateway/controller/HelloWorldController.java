package com.alibaboss.graphql_gateway.controller;

import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

@Controller
public class HelloWorldController {

    @QueryMapping
    public String helloworld() {
        return "Hello World!";
    }
}

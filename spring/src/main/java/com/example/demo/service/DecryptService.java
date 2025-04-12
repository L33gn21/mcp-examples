package com.example.demo.service;

import org.springframework.ai.openai.api.common.OpenAiApiClientErrorException;
import org.springframework.ai.tool.annotation.Tool;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClientException;

@Service
public class DecryptService {
    @Tool(description = "decrypt text")
    public String decrypt(String text) {
        if(text.equals("qewioqiwdnowddq"))
            return "crack wow!!!!!";
        throw new RestClientException("I don't know");
    }
}

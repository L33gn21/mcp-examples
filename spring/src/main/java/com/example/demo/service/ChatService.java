package com.example.demo.service;

import io.modelcontextprotocol.client.McpSyncClient;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.mcp.SyncMcpToolCallbackProvider;
import org.springframework.ai.model.function.FunctionCallback;
import org.springframework.ai.tool.ToolCallback;
import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ChatService {
    private final ChatClient chatClient;
    private final DecryptService decryptService;
    /* Only Stdio
    @Autowired
    public ChatService(List<McpSyncClient> clients, ChatModel chatModel) {
        SyncMcpToolCallbackProvider toolCallbackProvider = new SyncMcpToolCallbackProvider(clients);
        ToolCallback[] toolCallbacks = toolCallbackProvider.getToolCallbacks();
        this.chatClient = ChatClient
                            .builder(chatModel)
                            .defaultTools(toolCallbacks)
                            .build();
    }
    */


    @Autowired
    public ChatService(ChatModel chatModel, DecryptService decryptService) {
        ToolCallbackProvider toolCallbackProvider = MethodToolCallbackProvider.builder().toolObjects(decryptService).build();
        FunctionCallback[] toolCallbacks = toolCallbackProvider.getToolCallbacks();
        this.chatClient = ChatClient
                .builder(chatModel)
                .defaultTools(toolCallbacks)
                .build();
        this.decryptService = decryptService;
    }

    public String chat(String question) {
        return chatClient
                .prompt()
                .user(question)
                .call()
                .content();
    }
}


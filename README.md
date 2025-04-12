## 1. Python 구현
Python으로 구현된 MCP 예제입니다.

### Python OpenAI API 키 설정
- OpenAI API 키 설정이 필요합니다. (`_mcp_client.py`에서 설정)

### Python MCP 서버 설정
`mcp.json`:
```json
{
    "mcpServers": {
      "mcp-test": {
        "command": "{python_path}",
        "args": ["{_mcp_server.py path (relative path allowed)}"]
      }
    }
}
```

### Python 버전 실행하기
- Python 3.x

1. Python 의존성 설치:
```bash
pip install -r requirements.txt
```
2. MCP Client 실행:
```bash
python _mcp_client.py
```
3. 웹 브라우저에서 `http://localhost:8000` 접속



## 2. Spring 구현
Spring AI를 사용한 MCP 예제입니다.

### Spring MCP 설정
Spring AI의 Starter 통해 구성되며 application.properties에서 커스터마이징 가능합니다.

### Spring OpenAI API 키 설정
- OpenAI API 키 설정 (application.properties에서)

### Spring 버전 실행하기
1. Java 21 설치

2. 프로젝트 빌드 및 실행:
```bash
./gradlew bootRun
```

3. 웹 브라우저에서 `http://localhost:8080` 접속
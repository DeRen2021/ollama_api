# FastAPI Ollama Chat API (Ngrok Branch)

This branch provides a FastAPI wrapper for Ollama or LM Studio chat functionality with public access through ngrok.
This branch is less update and havent optimial for production. Please check the cloudflare branch for a more stable and optimized version.
As cloudflare offer more than one static domian.

(中文：该分支提供了一个使用 FastAPI 封装 Ollama 或者 LM Studio 聊天功能的 API 服务，并通过 ngrok 实现外网访问。)

## Features

- REST API based on FastAPI
- Integration with Ollama LLM
- Public access via ngrok
- Model validation and error handling
- Asynchronous chat processing

(功能特点：
- 基于 FastAPI 的 REST API
- 集成 Ollama 大语言模型
- 使用 ngrok 进行内网穿透
- 支持模型验证和错误处理
- 异步处理聊天请求)

## Requirements

- Python 3.8+
- Ollama service installed and running
- ngrok account and authtoken

(环境要求：
- Python 3.8+
- Ollama 服务已安装并运行
- ngrok 账号和 authtoken)

## Installation

1. Clone the repository and switch to ngrok branch:
```bash
git clone <repository_url>
git checkout ngrok
```

2. Create and activate virtual environment:
```bash
python -m venv ollama_venv
source ollama_venv/bin/activate  # Linux/Mac
# or
.\ollama_venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create `.env` file and add:
```
NGROK_AUTHTOKEN=your_ngrok_authtoken
NGROK_DOMAIN=your_static_domain(if_any)
```

(安装说明：
1. 克隆仓库并切换到 ngrok 分支
2. 创建并激活虚拟环境
3. 安装依赖
4. 配置环境变量，创建 .env 文件)

## Running the Service

1. Ensure Ollama service is running
2. Start the API service:
```bash
python main.py
```

The service will start on `http://localhost:8000` and be exposed via ngrok.

(运行服务：
1. 确保 Ollama 服务正在运行
2. 启动 API 服务
服务将在 `http://localhost:8000` 启动，并通过 ngrok 暴露到公网。)

## API Endpoints

### POST /chat
Send chat request

Request body:
```json
{
    "model": "llama2",  // or other installed models
    "message": "your question"
}
```

Response:
```json
{
    "reply": "model's response"
}
```

### GET /health
Health check endpoint

Response:
```json
{
    "status": "ok"
}
```

(API 端点说明：
1. POST /chat - 发送聊天请求
   - 请求体需包含模型名称和问题
   - 返回模型回答
2. GET /health - 健康检查端点)

## Error Handling

The service includes the following error handling:
- 400: Invalid request or model name
- 504: Request timeout
- 500: Server internal error

Error response format:
```json
{
    "detail": "error message"
}
```

(错误处理：
- 400: 无效的请求或模型名称
- 504: 请求超时
- 500: 服务器内部错误)

## Notes

1. Ensure Ollama service is running before starting the API service
2. Default request timeout is 90 seconds
3. Make sure ngrok authtoken is configured before use

(注意事项：
1. 确保 Ollama 服务在 API 服务启动前已经运行
2. 默认请求超时时间为 90 秒
3. 使用前请确保已配置 ngrok authtoken)

## Development

- `main.py`: Main application entry
- `schemas/`: Request and response model definitions
- `config/`: Configuration files

(开发说明：
- `main.py`: 主应用入口
- `schemas/`: 请求和响应模型定义
- `config/`: 配置文件)

## License

[License Type]

(许可证类型：[待定]) 
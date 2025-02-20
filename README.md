# FastAPI Cloudflare Tunnel Project | FastAPI Cloudflare Tunnel 项目

[English](#english) | [中文](#chinese)

<a name="english"></a>
## English Version

This project provides a FastAPI application that creates public endpoints for either Ollama or LM Studio through Cloudflare Tunnel, allowing secure access to your local LLM services over the internet.

### Features

- Create public API endpoints for either Ollama or LM Studio
- High-performance Web API built with FastAPI
- Secure public access through Cloudflare Tunnel
- Support for both Ollama and LM Studio backends
- Health check and model listing endpoints
- Hot-reload support for development

### Requirements

- Python 3.13+
- pip (Python package manager)
- Cloudflared
- Either Ollama or LM Studio running locally

### Project Structure

```
.
├── config/
│   └── config.py              # Configuration settings
├── llm/
│   ├── ollama_endpoint.py     # Ollama API integration
│   └── lm_studio_endpoint.py  # LM Studio API integration
├── schemas/
│   ├── ollama_scheme.py       # Ollama request/response schemas
│   └── lm_studio_scheme.py    # LM Studio request/response schemas
├── main_ollama.py             # Main FastAPI application for Ollama
├── main_lm_studio.py          # Main FastAPI application for LM Studio
├── requirements.txt           # Python dependencies
└── README.md
```

### Installation

1. Clone the project and create virtual environment:
```bash
git clone <repository-url>
cd <project-directory>
python -m venv fc_venv
source fc_venv/bin/activate  # On Windows: .\fc_venv\Scripts\activate
```

2. Install project dependencies:
```bash
pip install -r requirements.txt
```

3. Install Cloudflared:
```bash
# On macOS
brew install cloudflared

# For other systems, please refer to Cloudflare documentation
# https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation
```

### Configuration

1. Configure your local LLM service:
   - For Ollama: Ensure Ollama is running on http://localhost:11434
   - For LM Studio: Ensure LM Studio is running on http://localhost:1234

2. Configure Cloudflare Tunnel:

   a. Login to Cloudflare:
   ```bash
   cloudflared login
   ```

   b. Create a tunnel:
   ```bash
   cloudflared tunnel create lm_studio_tunnel  # or ollama_tunnel
   ```

   c. Create `cloudflared/my_tunnel.yml`:
   ```yaml
   tunnel: <your-tunnel-id>
   credentials-file: /Users/<username>/.cloudflared/<tunnel-id>.json

   ingress:
     - hostname: your-subdomain.your-domain.com
       service: http://localhost:8000
     - service: http_status:404
   ```

   d. Configure DNS:
   ```bash
   cloudflared tunnel route dns lm_studio_tunnel your-subdomain.your-domain.com
   ```

### Running the Project

1. Start your local LLM service (either Ollama or LM Studio)

2. Start the FastAPI server:
   
   For Ollama:
   ```bash
   uvicorn main_ollama:app --host 0.0.0.0 --port 8000 --reload
   ```
   
   For LM Studio:
   ```bash
   uvicorn main_lm_studio:app --host 0.0.0.0 --port 8000 --reload
   ```

3. Run Cloudflare Tunnel:
   ```bash
   cloudflared tunnel --config cloudflared/my_tunnel.yml run lm_studio_tunnel
   ```

### API Endpoints

- `GET /health`: Health check endpoint
- `GET /models`: List available models
- `POST /chat`: Chat completion endpoint
  ```json
  {
    "model": "model_name",
    "messages": [
      {
        "role": "user",
        "content": "Your message here"
      }
    ]
  }
  ```

### Development Notes

- API documentation available at: `https://your-subdomain.your-domain.com/docs`
- Default port is 8000
- Supports hot-reload in development mode
- SSL/TLS handled by Cloudflare

---

<a name="chinese"></a>
## 中文说明

这是一个使用 FastAPI 框架开发的应用程序，通过 Cloudflare Tunnel 为 Ollama 或 LM Studio 创建公开的 API 端点，实现本地 LLM 服务的安全公网访问。

### 项目特点

- 为 Ollama 或 LM Studio 创建公开 API 端点
- 使用 FastAPI 构建高性能 Web API
- 通过 Cloudflare Tunnel 实现安全的公网访问
- 支持 Ollama 和 LM Studio 两种后端
- 健康检查和模型列表端点
- 支持开发环境热重载

### 环境要求

- Python 3.13+
- pip (Python 包管理器)
- Cloudflared
- 本地运行的 Ollama 或 LM Studio

### 项目结构

```
.
├── config/
│   └── config.py              # 配置设置
├── llm/
│   ├── ollama_endpoint.py     # Ollama API 集成
│   └── lm_studio_endpoint.py  # LM Studio API 集成
├── schemas/
│   ├── ollama_scheme.py       # Ollama 请求/响应模式
│   └── lm_studio_scheme.py    # LM Studio 请求/响应模式
├── main_ollama.py             # Ollama 主应用
├── main_lm_studio.py          # LM Studio 主应用
├── requirements.txt           # Python 依赖
└── README.md
```

### 安装步骤

1. 克隆项目并创建虚拟环境：
```bash
git clone <仓库地址>
cd <项目目录>
python -m venv fc_venv
source fc_venv/bin/activate  # Windows: .\fc_venv\Scripts\activate
```

2. 安装项目依赖：
```bash
pip install -r requirements.txt
```

3. 安装 Cloudflared：
```bash
# macOS
brew install cloudflared

# 其他系统请参考 Cloudflare 文档
# https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation
```

### 配置

1. 配置本地 LLM 服务：
   - Ollama：确保运行在 http://localhost:11434
   - LM Studio：确保运行在 http://localhost:1234

2. 配置 Cloudflare Tunnel：

   a. 登录 Cloudflare：
   ```bash
   cloudflared login
   ```

   b. 创建隧道：
   ```bash
   cloudflared tunnel create lm_studio_tunnel  # 或 ollama_tunnel
   ```

   c. 创建 `cloudflared/my_tunnel.yml`：
   ```yaml
   tunnel: <你的隧道ID>
   credentials-file: /Users/<用户名>/.cloudflared/<隧道ID>.json

   ingress:
     - hostname: your-subdomain.your-domain.com
       service: http://localhost:8000
     - service: http_status:404
   ```

   d. 配置 DNS：
   ```bash
   cloudflared tunnel route dns lm_studio_tunnel your-subdomain.your-domain.com
   ```

### 运行项目

1. 启动本地 LLM 服务（Ollama 或 LM Studio）

2. 启动 FastAPI 服务器：
   
   Ollama：
   ```bash
   uvicorn main_ollama:app --host 0.0.0.0 --port 8000 --reload
   ```
   
   LM Studio：
   ```bash
   uvicorn main_lm_studio:app --host 0.0.0.0 --port 8000 --reload
   ```

3. 运行 Cloudflare Tunnel：
   ```bash
   cloudflared tunnel --config cloudflared/my_tunnel.yml run lm_studio_tunnel
   ```

### API 端点

- `GET /health`：健康检查端点
- `GET /models`：列出可用模型
- `POST /chat`：聊天完成端点
  ```json
  {
    "model": "模型名称",
    "messages": [
      {
        "role": "user",
        "content": "你的消息"
      }
    ]
  }
  ```

### 开发说明

- API 文档访问地址：`https://your-subdomain.your-domain.com/docs`
- 默认端口为 8000
- 开发模式支持热重载
- SSL/TLS 由 Cloudflare 处理 
# FastAPI Cloudflare Tunnel Project | FastAPI Cloudflare Tunnel 项目

[English](#english) | [中文](#chinese)

<a name="english"></a>
## English Version

This is a FastAPI application that creates public endpoints for Ollama and LM Studio through Cloudflare Tunnel. The project architecture is currently in development and will be optimized in future updates.

### Features

- Create public API endpoints for Ollama and LM Studio
- High-performance Web API built with FastAPI
- Secure public access through Cloudflare Tunnel
- Hot-reload support for development environment

### Requirements

- Python 3.x
- pip (Python package manager)
- Cloudflared
- Ollama or LM Studio running locally

### Project Structure

```
.
├── config/
│   └── config.py         # Configuration settings
├── llm/
│   ├── ollama_endpoint.py      # Ollama API integration
│   └── lm_studio_endpoint.py   # LM Studio API integration
├── schemas/
│   ├── ollama_scheme.py        # Ollama request/response schemas
│   └── lm_studio_scheme.py     # LM Studio request/response schemas
├── main_cloudflare.py          # Main FastAPI application
├── requirements.txt            # Python dependencies
└── README.md
```

### Installation

1. Clone the project and create virtual environment:
```bash
git clone <repository-url>
cd <project-directory>
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install project dependencies:
```bash
pip install -r requirements.txt
```

3. Install Cloudflared:
```bash
brew install cloudflared  # On macOS
# For other systems, please refer to Cloudflare documentation
```

### Environment Configuration

1. Create a `.env` file in the project root:
```bash
NGROK_DOMAIN=your-domain
NGROK_AUTHTOKEN=your-auth-token
PUBLIC_PORT=8000
```

2. Configure your local LLM service (Ollama or LM Studio) according to their respective documentation.

### Cloudflare Tunnel Configuration

1. Login to Cloudflare:
```bash
cloudflared login
```

2. Create tunnel:
```bash
cloudflared tunnel create my-tunnel
```

3. Configure tunnel (my_tunnel.yml):
```yaml
tunnel: <your-tunnel-id>
credentials-file: /path/to/your/credentials-file.json

ingress:
  - hostname: yoursubdomain.yourdomain.com
    service: http://localhost:8000
  - service: http_status:404
```

### Running the Project

1. Start your local LLM service (Ollama or LM Studio)

2. Start FastAPI server:
```bash
uvicorn main_cloudflare:app --host 0.0.0.0 --port 8000 --reload
```

3. Run Cloudflare Tunnel:
```bash
cloudflared tunnel --config my_tunnel.yml run my-tunnel
```

### API Endpoints

- `/chat`: POST endpoint for LLM chat interactions
- `/health`: GET endpoint for health check

### Development Notes

- Hot-reload supported in development mode
- API documentation available at: `https://yoursubdomain.yourdomain.com/docs`
- Project runs on port 8000 by default
- Project architecture will be optimized in future updates

---

<a name="chinese"></a>
## 中文说明

这是一个使用 FastAPI 框架开发的应用程序，通过 Cloudflare Tunnel 为 Ollama 和 LM Studio 创建公开的 API 端点。项目架构目前正在开发中，后续会进行优化。

### 项目特点

- 为 Ollama 和 LM Studio 创建公开 API 端点
- 使用 FastAPI 构建高性能 Web API
- 通过 Cloudflare Tunnel 实现安全的公网访问
- 支持热重载的开发环境

### 环境要求

- Python 3.x
- pip (Python 包管理器)
- Cloudflared
- 本地运行的 Ollama 或 LM Studio

### 项目结构

```
.
├── config/
│   └── config.py         # 配置设置
├── llm/
│   ├── ollama_endpoint.py      # Ollama API 集成
│   └── lm_studio_endpoint.py   # LM Studio API 集成
├── schemas/
│   ├── ollama_scheme.py        # Ollama 请求/响应模式
│   └── lm_studio_scheme.py     # LM Studio 请求/响应模式
├── main_cloudflare.py          # 主 FastAPI 应用
├── requirements.txt            # Python 依赖
└── README.md
```

### 安装步骤

1. 克隆项目并创建虚拟环境：
```bash
git clone <仓库地址>
cd <项目目录>
python -m venv venv
source venv/bin/activate  # Windows系统：.\venv\Scripts\activate
```

2. 安装项目依赖：
```bash
pip install -r requirements.txt
```

3. 安装 Cloudflared：
```bash
brew install cloudflared  # macOS系统
# 其他系统请参考 Cloudflare 文档
```

### 环境配置

1. 在项目根目录创建 `.env` 文件：
```bash
NGROK_DOMAIN=你的域名
NGROK_AUTHTOKEN=你的认证令牌
PUBLIC_PORT=8000
```

2. 根据相应文档配置本地 LLM 服务（Ollama 或 LM Studio）。

### 配置 Cloudflare Tunnel

1. 登录 Cloudflare：
```bash
cloudflared login
```

2. 创建隧道：
```bash
cloudflared tunnel create my-tunnel
```

3. 配置隧道（my_tunnel.yml）：
```yaml
tunnel: <你的隧道ID>
credentials-file: /path/to/your/credentials-file.json

ingress:
  - hostname: yoursubdomain.yourdomain.com
    service: http://localhost:8000
  - service: http_status:404
```

### 运行项目

1. 启动本地 LLM 服务（Ollama 或 LM Studio）

2. 启动 FastAPI 服务器：
```bash
uvicorn main_cloudflare:app --host 0.0.0.0 --port 8000 --reload
```

3. 运行 Cloudflare Tunnel：
```bash
cloudflared tunnel --config my_tunnel.yml run my-tunnel
```

### API 端点

- `/chat`: POST 端点，用于 LLM 聊天交互
- `/health`: GET 端点，用于健康检查

### 开发说明

- 开发模式下支持热重载
- API 文档访问地址：`https://yoursubdomain.yourdomain.com/docs`
- 项目默认运行在 8000 端口
- 项目架构将在后续更新中优化 
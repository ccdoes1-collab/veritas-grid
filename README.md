# Veritas Grid

A comprehensive full-stack platform with multi-language SDK support, scalable infrastructure, and robust documentation.

## Project Structure

```
veritas-grid/
├── apps/              # Applications
│   ├── api/           # Backend API service
│   ├── web/           # Frontend web application
│   └── worker/        # Background worker service
├── packages/          # Shared packages
│   ├── engine/        # Core business logic
│   ├── sdk-js/        # JavaScript/TypeScript SDK
│   └── sdk-python/    # Python SDK
├── infra/             # Infrastructure
│   ├── terraform/     # Infrastructure as Code
│   ├── cloudflare/    # CDN/DNS configuration
│   └── docker/        # Container definitions
├── docs/              # Documentation
│   ├── api/           # API documentation
│   ├── architecture/  # System architecture
│   └── compliance/    # Compliance & security
└── scripts/           # Utility scripts
    ├── migrations/    # Database migrations
    └── seeding/       # Data seeding scripts
```

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.9+
- Docker
- Terraform

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ccdoes1-collab/veritas-grid.git
cd veritas-grid
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables:
```bash
cp .env.example .env.local
```

### Running Locally

#### API Server
```bash
cd apps/api
npm run dev
```

#### Web Application
```bash
cd apps/web
npm run dev
```

#### Worker Service
```bash
cd apps/worker
npm run dev
```

## Development

### Creating a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### Running Tests
```bash
npm run test
```

### Building for Production
```bash
npm run build
```

## Documentation

- [API Documentation](./docs/api)
- [Architecture Guide](./docs/architecture)
- [Compliance & Security](./docs/compliance)

## Infrastructure

Infrastructure is managed with Terraform. See [infra/terraform](./infra/terraform) for configuration.

## SDKs

- **JavaScript/TypeScript**: [packages/sdk-js](./packages/sdk-js)
- **Python**: [packages/sdk-python](./packages/sdk-python)

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request
4. Ensure all tests pass

## License

MIT

## Support

For issues and questions, please open a GitHub issue.

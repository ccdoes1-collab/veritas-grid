# Architecture Guide

## System Overview

Veritas Grid is a modern, scalable full-stack platform built with:

```
┌─────────────────────────────────────────────────┐
│                  Web Frontend                    │
│             (Next.js / React)                    │
└────────────┬────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────┐
│                  API Server                      │
│            (Express.js / Node.js)                │
└────┬───────────────────────────────────┬────────┘
     │                                   │
     ▼                                   ▼
┌──────────────┐              ┌──────────────────┐
│  Database    │              │  Redis/Queue     │
└──────────────┘              └──────────────────┘
                                      │
                                      ▼
                              ┌──────────────────┐
                              │  Worker Service  │
                              │  (Bull/Node.js)  │
                              └──────────────────┘
```

## Components

### Web Application
- **Technology**: Next.js, React
- **Purpose**: User interface and client-side logic
- **Location**: `apps/web/`

### API Server
- **Technology**: Express.js, Node.js
- **Purpose**: REST API, business logic
- **Location**: `apps/api/`

### Worker Service
- **Technology**: Bull, Redis, Node.js
- **Purpose**: Asynchronous job processing
- **Location**: `apps/worker/`

### Core Engine
- **Technology**: TypeScript, Node.js
- **Purpose**: Shared business logic library
- **Location**: `packages/engine/`

### SDKs
- **JavaScript SDK**: `packages/sdk-js/`
- **Python SDK**: `packages/sdk-python/`

## Data Flow

1. User interacts with Web Frontend
2. Frontend calls API endpoints
3. API processes requests and stores/retrieves data
4. For async operations, API queues jobs in Redis
5. Worker service processes jobs from the queue
6. Results are stored and made available to the frontend

## Infrastructure

- **Hosting**: AWS (ECS, RDS, ElastiCache)
- **CDN**: Cloudflare
- **Infrastructure as Code**: Terraform
- **Containerization**: Docker

See `infra/` directory for details.

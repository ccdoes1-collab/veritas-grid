# API Documentation

## Overview

The Veritas Grid API is a RESTful API that provides access to core functionality.

## Base URL

```
http://localhost:3000/api/v1
```

## Authentication

All API requests require authentication using an API key in the Authorization header:

```
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

### Health Check

**GET** `/health`

Check if the API is running.

**Response:**
```json
{
  "status": "ok",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### Status

**GET** `/status`

Get API status and version information.

**Response:**
```json
{
  "service": "Veritas Grid API",
  "version": "1.0.0",
  "status": "running"
}
```

## Error Handling

The API returns appropriate HTTP status codes:

- `200 OK` - Successful request
- `400 Bad Request` - Invalid request
- `401 Unauthorized` - Missing or invalid authentication
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## Rate Limiting

API requests are rate-limited to 1000 requests per hour per API key.

## Versioning

The API uses URL-based versioning. The current version is `/v1`.

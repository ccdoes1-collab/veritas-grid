/**
 * Database Seeding Script
 * 
 * Usage: npm run seed
 */

import * as crypto from 'crypto';

interface User {
  id: string;
  email: string;
  name: string;
  created_at: string;
}

interface ApiKey {
  id: string;
  user_id: string;
  key_hash: string;
  name: string;
  created_at: string;
}

// Sample data
const users: User[] = [
  {
    id: crypto.randomUUID(),
    email: 'admin@veritas-grid.com',
    name: 'Admin User',
    created_at: new Date().toISOString(),
  },
  {
    id: crypto.randomUUID(),
    email: 'dev@veritas-grid.com',
    name: 'Developer',
    created_at: new Date().toISOString(),
  },
];

const apiKeys: ApiKey[] = users.map(user => ({
  id: crypto.randomUUID(),
  user_id: user.id,
  key_hash: crypto
    .createHash('sha256')
    .update(crypto.randomBytes(32))
    .digest('hex'),
  name: `${user.name} API Key`,
  created_at: new Date().toISOString(),
}));

async function seed() {
  console.log('Starting database seed...');
  
  console.log('Users to create:', users.length);
  users.forEach(user => {
    console.log(`  - ${user.email} (${user.name})`);
  });

  console.log('API Keys to create:', apiKeys.length);
  apiKeys.forEach(key => {
    console.log(`  - ${key.name}`);
  });

  console.log('Seed data prepared. Connect to database and run migrations.');
}

seed().catch(console.error);

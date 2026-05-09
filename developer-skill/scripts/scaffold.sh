#!/usr/bin/env bash
set -euo pipefail

APP_NAME="${1:-my-app}"

if ! command -v bun >/dev/null 2>&1; then
  echo "bun is required. Install Bun first: https://bun.sh"
  exit 1
fi

bun create next-app "$APP_NAME" \
  --ts \
  --tailwind \
  --eslint \
  --app \
  --src-dir \
  --import-alias "@/*"

cd "$APP_NAME"

bunx shadcn@latest init

mkdir -p \
  src/components/layout \
  src/components/data \
  src/lib \
  src/server \
  src/db \
  src/hooks \
  src/types

cat > src/lib/env.ts <<'EOF'
export const env = {
  NODE_ENV: process.env.NODE_ENV ?? "development",
}
EOF

echo "Created $APP_NAME with Next.js, Tailwind, shadcn, and project folders."

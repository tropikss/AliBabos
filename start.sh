#!/usr/bin/env bash
set -euo pipefail

NETWORK_NAME="microservices-network"

# Crée le réseau uniquement s'il n'existe pas
if ! docker network inspect "$NETWORK_NAME" >/dev/null 2>&1; then
  docker network create "$NETWORK_NAME"
fi

# Démarre l'infra sur le réseau partagé
docker compose -f infra/docker-compose.yml up --build -d

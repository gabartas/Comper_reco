#!/bin/sh

echo "Starting Recommandations service..."

export LOG_WITH_GUNICORN=true
export CONFIG_TYPE="config.ProductionConfig"

gunicorn app:app -w 2 --threads 2 -b 0.0.0.0:3000 


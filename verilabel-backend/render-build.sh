#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting build process..."

# 1. Install Python dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# 2. Run Database Seeding
# Make sure your DATABASE_URL is configured in Render's Environment Variables
# If using a remote PostgreSQL database, this will seed it correctly.
echo "Seeding database regulations..."
python -m scripts.seed_regulations

echo "Build complete!"

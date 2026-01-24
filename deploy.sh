#!/bin/bash

# Interactive deployment script for bertbullough.com

set -e

echo "================================"
echo "  bertbullough.com Deployment"
echo "================================"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
    git branch -M main
fi

# Check for GitHub remote
if ! git remote get-url origin &>/dev/null; then
    echo ""
    echo "No GitHub remote configured."
    read -p "Enter your GitHub username: " github_user

    if [ -z "$github_user" ]; then
        echo "Error: GitHub username required"
        exit 1
    fi

    git remote add origin "https://github.com/${github_user}/bertbullough.com.git"
    echo "Remote added: https://github.com/${github_user}/bertbullough.com.git"
fi

# Show status
echo ""
echo "Current status:"
git status --short

# Confirm deployment
echo ""
read -p "Deploy these changes? (y/n): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "Deployment cancelled."
    exit 0
fi

# Get commit message
echo ""
read -p "Commit message: " commit_msg

if [ -z "$commit_msg" ]; then
    commit_msg="Update site"
fi

# Deploy
git add .
git commit -m "$commit_msg"
git push -u origin main

echo ""
echo "================================"
echo "  Deployment complete!"
echo "================================"
echo ""
echo "Site will be live in 1-2 minutes at:"
echo "  https://bertbullough.com"
echo ""
echo "Check deployment status:"
echo "  https://github.com/$(git remote get-url origin | sed 's/.*github.com[:/]\(.*\)\.git/\1/')/actions"
echo ""

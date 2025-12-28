#!/bin/bash

# GitHub Contribution Graph Filler for 2024
# This script creates backdated commits throughout 2024
# Run this script locally to fill your 2024 contribution graph

# Configuration
REPO_NAME="contribution-filler-2024"
GITHUB_USERNAME="Muhammad00Ahmed"
EMAIL="mahmedrangila@gmail.com"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== GitHub 2024 Contribution Graph Filler ===${NC}\n"

# Create repository directory
mkdir -p $REPO_NAME
cd $REPO_NAME

# Initialize git repository
git init
echo "# 2024 Contribution Filler" > README.md
git add README.md
git commit -m "Initial commit"

echo -e "${GREEN}Creating backdated commits for 2024...${NC}\n"

# Counter for commits
COMMIT_COUNT=0

# Loop through all days in 2024 (366 days - leap year)
for month in {1..12}; do
    # Days in each month (accounting for leap year)
    case $month in
        1|3|5|7|8|10|12) days=31 ;;
        4|6|9|11) days=30 ;;
        2) days=29 ;; # 2024 is a leap year
    esac
    
    for day in $(seq 1 $days); do
        # Random number of commits per day (1-5)
        commits_per_day=$((RANDOM % 5 + 1))
        
        for commit_num in $(seq 1 $commits_per_day); do
            # Format date
            DATE=$(printf "2024-%02d-%02d" $month $day)
            
            # Random hour and minute
            HOUR=$((RANDOM % 24))
            MINUTE=$((RANDOM % 60))
            TIMESTAMP="${DATE}T$(printf "%02d:%02d:00" $HOUR $MINUTE)"
            
            # Create a file with unique content
            FILE="commits/commit_${DATE}_${commit_num}.txt"
            mkdir -p commits
            echo "Commit on $TIMESTAMP" > $FILE
            echo "Random data: $RANDOM" >> $FILE
            
            # Add and commit with backdated timestamp
            git add $FILE
            GIT_AUTHOR_DATE="$TIMESTAMP" GIT_COMMITTER_DATE="$TIMESTAMP" \
                git commit -m "Update on $DATE (commit $commit_num)" \
                --author="$GITHUB_USERNAME <$EMAIL>"
            
            COMMIT_COUNT=$((COMMIT_COUNT + 1))
            
            # Progress indicator
            if [ $((COMMIT_COUNT % 50)) -eq 0 ]; then
                echo -e "${GREEN}Created $COMMIT_COUNT commits...${NC}"
            fi
        done
    done
done

echo -e "\n${GREEN}✅ Successfully created $COMMIT_COUNT backdated commits for 2024!${NC}\n"

echo -e "${BLUE}Next steps:${NC}"
echo "1. Create a new repository on GitHub named '$REPO_NAME'"
echo "2. Run these commands:"
echo -e "   ${GREEN}git remote add origin https://github.com/$GITHUB_USERNAME/$REPO_NAME.git${NC}"
echo -e "   ${GREEN}git branch -M main${NC}"
echo -e "   ${GREEN}git push -u origin main${NC}"
echo ""
echo "3. Wait 5-10 minutes and check your GitHub profile!"
echo "   Your 2024 contribution graph should be filled! 🎉"
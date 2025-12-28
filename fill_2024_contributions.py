#!/usr/bin/env python3
"""
GitHub 2024 Contribution Graph Filler
This script creates backdated commits throughout 2024
"""

import os
import subprocess
import random
from datetime import datetime, timedelta

# Configuration
REPO_NAME = "contribution-filler-2024"
GITHUB_USERNAME = "Muhammad00Ahmed"
EMAIL = "mahmedrangila@gmail.com"

def run_command(cmd):
    """Execute shell command"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode == 0

def create_backdated_commits():
    """Create backdated commits for entire 2024"""
    
    print("🚀 GitHub 2024 Contribution Graph Filler\n")
    
    # Create and initialize repository
    os.makedirs(REPO_NAME, exist_ok=True)
    os.chdir(REPO_NAME)
    
    if not os.path.exists('.git'):
        run_command('git init')
        with open('README.md', 'w') as f:
            f.write('# 2024 Contribution Filler\n\nAutomated commits for 2024')
        run_command('git add README.md')
        run_command('git commit -m "Initial commit"')
    
    print("✅ Repository initialized\n")
    print("📅 Creating backdated commits for 2024...\n")
    
    # Create commits directory
    os.makedirs('commits', exist_ok=True)
    
    commit_count = 0
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    current_date = start_date
    while current_date <= end_date:
        # Random commits per day (1-5)
        commits_per_day = random.randint(1, 5)
        
        for i in range(commits_per_day):
            # Random time
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            
            commit_datetime = current_date.replace(hour=hour, minute=minute)
            timestamp = commit_datetime.strftime('%Y-%m-%dT%H:%M:%S')
            
            # Create unique file
            filename = f"commits/commit_{current_date.strftime('%Y-%m-%d')}_{i+1}.txt"
            with open(filename, 'w') as f:
                f.write(f"Commit on {timestamp}\n")
                f.write(f"Random data: {random.randint(1000, 9999)}\n")
            
            # Add and commit with backdated timestamp
            run_command(f'git add {filename}')
            
            commit_cmd = (
                f'GIT_AUTHOR_DATE="{timestamp}" '
                f'GIT_COMMITTER_DATE="{timestamp}" '
                f'git commit -m "Update on {current_date.strftime("%Y-%m-%d")} (commit {i+1})" '
                f'--author="{GITHUB_USERNAME} <{EMAIL}>"'
            )
            run_command(commit_cmd)
            
            commit_count += 1
            
            # Progress indicator
            if commit_count % 50 == 0:
                print(f"✅ Created {commit_count} commits...")
        
        current_date += timedelta(days=1)
    
    print(f"\n🎉 Successfully created {commit_count} backdated commits for 2024!\n")
    
    print("📋 Next steps:")
    print(f"1. Create a new PUBLIC repository on GitHub named '{REPO_NAME}'")
    print("2. Run these commands:")
    print(f"   git remote add origin https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git")
    print(f"   git branch -M main")
    print(f"   git push -u origin main")
    print("\n3. Wait 5-10 minutes and check your GitHub profile!")
    print("   Your 2024 contribution graph should be filled! 🎉\n")

if __name__ == "__main__":
    try:
        create_backdated_commits()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure you have Git installed and configured!")
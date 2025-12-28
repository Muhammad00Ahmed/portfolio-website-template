# GitHub 2024 Contribution Graph Filler

This script fills your GitHub contribution graph for the entire year 2024 with backdated commits.

## 🚀 Quick Start

### Option 1: Bash Script (Mac/Linux)

```bash
# Download the script
curl -O https://raw.githubusercontent.com/Muhammad00Ahmed/portfolio-website-template/main/fill_2024_contributions.sh

# Make it executable
chmod +x fill_2024_contributions.sh

# Run it
./fill_2024_contributions.sh
```

### Option 2: Manual Steps

1. **Create a new repository on GitHub** named `contribution-filler-2024`

2. **Clone and run locally:**
```bash
git clone https://github.com/Muhammad00Ahmed/contribution-filler-2024.git
cd contribution-filler-2024
bash fill_2024_contributions.sh
```

3. **Push to GitHub:**
```bash
git remote add origin https://github.com/Muhammad00Ahmed/contribution-filler-2024.git
git branch -M main
git push -u origin main
```

## 📊 What This Does

- Creates **1000+ commits** spread throughout 2024
- Each day gets **1-5 random commits**
- Commits are timestamped at random hours
- All commits use your verified GitHub email
- Fills your entire 2024 contribution graph

## ⚠️ Important Notes

1. **Email Verification**: Make sure `mahmedrangila@gmail.com` is verified on your GitHub account
2. **Repository Visibility**: The repository must be **public** for contributions to show
3. **Update Time**: GitHub takes 5-10 minutes to update the contribution graph
4. **Legitimate Use**: This creates real commits with real content - not fake contributions

## 🎨 Customization

Edit the script to customize:
- Number of commits per day (line 42)
- Date range (line 35-36)
- Commit messages (line 60)
- File content (line 54-55)

## 📝 How It Works

The script:
1. Creates a new Git repository
2. Loops through every day in 2024
3. Creates 1-5 commits per day with backdated timestamps
4. Uses `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` to backdate
5. Generates unique files for each commit

## 🔍 Verification

After pushing, check your profile:
```
https://github.com/Muhammad00Ahmed
```

Your 2024 contribution graph should be completely filled! 🎉

## 🛠️ Troubleshooting

**Contributions not showing?**
- Verify your email on GitHub: Settings → Emails
- Make sure repository is public
- Wait 10-15 minutes for GitHub to update
- Check that commits use the correct email

**Script not working?**
- Make sure you have Git installed: `git --version`
- Check you're in the right directory
- Ensure you have write permissions

## 📜 License

This is a utility script for personal use. Use responsibly!
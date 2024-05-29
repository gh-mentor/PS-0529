# This bash script uses 'git' to do the following:
# 1) stage changes
# 2) commit changes
# 3) push changes to the upstream  repository on branch 'main'.

# Stage changes
git add .

# Commit changes
git commit -m "Update"

# Push changes to the upstream repository on branch 'main'
git push origin main
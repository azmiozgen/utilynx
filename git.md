# Git commands

## Add submodule
* `git submodule add <URL to Git repo>`
* `git submodule init`

## Clone with submodules
* `git clone --recursive <URL to Git repo>`
* `git submodule update --init --recursive` (Already cloned repository)

## Git pull-push with specific ssh-key
`ssh-agent bash -c 'ssh-add ~/.ssh/azmi; git pull'`

## List large files
```
git ls-files -s | while read -r mode sha stage file; do
  size=$(git cat-file -s "$sha")
  # convert to human readable (KB/MB/GB)
  hr=$(numfmt --to=iec --suffix=B "$size")
  echo -e "$hr\t$file"
done | sort -h | tail -20
```

## Pull with submodules
* `git pull --recurse-submodules`

## Remove unnecessary objects from .git
1. Find the biggest 10 objects with `git verify-pack -v .git/objects/pack/pack-*.idx | sort -k 3 -n | tail -10`
2. Get object name with `git rev-list --objects --all | grep <sha1 code from the 1st command>`
3. Remove objects with `git filter-branch --index-filter 'git rm --cached --ignore-unmatch <filename-pattern>' -- --all`
4. `rm -Rf .git/refs/original/`
5. `rm -Rf .git/logs`
6. Continue step 3. by removing other filename-patterns.
7. If done with 6. prune with `git gc --prune=now --aggressive`
8. `git push --force`

## Recover deleted branch
1. `git reflog`
2. Take the deleted branch log id
3. `git checkout <id>`
4. `git branch <branch-name>`

## Prune remote branches
`git remote prune origin`

## Prune local branches merged to main (safely)
`!f() { \n    echo \"Switching to main branch...\"; \n    git checkout main; \n    echo \"Pulling latest changes...\"; \n    git pull origin main; \n    echo \"\"; \n    echo \"Branches that would be deleted:\"; \n    git branch --merged | grep -v \"\\\\*\\\\|main\\\\|master\\\\|develop\"; \n    echo \"\"; \n    echo \"Continue with deletion? (y/N)\"; \n    read answer; \n    if [ \"$answer\" = \"y\" ]; then \n        git branch --merged | grep -v \"\\\\*\\\\|main\\\\|master\\\\|develop\" | xargs -n 1 git branch -d; \n        echo \"Cleanup complete!\"; \n    else \n        echo \"Cleanup cancelled.\"; \n    fi; \n}; f`

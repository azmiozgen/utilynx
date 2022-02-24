# Git commands

## Add submodule
* `git submodule add <URL to Git repo>`
* `git submodule init`

## Clone with submodules
* `git clone --recursive <URL to Git repo>`
* `git submodule update --init --recursive` (Already cloned repository)

## Git pull-push with specific ssh-key
`ssh-agent bash -c 'ssh-add ~/.ssh/azmi; git pull'`

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
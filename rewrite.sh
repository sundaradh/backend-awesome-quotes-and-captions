git filter-branch --env-filter '
if [ "$GIT_AUTHOR_EMAIL" = "mailarjunadhikari@gmail.com" ]; then
    GIT_AUTHOR_NAME="iamawmrit"
    GIT_AUTHOR_EMAIL="awmrit@gmail.com"
fi
if [ "$GIT_COMMITTER_EMAIL" = "mailarjunadhikari@gmail.com" ]; then
    GIT_COMMITTER_NAME="iamawmrit"
    GIT_COMMITTER_EMAIL="awmrit@gmail.com"
fi
' --tag-name-filter cat -- --branches --tags
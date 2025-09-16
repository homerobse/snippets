echo 'Start.'

cat config.json | jq '.project_folder'  # prints: "this/is/the/folder"

echo "--- after cat ---"

proj_folder=$(jq -r '.project_folder' config.json)

echo $proj_folder  # prints: this/is/the/folder (without quotes)
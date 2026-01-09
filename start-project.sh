#! /usr/bin/bash

# # get the project dir name
project=$1
if [ -z "$1" ]; then
  echo "Enter the project dir"
  exit 1
fi
# # cd to that dir
# cd "$project" || echo "Cant cd into dir $project" && exit 1
# start a new tmux session, or attach to one if already exists
tmux new-session -d -s "$project"
# start a server window
tmux rename-window -t "$project":0 'server'
# start a nvim editor
tmux new-window -t "$project" -n 'editor'
tmux send-keys -t "$project":editor "nvim" C-m
tmux attach-session -t "$project"

#!/usr/bin/env python3
import argparse
import json
import sys
import urllib.error
import urllib.request

def fetch_events(username):
    url = f"https://api.github.com/users/{username}/events"
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "github-activity-cli",
            "Accept": "application/vnd.github+json",
        },
    )
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
    return json.loads(body)


def format_event(event):
    event_type = event["type"]
    repo = event["repo"]["name"]
    payload = event["payload"]

    if event_type == "PullRequestReviewCommentEvent":
       return f"Commented on a pull request review in {repo}"
    if event_type == "MemberEvent":
        return f"{payload['action'].capitalize()} a collaborator in {repo}"


    if event_type == "PushEvent":
        branch = payload["ref"].removeprefix("refs/heads/")
        return f"Pushed to {branch} in {repo}"
    if event_type == "PullRequestEvent":
        return f"{payload['action'].capitalize()} a pull request in {repo}"
    if event_type == "PullRequestReviewEvent":
        return f"Reviewed a pull request in {repo}"
    if event_type == "IssuesEvent":
        return f"{payload['action'].capitalize()} an issue in {repo}"
    if event_type == "IssueCommentEvent":
        return f"Commented on an issue in {repo}"
    if event_type == "WatchEvent":
        return f"Starred {repo}"
    if event_type == "ForkEvent":
        return f"Forked {repo}"
    if event_type == "CreateEvent":
        return f"Created a {payload['ref_type']} in {repo}"
    return f"{event_type} in {repo}"

def parse_args():
    parser = argparse.ArgumentParser(
        prog="github-activity",
        description="Show a GitHub user's recent public activity.",
    )
    parser.add_argument("username", help="GitHub username")
    parser.add_argument("--type", help="only show this event type, e.g. PushEvent")
    return parser.parse_args()
def main():
    args = parse_args()
    username = args.username

    try:
        events = fetch_events(username)
    except urllib.error.HTTPError as error:
        ...  # unchanged
    except urllib.error.URLError as error:
        ...  # unchanged

    if not events:
        print("No recent activity found.")
        return

    if args.type:
        events = [event for event in events if event["type"] == args.type]
        if not events:
            print(f"No {args.type} events found for '{username}'.")
            return
    
    counts = {}
    for event in events:
        line = format_event(event)
        counts[line] = counts.get(line, 0) + 1

    for line, count in counts.items():
        if count > 1:
            print(f"- {line} ({count} times)")
        else:
            print(f"- {line}")
if __name__ == "__main__":
    main()
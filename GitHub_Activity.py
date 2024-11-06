
import requests
import json
import datetime

username=input("Enter user name:")
user_url=f"https://api.github.com/users/{username}"#user url
event_url=f"https://api.github.com/users/{username}/events"#event url

user_content=requests.get(user_url)#user info get req
event_content=requests.get(event_url)#event info ger req

response = requests.get(user_url, timeout=10)#ger resposnse code

if response.status_code == 200:
    user_info = user_content.json()  # convert obj/json to dict using request module
    event_info = event_content.json()  # convert obj/json to dict  using request module

    name = user_info.get('name', 'Name not available') # get name...account detils using get method from dict
    location = user_info.get("location", 'Not found !')
    follower = user_info.get("followers", "None")
    following = user_info.get('following', "None")
    account_created = user_info.get("created_at")

    account_created_date = datetime.datetime.strptime(account_created, '%Y-%m-%dT%H:%M:%SZ')
    account_created_formatted = account_created_date.strftime('%Y-%m-%d')

    current_datetime = datetime.datetime.now()
    total_days = current_datetime - account_created_date
    # print(f"Name: {name}")
    print(f'Location:{location}')
    print(f'Followers:{follower} people.')
    print(f'Following:{following} people.')
    print(f'Account created at: {account_created_formatted} Total {total_days.days} day ago!')
    print("Common Events")
    for event in event_info:
        # Covering only the most common events
        if event['type'] == 'IssueCommentEvent':
            print(f"-commented on issue {event['payload']['issue']['number']}")
        elif event['type'] == 'PushEvent':
            print(f"-pushed to {event['repo']['name']}")
        elif event['type'] == 'IssuesEvent':
            print(f"-created issue {event['payload']['issue']['number']}")
        elif event['type'] == 'WatchEvent':
            print(f"-starred {event['repo']['name']}")
        elif event['type'] == 'PullRequestEvent':
            print(f"-created pull request {event['payload']['pull_request']['number']}")
        elif event['type'] == 'PullRequestReviewEvent':
            print(f"-reviewed pull request {event['payload']['pull_request']['number']}")
        elif event['type'] == 'PullRequestReviewCommentEvent':
            print(f"-commented on pull request {event['payload']['pull_request']['number']}")
        elif event['type'] == 'CreateEvent':
            print(f"-created {event['payload']['ref_type']} {event['payload']['ref']}")
        else:
            print(f"-{event['type']}")

else:
    print(f"Error fetching events for {username}: {response.status_code}")

import requests

def delete_webhook(webhook_url):
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.delete(webhook_url, headers=headers)
    
    if response.status_code == 204:
        print("Webhook deleted successfully.")
    else:
        print(f"Failed to delete webhook. Status code: {response.status_code}")

# Prompt the user to enter the webhook URL
webhook_url = input("Enter the webhook URL: ")
delete_webhook(webhook_url)

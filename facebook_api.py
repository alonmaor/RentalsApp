import requests

# Set your access token and group ID
fb_access_token = 'EAANiLsDHsckBAAda0LvZAB9jceHYqJFzSpz7lykTwzamTj5rKBde4uW2BwIrss3G0RUaMakQ7TATjkH6nWWUiFwvmGOZBsOZBCJQmlZCXFIxUwRpxUY3WWZB3lsYGGL4OQMVE667Ae6DLFDNnvzs6CSlxwH7Xy1YRwtUunCOS7AZDZD'
fb_group_id = '145137958541058'

# Make a GET request to fetch posts from the group
fb_url = f'https://graph.facebook.com/v16.0/{fb_group_id}/feed'
fb_params = {
    'access_token': fb_access_token,
    'limit': 100  # Adjust the limit as per your requirements
}

all_posts = []

def get_posts():
    try:
        response = requests.get(fb_url, params=fb_params)
        data = response.json()

        # Add posts to the list
        all_posts.extend(data['data'])

        # Check if there are more posts
        # if 'paging' in data and 'next' in data['paging']:
        #     url = data['paging']['next']
        # else:
        #     break

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    # Process the retrieved posts
    messages = []
    for post in all_posts:
        # Extract relevant information from the post
        post_id = post['id']
        message = post.get('message', '')
        messages.append(message)
        created_time = post['updated_time']
        # Additional information can be extracted based on your requirements

        # Process the post as desired (e.g., store in a database, perform analysis, etc.)
        # print(f"Post ID: {post_id}")
        # print(f"Message: {message}")
        # print(f"Created Time: {created_time}")
        # print('---')

    return messages

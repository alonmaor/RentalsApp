import requests

from common.constants import FB_ACCESS_TOKEN_NAME, FB_GROUP_ID_NAME

from facebook_scraper import get_posts
# Set your access token and group ID
#fb_access_token = 'EAANiLsDHsckBAPZA3LeMtw6l52NwqAZByXCE70Vz5GwVldUsU8LhH1OeG4GwkOAIGJaUyYnvGca0hk9YOWiBZABKuarQJjZBjX2AFZBhW83tBSQCrZBclI6ZCrmYMCCAzwwjop3PpJZBtDG01et8fpZCi75ahs8ZAfjuZBdSJAkjVLun56dY0JqIkZBeVXKfTpx4PniyrvTMXj9usQZDZD'
#
# # Make a GET request to fetch posts from the group
# fb_url = f'https://graph.facebook.com/v16.0/{fb_group_id}/feed'
# fb_params = {
#     'access_token': fb_access_token,
#     'limit': 100  # Adjust the limit as per your requirements
# }


def scrape_fb_posts(config, logger):
    fb_group_ids = ['458499457501175', '287564448778602', '189220514572424', '2092819334342645', 'ApartmentsTelAviv', '1485565508385836', 'telavivrentals', '1196843027043598', '174312609376409', 'RentinTLV', '1458853481020151', 'tel.aviv.dirot']
    try:
        for group_id in fb_group_ids:
            for post in get_posts(group_id, pages=100):
                print('----------------------------------post----------------------------------\n')
                print(post)
                yield post
    except Exception as e:
        logger.error(f'failed to scrape fb posts. \n {e}')
        return None


def get_fb_posts(config, logger):
    all_posts = []
    try:
        fb_access_token = config[FB_ACCESS_TOKEN_NAME]
        fb_group_id = config[FB_GROUP_ID_NAME]
        print(f'fb_access_token: {fb_access_token}')
        print(f'fb_group_id: {fb_group_id}')
        fb_url = f'https://graph.facebook.com/v16.0/{fb_group_id}/feed'
        fb_params = {
            'access_token': fb_access_token,
            'limit': 100  # Adjust the limit as per your requirements
        }
        response = requests.get(fb_url, params=fb_params)
        print(response)
        data = response.json()

        # Add posts to the list
        all_posts.extend(data['data'])

        # Check if there are more posts
        # if 'paging' in data and 'next' in data['paging']:
        #     url = data['paging']['next']
        # else:
        #     break

    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred: {e}")
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

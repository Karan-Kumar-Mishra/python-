from instaloader import Instaloader, Profile

def get_instagram_user_info(username):
    loader = Instaloader()
    try:
        profile = Profile.from_username(loader.context, username)
        print(f"Username: {profile.username}")
        print(f"Full Name: {profile.full_name}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts Count: {profile.mediacount}")
        # Additional information can be retrieved as per the library documentation.
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
get_instagram_user_info("example_username")

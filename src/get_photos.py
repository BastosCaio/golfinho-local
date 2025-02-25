import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.logger_instructions import logger
from utils.utils import get_full_json, get_photo_data_from_id

def download_photo(user_id):
    """
    Wrapper function that calls get_photo_data_from_id for a given user_id.
    """
    try:
        get_photo_data_from_id(user_id)
        logger.info(f"Successfully downloaded photos for user ID {user_id}")
    except Exception as e:
        logger.error(f"Error downloading photos for user ID {user_id}: {e}")

def download_all_photos():
    full_json = json.loads(get_full_json())
    user_ids = [content['UserID'] for content in full_json.values() if 'UserID' in content]
    
    # Adjust max_workers as needed (e.g., 5, 10, or more depending on your network and device capacity).
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit download tasks for each user_id.
        future_to_user_id = {executor.submit(download_photo, user_id): user_id for user_id in user_ids}
        
        # iterate over completed futures to log their results.
        for future in as_completed(future_to_user_id):
            user_id = future_to_user_id[future]
            try:
                future.result()
            except Exception as e:
                logger.error(f"Exception occurred for user ID {user_id}: {e}")

if __name__ == "__main__":
    download_all_photos()

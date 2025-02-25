import json
from utils.logger_instructions import logger
from utils.utils import get_full_json, get_photo_data_from_id


def get_id_by_name(name):
    """
    Searches and returns the ID (index) of a record where the 'CardName' field matches the given name.
    """
    json_str = get_full_json()
    full_json = json.loads(json_str)
    
    for _, content in full_json.items():
        card_name = content.get('CardName', '')
        logger.debug(f"Checking record with CardName: {card_name}")
        if card_name == name:
            user_id = content.get("UserID")
            logger.info(f"Found record with CardName '{name}': UserID {user_id}")
            return user_id
        
    logger.warning(f"No record found with CardName: {name}")
    return None

if __name__ == "__main__":
    user_name = input("Enter CardName: ")
    user_id = get_id_by_name(user_name)
    
    if user_id is not None:
        get_photo_data_from_id(user_id)
    else:
        logger.error(f"User with CardName '{user_name}' not found.")

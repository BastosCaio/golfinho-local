import requests
import base64
import re
import os
import json
from utils.logger_instructions import logger
from dotenv import load_dotenv
import os

load_dotenv()

IP_DNS = os.getenv("IP_DNS")
USERNAME_GF = os.getenv("USERNAME_GF")
PASSWORD_GF = os.getenv("PASSWORD_GF")

def get_full_json():
    """
    Makes a request to the API to retrieve the AccessControlCard records and 
    converts the response into a JSON object.
    """
    url = f"http://{IP_DNS}/cgi-bin/recordFinder.cgi?action=doSeekFind&name=AccessControlCard&count=999999"
    digest_auth = requests.auth.HTTPDigestAuth(USERNAME_GF, PASSWORD_GF)

    try:
        response = requests.get(url, auth=digest_auth, timeout=20, verify=False)
        logger.info(f"Successfully accessed API at {url}")
        logger.info(f"Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error accessing API at {url}: {e}")
        raise

    records = {}
    pattern = r"records\[(\d+)\]\.([^=]+)=(.*)"

    for line in response.text.splitlines():
        line = line.strip()
        if not line or line.startswith("found="):
            continue  # Skip empty lines or lines starting with "found="

        match = re.match(pattern, line)
        if match:
            rec_id, key, value = match.groups()
            rec_id = int(rec_id)
            if rec_id not in records:
                records[rec_id] = {}
            records[rec_id][key] = value
            logger.debug(f"Parsed record {rec_id}: {key} = {value}")

    json_output = json.dumps(records, indent=4)
    logger.info("Successfully converted response to JSON")
    return json_output


def get_photo_data_from_id(user_id):
    """
    Retrieves photo data (Base64 encoded) for a given user ID,
    decodes it, and saves the photos as JPEG files.
    """
    url = f"http://{IP_DNS}/cgi-bin/AccessFace.cgi?action=list&UserIDList[0]={user_id}"
    digest_auth = requests.auth.HTTPDigestAuth(USERNAME_GF, PASSWORD_GF)

    try:
        response = requests.get(url, auth=digest_auth, timeout=20, verify=False)
        logger.info(f"Successfully accessed photo API at {url}")
        logger.info(f"Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error accessing photo API at {url}: {e}")
        raise

    pattern = r"FaceDataList\[\d+\]\.PhotoData\[\d+\]=(.*)"
    photo_data = re.findall(pattern, response.text)
    logger.info(f"Found {len(photo_data)} photo data entries for user ID {user_id}")

    folder = f"photos/face_photos_user_{user_id}"
    os.makedirs(folder, exist_ok=True)
    
    for i, photo in enumerate(photo_data):
        try:
            decoded_data = base64.b64decode(photo)
        except Exception as e:
            logger.error(f"Failed to decode photo data for image {i}: {e}")
            continue

        image_path = os.path.join(folder, f"face_image_{i}.jpg")
        try:
            with open(image_path, "wb") as f:
                f.write(decoded_data)
            logger.info(f"Image saved at {image_path}")
        except Exception as e:
            logger.error(f"Failed to save image {i} at {image_path}: {e}")
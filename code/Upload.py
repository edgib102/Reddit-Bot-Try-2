# import datetime
# from logging import exception
# from wsgiref.simple_server import server_version
from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import json

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

with open('settings.json') as x:
    settings = json.load(x)

uploadDetails = settings['upload_details']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
def create_video(videoFileName,thumbnailName,videoTitle):

    # upload_date_time = datetime.datetime(2021, 7, 23, 3, 30, 0).isoformat() + '.000Z'
    request_body = {
        'snippet':{
            'categoryId':uploadDetails['category'], #possible error
            'title': videoTitle,
            'description': f'{videoTitle}\n\n' + uploadDetails['description'],
            'tags': uploadDetails['tags']
        },
        'status':{
            'privacyStatus': uploadDetails['privacy'],
            # 'publishAt': upload_date_time,
            'selfDeclareMadeForKids': False
            
        },
        'notifySubscribers': False
    }

    mediaFile = MediaFileUpload('Video\\Output\\'+ videoFileName)


    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

    print('ran into an error')

    service.thumbnails().set(
        videoId=response_upload.get('id'),
        media_body=MediaFileUpload('Thumbnail\\'+ thumbnailName)
    ).execute()
    print('uploading video')

if __name__ == '__main__':
    create_video('Reddit Tts Video','thumbnail','Test video')
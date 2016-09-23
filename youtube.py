# code from https://developers.google.com/youtube/v3/code_samples/python#search_by_keyword
import sys
import urllib
from googleapiclient.discovery import build

"""
DEVELOPER_KEY = "AIzaSyAjZIqTWDXUHcYEx9OrtjrMcsHztHoUd8k"
QUERY = sys.argv[1] # e.g., "cats and dogs"
QUERY = urllib.quote(QUERY)
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
    q=QUERY,            # search terms
    part="id,snippet",  # what we want back
    maxResults=20,      # how many results we want back
    type="video"        # only tell me about videos
).execute()

videoURL = "https://www.youtube.com/watch?v=%s"

for search_result in search_response["items"]:
	print search_result["snippet"]["title"], videoURL%search_result["id"]["videoId"]
"""
"""
#video_id1 = "gU_gYzwTbYQ"  # bonkers the cat
#video_id2 = "tntOCGkgt98"  # cat compilation

DEVELOPER_KEY = "AIzaSyAjZIqTWDXUHcYEx9OrtjrMcsHztHoUd8k"
QUERY = sys.argv[1] # e.g., gU_gYzwTbYQ, tntOCGkgt98
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

results = youtube.commentThreads().list(
    part="snippet",
    videoId=QUERY,
    textFormat="plainText"
  ).execute()

#commentsURL = "https://www.youtube.com/all_comments?v=%s"

for item in results["items"]:
    comment = item["snippet"]["topLevelComment"]
    author = comment["snippet"]["authorDisplayName"]
    text = comment["snippet"]["textDisplay"]
    print "Comment by %s: %s" % (author, text)
"""
DEVELOPER_KEY = "AIzaSyAjZIqTWDXUHcYEx9OrtjrMcsHztHoUd8k"
QUERY = sys.argv[1] # e.g., "cats and dogs"
QUERY = urllib.quote(QUERY)
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def videoIDs(query):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

	search_response = youtube.search().list(
		q=query,            # search terms
		part="id,snippet",  # what we want back
		maxResults=10,      # how many results we want back
		type="video"        # only tell me about videos
	).execute()

	ids = [search_result["id"]["videoId"] for search_result in search_response["items"]]
	return ids

def comments(query):
	ids = videoIDs(query)
	comments = {} # map video ID to list of comment strings
	for id in ids:
		youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

		results = youtube.commentThreads().list(
			part="snippet",
			videoId=id,
			textFormat="plainText"
		).execute()

		comments[id] = []
		for item in results["items"]:
			comment = item["snippet"]["topLevelComment"]
			author = comment["snippet"]["authorDisplayName"]
			text = comment["snippet"]["textDisplay"]
			comments[id].append("Comment by %s: %s" % (author, text))
	return comments

allcomments = comments(QUERY)
for vid in allcomments:
    comments = allcomments[vid]
    print "Video "+vid
    print "\t",
    print '\n\t'.join(comments)

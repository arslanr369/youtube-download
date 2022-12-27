# Import the pytube library
import pytube

# Get the YouTube video URL
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object
yt = pytube.YouTube(url)

# Get the first video stream available
video_stream = yt.streams.first()

# Download the video to the current directory
video_stream.download()


video_stream.download('./videos', filename='my_video')

# Get all video streams available in 720p resolution
video_streams = yt.streams.filter(res='720p')

# Download the first video stream in 720p
video_stream = video_streams[0]
video_stream.download()


To download YouTube videos using Python, you can use the pytube library. Here is an example of how you can use pytube to download a video:

Copy code
# Import the pytube library
import pytube

# Get the YouTube video URL
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object
yt = pytube.YouTube(url)

# Get the first video stream available
video_stream = yt.streams.first()

# Download the video to the current directory
video_stream.download()
This code will download the video with the URL specified in the url variable to the current directory.

You can also customize the download by specifying the download location, the file format, and the quality of the video. For example, you can use the download method of the VideoStream object to specify the download location and the file name:

Copy code
video_stream.download('./videos', filename='my_video')
You can also use the filter method of the streams object to select a specific video stream based on its quality or format:

Copy code
# Get all video streams available in 720p resolution
video_streams = yt.streams.filter(res='720p')

# Download the first video stream in 720p
video_stream = video_streams[0]
video_stream.download()
It's important to note that downloading videos from YouTube is against the terms of service and may be illegal in some countries. You should make sure to respect the copyright laws and the terms of service of YouTube and other video sharing platforms.
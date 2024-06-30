# Video Streaming Application
## Languages & Tools

<img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/267_Python_logo-256.png" align="center" style="margin-left:10px;margin-bottom:5px;" width=70px/>

## Description
- **Client.launcher**: Launch the Client and application interface where we send RTSP requests and watch videos.
- **Client**: Implement SETUP, PLAY, PAUSE, TEARDOWN buttons for application, communicate with Server via RTSP protocol.
- **Client2**: Similar to Client but adds Extend functions such as: DESCRIBE, STOP, showing total time and remaining time of video, FORWARD, BACKWARD, calculating packet indexes.
- **Server**: Initialize Server.
- **ServerWorker**: Process requests sent from Client and respond.
- **RTPPacket**: Handle RTP packets.
- **VideoStream**: Includes information about the video stream from the server to the client and video stream processing.

## How to run
- First, launch the Server with the following command:

```python
python Server.py <server_port>
```

where <server_port> is the port for the Server to establish RTSP connections. The standard RTSP port is 554 but it is recommended to use a port greater than 1024.

- Then, create a new terminal window and launch the Client with the following command:

```python
python ClientLauncher.py <server_host> <server_port> <rtp_port> <video_file>
```

where <server_host> is the IP address of the machine running the Server, <server_port> is the same as the previous command, <rtp_port> is the port to receive RTP_packet, <video_file> is the name of the video file we want to watch (for example: movie.Mjpeg )

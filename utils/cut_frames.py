import cv2
import os
import shutil
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def convertMillis(millis):
    return str(round(millis//(1000*60*60))) + ":"+str(round(millis//(1000*60)))+ ":" +str((millis/1000)%60)

def cut_video_frames(video_path, s_t, e_t):
    dic = {}
    video = video_path
    s_time = s_t
    e_time = e_t
    # ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
    print("Cutting the video according to the given time.")
    ffmpeg_extract_subclip(video, s_time, e_time, targetname="cut.mp4")
    print("Video cutting Done.")
    cap= cv2.VideoCapture('cut.mp4')
    i=0
    fps = cap.get(cv2.CAP_PROP_FPS)
    timestamps = [cap.get(cv2.CAP_PROP_POS_MSEC)]
    calc_timestamps = [0.0]
    path = "./frames"
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)
        
    print('Extracting frames.')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC))
        calc_timestamps.append(calc_timestamps[-1] + 1000/fps)
        name = str(i+1)+'.jpg'
        cv2.imwrite(path+ "/" +name, frame)
        i+=1
        dic[name] = convertMillis(s_time*1000 + calc_timestamps[i]) 
    
    cap.release()
    cv2.destroyAllWindows()
    
    print('Frames Extraction Done.')

    try:
        if os.path.exists("cut.mp4"):
            os.remove("cut.mp4")
    except:
        pass
    
    return dic
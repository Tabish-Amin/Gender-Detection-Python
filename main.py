from utils.cut_frames import cut_video_frames
from utils.detect import detect_gender
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--video', type=str, required=True)
parser.add_argument('--start_time', type=int, required=True)
parser.add_argument('--end_time', type=int, required=True)

args = parser.parse_args()

timestramp_dic = cut_video_frames(args.video,args.start_time,args.end_time)
gender_dic = detect_gender()

keys = set(list(timestramp_dic.keys()) + list(gender_dic.keys()))

results = []
for key in keys:
    result = {}
    result['frame_name'] = int(key.split(".")[0])
    result['timestramp'] = timestramp_dic[key]
    result['detected_genders'] = gender_dic[key]
    results.append(result)

df = pd.DataFrame(results).sort_values('frame_name')
df['frame_name'] = df['frame_name'].astype(str) + '.jpg'

df.to_csv('genders.csv',index = False)

print("Result saved to csv named 'gender.csv' in the current dir")

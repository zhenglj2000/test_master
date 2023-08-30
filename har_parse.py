import json
import re

har_file = "D:\VSProject\Test\youtube_Love Bites.har"
with open(har_file, "r", encoding='utf-8') as f:
    har_data = json.load(f)

video_url = []
audio_url = []
video_range = []
audio_range = []
video_size = []
audio_size = []
for entry in har_data['log']['entries']:
    url = entry['request']['url']
    if 'videoplayback?' in url:
        if 'itag=251' in url:
            audio_url.append(url)
            # range_num = re.findall(r'range=(.*)&', url)#使用了贪婪匹配，意味着它会尽可能多地匹配字符，直到遇到最后一个&字符为止。
            range_num = re.findall(r'range=([^&]+)&', url)[0]
            audio_range.append(range_num) #使用了非贪婪匹配，表示匹配尽量少的字符，直到遇到第一个&字符为止。注意返回类型是list类型，所以取下标0 
            audio_size.append(-eval(range_num)+1) #eval()用于求字符串表达式的结果

        if 'itag=248' in url:
            video_url.append(url)
            range_num = re.findall(r'range=([^&]+)&', url)[0]
            video_range.append(range_num)#使用了非贪婪匹配，表示匹配尽量少的字符，直到遇到第一个&字符为止。 
            video_size.append(-eval(range_num)+1)

print(audio_range)
print(video_range)
print(audio_size)
print(video_size)
# print(audio_url)
print(video_url[0])
print(sum(video_size) + sum(audio_size))


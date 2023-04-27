import os
import json

def extract_format_data(format_data):
    extension = format_data["ext"]
  #  filesize = format_data["filesize"] or "00"
    format_name = format_data["format"]
    url = format_data["url"]
    format_name = format_data["format"]
    format_id = format_data["format_id"]
    #format_note = format_data["format_note"]
    
    return {
        "extension": extension,
        "format_name": format_name,
        "url": url,
       #"filesize": filesize,
        
      # "format_note":format_note,
        "format_id":format_id,
    }


def extract_video_data_from_url(url):  
    
    command = f'youtube-dl "{url}" -j --no-playlist'
    output = os.popen(command).read()
    video_data = json.loads(output)

    title = video_data["title"]
    formats = video_data["formats"]
    thumbnail = video_data["thumbnail"]

    formats = [extract_format_data(format_data) for format_data in formats]
    return {
        "title": title,
        "formats": formats,
        "thumbnail": thumbnail,
        
        

        #"ext": ext,
        #"tbr": tbr,
       # "filesize":filesize

    }

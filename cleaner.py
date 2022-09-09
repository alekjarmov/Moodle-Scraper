from urllib.parse import urlparse
from urllib.parse import parse_qs
import os

def clean():
    filename = input("Enter the name of the file to clean: ")
    base_recording_url = 'https://bbb-lb.finki.ukim.mk/playback/presentation/2.3/'
    with open(filename, 'r', encoding='utf-8') as f:
        with open('cleaned_' + filename, 'w', encoding='utf-8') as f2:
            lines = f.readlines()
            for line in lines:
                if line == '\n':
                    f2.write(line)
                    continue
                line_split = line.split(' ')
                url = line_split[-1]
                parsed_url = urlparse(url)
                rid = parse_qs(parsed_url.query)['rid'][0]
                url = base_recording_url + rid
                new_line = line_split[:-1] + [url] + ['\n']
                f2.write(' '.join(new_line))

def test_folder():
    # if the directory snimki does not exist, create it
    if not os.path.exists('snimki'):
        os.makedirs('snimki')

    with open('snimki/test.txt', 'w', encoding='utf-8') as f:
        f.write('test')

test_folder()
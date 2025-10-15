import urllib.request

urls = ['http://127.0.0.1:5000/', 'http://127.0.0.1:5000/static/xiao.jpg']
for url in urls:
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            info = r.info()
            data = r.read()
            print(url)
            print(' status:', r.getcode())
            print(' content-type:', info.get_content_type())
            print(' length:', len(data))
            print('-' * 40)
    except Exception as e:
        print(url)
        print(' ERROR:', e)
        print('-' * 40)

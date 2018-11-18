import re

"Process the large volume of files"

"""
Using buffering concept, so file will be read 10bytes at a time
This is mainly to avoid memory consumption at RAM level.
"""
"Created a pattern to identify ip address, url and http_status"
"This works perfect"
pattern = '^((\d{3}|\d{2}|\d{1}).(\d{3}|\d{2}|\d{1}).(\d{3}|\d{2}|\d{1}).(\d{3}|\d{2}|\d{1})).*\[(.*)\]\s(.*)\sHTTP/1.1\"\s(\d{3})'
with open('apache_logs.txt', 'r', buffering=10) as f:
    count = 0
    fw = open('data_output.txt', 'w')
    for line in f:
        full_match = re.findall(r'%s' % pattern, line, re.X)
        if full_match:
            ip_address, url, http_status = full_match[0][0], full_match[0][6],full_match[0][7]
            # print(ip_address, url, http_status)
            "Writing in to new file"
            fw.write(ip_address + "|" + url + "|" + http_status + "\n")
            """
            Sample output:
            65.55.213.73|"GET /blog/geekery/installing-windows-8-consumer-preview.html|200
            65.55.213.73|"GET /blog/tags/ruby|200
            65.55.213.73|"GET /blog/geekery/logstash-1.0.0-release.html|200
            """
    fw.close()




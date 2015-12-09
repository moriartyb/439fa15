
cmd = "iwlist wlp1s0 scan | sed -ne \'s#^[[:space:]]*\\(Quality=\\|Encryption key:\\|ESSID:\\)#\\1#p\' -e \'s#^[[:space:]]*\\(Mode:.*\\)$#\\1\\n#p\' | grep -B 2 hoc | grep -vE \'hoc|Encryption\' > last_datum.txt"

iteration = 0
data_pool = open("data_pool.txt", "w")

while True:
    os.system(cmd)
    a = open("last_datum.txt", "r")
    while a.readline() == '':
            a.seek(0)
    a.seek(0)
    line = a.readline()
    start = line.find("Signal level=") + len("Signal level=")
    end = line.find("dBm") - 1

    print "%d: %s" % (iteration, line[start:end])
    data_pool.write(line[start:end] + '\n')

    iteration++
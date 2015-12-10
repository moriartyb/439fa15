iwlist wlp1s0 scan | sed -ne \'s#^[[:space:]]*\\(Quality=\\|Encryption key:\\|ESSID:\\)#\\1#p\' -e \'s#^[[:space:]]*\\(Mode:.*\\)$#\\1\\n#p\' | grep -B 2 hoc | grep -vE \'hoc|Encryption\'

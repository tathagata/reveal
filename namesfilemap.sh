rm -f  *.log namefile.log *.html 
while read LINE;do
name=${LINE%,*}
echo "<a href=\"http://dl.dropbox.com/u/18146922/cables/"$name".html\">"$LINE"</a><br/>" >> namefile.html
echo "<h2>$LINE</h2><hr/>" > "${name/\//_}".html
grep "$name" data/names | awk -F"," '{printf("<a href=\"http://dl.dropbox.com/u/18146922/cables/%s\">%s, </a>\n",$1,$1);}' | sort | uniq | tr '\n' ',' >> "${name//\//_}".html
done < sig_names
cp *.html /home/tathagata/Dropbox/Public/cables/.

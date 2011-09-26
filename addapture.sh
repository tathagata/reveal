#!/bin/bash

top='<DOCTYPE html><html><head><title></title></head>'
script='<script id="aptureScript">(function (){var a=document.createElement("script");a.defer="true";a.src="http://www.apture.com/js/apture.js?siteToken=z5T7o7b";document.getElementsByTagName("head")[0].appendChild(a);})();</script><body>'

bot='</body></html>'
echo $top $script $bot
#for f in `find -name [0-9]*`;do 
sed '1i $top$script

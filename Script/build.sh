#!/bin/sh
echo Start generating hocky.plist...
./run.py

cp build/*.ipa t.ipa

cp hockey.plist t.ipa /Work/apache-tomcat-9.0.0.M9/webapps/Documents/iOS/NewTestStructDemo

echo done

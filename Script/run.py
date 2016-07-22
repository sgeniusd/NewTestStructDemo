#!/usr/bin/env python

import plistlib
info = plistlib.readPlist('../build/NewTestStructDemo.app/Info.plist')
subtitle = info['CFBundleShortVersionString']
identifier = info['CFBundleIdentifier']
bundleVersion = info['CFBundleVersion']
name = info['CFBundleDisplayName'] + bundleVersion

t = plistlib.readPlist('t.plist')
t['items'][0]['metadata']['bundle-identifier'] = identifier
t['items'][0]['metadata']['bundle-version'] = bundleVersion
t['items'][0]['metadata']['title'] = name
t['items'][0]['metadata']['subtitle'] = subtitle
plistlib.writePlist(t,'hockey.plist')

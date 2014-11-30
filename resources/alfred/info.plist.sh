#!/bin/bash

DIR=$(cd $(dirname $0); echo $PWD)

cat <<EOF > $DIR/info.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>bundleid</key>
	<string>com.resamsel.dbnavigator</string>
	<key>connections</key>
	<dict>
		<key>45B74738-9B9E-470A-B263-574B8C226CE8</key>
		<array>
			<dict>
				<key>destinationuid</key>
				<string>0A1E5AF5-6A96-4EE2-87E3-BBA9B66FDF79</string>
				<key>modifiers</key>
				<integer>0</integer>
				<key>modifiersubtext</key>
				<string></string>
			</dict>
		</array>
		<key>5AD6B622-051E-41D9-A608-70919939967A</key>
		<array>
			<dict>
				<key>destinationuid</key>
				<string>0A1E5AF5-6A96-4EE2-87E3-BBA9B66FDF79</string>
				<key>modifiers</key>
				<integer>0</integer>
				<key>modifiersubtext</key>
				<string></string>
			</dict>
		</array>
	</dict>
	<key>createdby</key>
	<string>René Samselnig</string>
	<key>description</key>
	<string></string>
	<key>disabled</key>
	<false/>
	<key>name</key>
	<string>Database Navigator</string>
	<key>objects</key>
	<array>
		<dict>
			<key>config</key>
			<dict>
				<key>autopaste</key>
				<false/>
				<key>clipboardtext</key>
				<string>{query}</string>
			</dict>
			<key>type</key>
			<string>alfred.workflow.output.clipboard</string>
			<key>uid</key>
			<string>0A1E5AF5-6A96-4EE2-87E3-BBA9B66FDF79</string>
			<key>version</key>
			<integer>0</integer>
		</dict>
		<dict>
			<key>config</key>
			<dict>
				<key>argumenttype</key>
				<integer>1</integer>
				<key>escaping</key>
				<integer>126</integer>
				<key>keyword</key>
				<string>dbnav</string>
				<key>runningsubtext</key>
				<string>Retrieving...</string>
				<key>script</key>
				<string>python alfred.py "{query}"</string>
				<key>subtext</key>
				<string>Shows database contents</string>
				<key>title</key>
				<string>Database Navigator</string>
				<key>type</key>
				<integer>0</integer>
				<key>withspace</key>
				<true/>
			</dict>
			<key>type</key>
			<string>alfred.workflow.input.scriptfilter</string>
			<key>uid</key>
			<string>5AD6B622-051E-41D9-A608-70919939967A</string>
			<key>version</key>
			<integer>0</integer>
		</dict>
		<dict>
			<key>config</key>
			<dict>
				<key>argumenttype</key>
				<integer>0</integer>
				<key>escaping</key>
				<integer>126</integer>
				<key>keyword</key>
				<string>res</string>
				<key>runningsubtext</key>
				<string>Searching...</string>
				<key>script</key>
				<string>/usr/local/bin/dbnav -X "skiline@localhost/skiline/resort?~{query}%"</string>
				<key>title</key>
				<string>Skiresort</string>
				<key>type</key>
				<integer>0</integer>
				<key>withspace</key>
				<true/>
			</dict>
			<key>type</key>
			<string>alfred.workflow.input.scriptfilter</string>
			<key>uid</key>
			<string>45B74738-9B9E-470A-B263-574B8C226CE8</string>
			<key>version</key>
			<integer>0</integer>
		</dict>
	</array>
	<key>readme</key>
	<string></string>
	<key>webaddress</key>
	<string>http://resamsel.com</string>
</dict>
</plist>
EOF

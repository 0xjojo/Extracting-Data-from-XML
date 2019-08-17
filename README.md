# Extracting-Data-from-XML
Data Format and Approach The data consists of a number of names and comment counts in XML as follows:
<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
You are to look through all the <comment> tags and find the <count> values sum the numbers.
The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements 
in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.
To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML
for any tag named 'count' with the following line of code:
counts = tree.findall('.//count')
Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. 
You could also work from the top of the XML down to the comments node and then loop through the child
nodes of the comments node.
Sample Execution
$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...

--------------------------------------------------------------------------------------------------------
My answer
Enter location: http://py4e-data.dr-chuck.net/comments_180845.xml
Retrieving  http://py4e-data.dr-chuck.net/comments_180845.xml
Retrieved 4209 characters
Count: 50
Sum: 2611


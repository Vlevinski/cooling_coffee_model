import requests
import pdfkit

#url = input("Please enter the url of the file you want to download.")
url = "https://blog.usejournal.com/python-basics-data-structures-d378d854df1b"
try:
    pdf = pdfkit.from_url(url, "file.pdf")
except Exception as e:
    print ("Exception", e)
    exit (999)
print (pdf)
#path = input("Please enter the file path that you would like the file to \
#download to. c:\Bob\PDF is an example of a valid file path.")
path = "/home/val/Desktop/MediumPages/structures.pdf"
print("Download starting.")
r = requests.get(pdf)
print (r)
with open(path, 'wb') as f:
    f.write(r.content)

# ????????????   Exception No wkhtmltopdf executable found: "b''"

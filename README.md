This is a personal project to see if i can actually beat captcha 
ALL HAIL ROBOTS WHO PASS CAPTCHA TEST

FYI Data Set would me made public later on 

For mac users ensure tesseract is installed on your device 
```brew install tesseract```

Then type in ```which tesseract``` on  your terminal 

Copy that path and replace it here 
```pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'```

PS Tesseract does not work on all captcha

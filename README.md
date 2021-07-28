# IOT-and-software-development-Department-tasks4.1
IOT-and-software-development-Department-tasks4.1
<br/><br/>
first part of the task
<br/>
<br/>
we will use IBM cloud to convert speech to text
<br/>
![image](https://user-images.githubusercontent.com/23351217/127134165-f251da29-1c41-4478-91d3-a73757718830.png)
<br/>
after we crate The IBM Watson™ Speech to Text service
<br/>
lets try the simple example uses the curl command to call methods of the service's HTTP interface.
<br/>
![image](https://user-images.githubusercontent.com/23351217/127137689-2721b2ce-c78c-4d6d-8090-cda283faafab.png)
<br/>
this is the result
<br/>
![image](https://user-images.githubusercontent.com/23351217/127137619-95fc7e58-f0aa-40a9-b40b-fc425585c7f9.png)
<br/>
let use python with the speech to text service 
<br>
first you need to intall ibm-watson 
```ruby
pip install --upgrade "ibm-watson>=5.2.0"
```
then open 'speechToText.py' file 
<br/>
then change the "apikey" and "url" to your information 
<br/> 
you can find it in your IBM Watson™ Speech to Text service
<br/>
![image](https://user-images.githubusercontent.com/23351217/127258538-ffec5b83-efe3-44fb-9314-0df6d94cfc0c.png)
<br/>
then change the "file directory" and the "content_type" 
<br/>
after that run the python file
```ruby
python3 speechToText.py 
```
you will see the output in file "output.txt"
<br/>
![image](https://user-images.githubusercontent.com/23351217/127258973-d0e488a9-1c7d-4781-941d-b21887531322.png)

<br/><br/>
second part of the task
<br/>
The IBM Watson™ Text to Speech service
<br/>
![image](https://user-images.githubusercontent.com/23351217/127259279-8c6423c2-83c7-427e-b6e6-090ae34f7734.png)
<br/>
lets try the simple example uses the curl command to call methods of the service's HTTP interface.
<br/>
![image](https://user-images.githubusercontent.com/23351217/127261514-042c9ed0-d8c7-4354-9514-199a7751a42f.png)
<br/>
this command will convert the string "hello world" and produce a WAV file that is named hello_world.wav.
<br/>
let use python with the text to speech service 
<br/>
open 'TextsToSpeech.py' file 
<br/>
then change the "apikey" and "url" to your information 
<br/>
after that run the python file
```ruby
python3 TextsToSpeech.py 
```
this code first will crate new mp3 file(speech.mp3) with 'hello world' 
<br/>
and will use the output from the first part to crate new mp3 file (winston.mp3)



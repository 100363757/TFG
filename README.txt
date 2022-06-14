The configuration used to execute the websites uses a port redirect function found in the chrome browser.

In order to access the webXR functionality of the pages, a compatible hardware device is required.

The only compatible device tested is the Oculus Quest 2.

In order to host the websites it is required to run the nodejs application webserver.js in a command line.

To access the pages:

  -connect the headset to the computer via wired connection
  
  -enable access to files from the oculus quest by the computer in headset
  
  -open a chrome browser tab
   
  -open the following link: chrome://inspect/#devices
  
  -enable discover USB devices
  
  -configure port forwarding to include 2 port forwarding settings:
    + 3000 -> localhost:3000
    + 8000 -> localhost:3001
    
  -enable port forwarding by ticking the box in the port forwarding configuration window and confirm by clicking done
  
  -open the browser in the headset
  
  -wait for the Quest device to appear in the list of devices in the chrome tab
  
  -navigate to localhost:3000 to access the main page
  
 
The page accessed may require a connection with another node server, in such case it is required to run the nodejs application backServer.js in a command line

import cv2
import threading
import ftplib 
from mss import mss

def server_upload():
    threading.Timer(1, server_upload).start()    
    #Screenshot with MSS lib
    with mss() as sct:
        sct.shot(mon=-1, output="te.png")
    img = cv2.imread('te.png')
    #Scale Down the Screenshot Image to reduce size
    scale_percent = 20 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    #-------Scaling Code Ends Here---------------
    #Define Img Quality(1 - 100) and Write File ---- Here Quality is 50
    cv2.imwrite('test.jpg', resized, [cv2.IMWRITE_JPEG_QUALITY, 50])
    session = ftplib.FTP('#ftpHostName','#ftpusername','ftppassword')
    session.cwd('#ftp working directory. Leave empty if dont wanna change')
    file = open('test.jpg','rb')                 
    session.storbinary('STOR test.jpg', file)     
    file.close()                                   
    session.quit()
    print("upload Success")

server_upload()


# =========== Sample Wesbite to view your image (Image Auto Update) ===========
#<html>
#     <head><title>Blank</title></head>
#     <body>
#         <img src="ftp/test.jpg" id="img">
#     </body>
#     <script>
#         //Autorefresh Image Javascript
#         function refresh(node)
#             {
#                var times = 1000; // update Rate in Miliseconds;
#             
#                (function startRefresh()
#                {
#                   var address;
#                   if(node.src.indexOf('?')>-1)
#                    address = node.src.split('?')[0];
#                   else 
#                    address = node.src;
#                   node.src = address+"?time="+new Date().getTime();
#             
#                   setTimeout(startRefresh,times);
#                })();
#             
#             }
#             
#             window.onload = function()
#             {
#               var node = document.getElementById('img');
#               refresh(node);            
#             }
#     </script>
# </html>
# =============================================================================

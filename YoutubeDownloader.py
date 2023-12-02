from pytube import YouTube
from pytube import Playlist
import streamlit as st 
import time

st.title("Downloader")

st.markdown('<h5>Decent Youtube Video Downloader</h5>',unsafe_allow_html=True)



st.divider()
#ask for the link from user
link = st.text_input("Enter URL :")
st.divider()

if link:
   yt = YouTube(link)
   # st.video(link)

   col11, col22 = st.columns(2)
   col11.image(yt.thumbnail_url,width=300)
   col22.markdown('<h5 style="background-color:white;text-align:center;padding:5px;color:black;margin-top:5px;">Title<h5>',unsafe_allow_html=True)

   with col22: 
        st.markdown('<p style="background-color:white;color:black;text-align:center;">'+str(yt.title)+'</p>',unsafe_allow_html=True)  




   col2, col3,col4 = st.columns(3)
   col2.markdown('<h5 style="background-color:white;text-align:center;padding:1px;color:black">Views<h5>',unsafe_allow_html=True)
   col3.markdown('<h5 style="background-color:white;text-align:center;padding:5px;color:black;">Published</h5>',unsafe_allow_html=True)  
   col4.markdown('<h5 style="background-color:white;text-align:center;padding:5px;color:black;">Duration</h5>',unsafe_allow_html=True) 
   with col2:   
        st.markdown('<p style="background-color:white;color:black;text-align:center;"> '+str(yt.views)+'</p>',unsafe_allow_html=True)
   with col3:
        st.markdown('<p style="background-color:white;color:black;padding:5px;text-align:center;">'+str(yt.publish_date)+'</p>',unsafe_allow_html=True)
   with col4:
         le = yt.length / 60
         formatted_num = "%.2f" % le
         st.markdown('<p style="background-color:white;color:black;text-align:center;padding:5px;">'+str(formatted_num).replace(".",":")+'</p>',unsafe_allow_html=True)



tab1, tab2,tab3 = st.tabs(["Video", "Audio","Playlist"])
 
with tab1:

      if link:
          options = yt.streams.all()
          # resolution = yt.streams.filter(progressive=False,mime_type="video/mp4",res="360p")
          res_dict = {
             "360p" : yt.streams.filter(progressive=False,mime_type="video/mp4",res="360p"),
             "480p" : yt.streams.filter(progressive=False,mime_type="video/mp4",res="480p"),
             "720p" : yt.streams.filter(progressive=False,mime_type="video/mp4",res="720p"),
             "1080p": yt.streams.filter(progressive=False,mime_type="video/mp4",res="1080p"),
          }
             
             
          selected_option2 = st.selectbox("Resolution",["360p","480p","720p","1080p"]) # returns all aviliable streams
      
      
          # selected_stream = yt.streams.get_by_itag(resolution.itag)
      
          # def download_click():
          #     d = selected_stream.download()
          #     st.text("Download completed!")
          # if st.button("Download"):
          #    download_click()          
            
          st.download_button("Download",data=yt.streaming_data["formats"][1]["url"],file_name=yt.title+".mp4",mime="video/mp4",key="videobtn")


with tab2:

      if link:
          options = yt.streams.all()
          resolution = yt.streams.filter(progressive=False,mime_type="audio/mp4")

          audo_dict = {
             "48kbps" : yt.streams.filter(progressive=False,mime_type="audo/mp4",abr="48kbps"),
             "128kbps" : yt.streams.filter(progressive=False,mime_type="video/mp4",res="128kbps"),
          }
             
          selected_option2 = st.selectbox("Resolution",["40kbps","128kbps"]) # returns all aviliable streams
      
    
          st.download_button("Download",data=yt.streaming_data["formats"][1]["url"],file_name=yt.title+".mp4",mime="video/mp4",key="audiobtn")

with tab3:
     try:

          p = Playlist(link)
          st.video(p.playlist_url)
     except Exception as e:
          st.warning("It is a not a playlist use video downloader to download!")
           

     #  if link:
          # p = Playlist(link)
        #   if p.length > 1:
            #   st.write(p.title)
          # st.write(p.length)
        #   else:
            #   st.write("It is Not a Playlist Please Download It as Video") 

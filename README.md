# Gender-Detection   


<h2>Objective :</h2>
<p>To build a gender detector that can approximately guess the gender of the person (face) from the frames of video .</p>

<h2>About the Project :</h2>
<p>In this Python Project, I had used Deep Learning to accurately identify the gender of a person from a single image of a face. I used the models trained by <a href="https://talhassner.github.io/home/projects/Adience/Adience-data.html">Tal Hassner and Gil Levi</a>. The predicted gender may be one of ‘Male’ and ‘Female’. And so, I made this a classification problem instead of making it one of regression.</p>

<h2>Dataset :</h2>
<p>For this python project, I had used the Adience dataset; the dataset is available in the public domain and you can find it <a href="https://www.kaggle.com/ttungl/adience-benchmark-gender-and-age-classification">here</a>. This dataset serves as a benchmark for face photos and is inclusive of various real-world imaging conditions like noise, lighting, pose, and appearance. The images have been collected from Flickr albums and distributed under the Creative Commons (CC) license. It has a total of 26,580 photos of 2,284 subjects in eight age ranges (as mentioned above) and is about 1GB in size. The models I used had been trained on this dataset.</p>

<h2>Additional Python Libraries Required :</h2>
<ul>
  <li>OpenCV</li>
  
       pip install opencv-python
</ul>
<ul>
 <li>Argparse</li>
  
       pip install argparse
</ul>
<ul>
 <li>Moviepy</li>
  
       pip install moviepy
</ul>

<h2>The contents of this Project :</h2>
<ul>
  <li>opencv_face_detector.pbtxt</li>
  <li>opencv_face_detector_uint8.pb</li>
  <li>gender_deploy.prototxt</li>
  <li>gender_net.caffemodel</li>
  <li>main.py</li>
  <li>utils folder</li>
  <ul>
    <li>cut_frames.py</li>
    <li>detect.py</li>
  </ul>
 </ul>
 <p>For face detection, we have a .pb file- this is a protobuf file (protocol buffer); it holds the graph definition and the trained weights of the model. We can use this to run the trained model. And while a .pb file holds the protobuf in binary format, one with the .pbtxt extension holds it in text format. These are TensorFlow files. For gender, the .prototxt file describe the network configuration and the .caffemodel file defines the internal states of the parameters of the layers.</p>
 
 <h2>Usage :</h2>
 <ul>
  <li>Download my Repository</li>
  <li>Open your Command Prompt or Terminal and change directory to the folder where all the files are present.</li>
  <li><b>Detecting Gender From Video</b> Use Command :</li>
  
      python main.py --video <video_path> --start_time <seconds> --end_time<seconds>
</ul>
  
  <h2>Workflow :</h2>
  <p>After executing the above command the will detect gender from the video by following steps:</p>
  <ul>
  <li>mian.py call <b>cut_video_frames</b> function from <b>cut_frames.py</b> that is in the <b>utils</b> folder.</li>
  <li>Given video will cut according to the given time and saved as <b>cut.mp4</b> in the current directory using <b>Moviepy</b> library.</li>
  <li>By using <b>Opencv</b> frames will extracted from <b>cut.mp4</b> and will save in the <b>frames</b> folder and <b>cut.mp4</b> will delete.</li>
  <li><b>Detecting Gender From Video</b> Use Command :</li>
  
      python main.py --video <video_path> --start_time <seconds> --end_time<seconds>
</ul>

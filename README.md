# EMNIST
Developed by @shubhammor0403


<div align = "center">Classify and predict words using EMNIST dataset<br>

<a href="https://imgflip.com/gif/2eb1pw"><img src="https://i.imgflip.com/2eb1pw.gif" align = "center" height = "280" width = "480"/></a>
</div>

Implementation of this model in an android application can be found at :- <a href="https://github.com/shubhammor0403/EMNIST_Android">EMNIST ANDROID</a>

# Description

This project offers a new solution to traditional handwriting recognition techniques using concepts of Deep learning and computer vision. An extension of Mnist digits dataset called the Emnist dataset has been used. It contains 62 classes with 0-9 digits and A-Z characters in both uppercase and lowercase. An application for Android, to detect handwritten text and convert it into digital form using Convolutional Neural Networks, abbreviated as CNN, for text classication and detection, has been created. Prior to that we pre-processed the dataset and applied various flters over it. Two seperate Jupyter files have been included. modeltrain.ipynb contains creation and training of the model and segment.ipynb contains prediction of words using the created model.

# Environment

<b>Anaconda Python</b>
<ul>
<li>Tensorflow</li>
<li>Keras</li>
<li>Numpy</li>
<li>Matplotlib</li>
<li>Opencv</li>
  </ul>

# Usage
<ul>
  <li>Download the EMNIST byclass dataset and place the binary files in the data folder(Create a new folder named data).<br>
    <a href="http://www.itl.nist.gov/iaui/vip/cs_links/EMNIST/gzip.zip">Emnist Dataset</a></li>
  
  <li>Create and train a model using modeltrain.ipynb (or use the provided model)</li>
  <li>Test out the model using segment.ipynb</li>
  </ul>
  


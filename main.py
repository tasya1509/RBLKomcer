import streamlit as st
from streamlit_option_menu import option_menu
from ultralytics import YOLO
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from ultralytics import settings
from PIL import Image, ImageDraw
from numpy import asarray
# from ultralytics import YOLO
# import matplotlib.pyplot as plt
# from io import BytesIO
# from PIL import Image
# import time


detector = YOLO('yolov8n.pt')

st.set_page_config(
    page_title="DECARTERA",
)

with st.sidebar:
   selected = option_menu(
        menu_title="Main Menu",  
        options=["Home","References","Aplication"], 
        icons=["house", "record-circle"],  
        menu_icon="cast",  # optional
        default_index=0,  # optional         
)

if selected == "Home":

    image2 = Image.open("logo.jpg")
    st.image(image2)
    st.caption("Created by *Anatasya and Shalaesya Ariffani Fabillah*")
    st.markdown(
    """
    - [Source Code](https://github.com/tasya1509/RBLKomcer)
    """
    )
if selected == "References":
     st.write("# DECARTERA ")
    st.write(
    """
    **The YOLO (You Only Look Once) YOLOv8n**.
    """
    )

    image1 = Image.open('YOLOv8n-architecture.jpg')
    image1.thumbnail((800,800))
    image3 = Image.open('YOLOv8n-model.jpg')
    image3.thumbnail((800,800))
    st.image(image1)
    st.image(image3) 
    st.markdown(
    """
    - [Streamlit](https://docs.streamlit.io/)
    """
    )
    st.markdown(
    """
    - [Ultralytics](https://pypi.org/project/ultralytics/)
    """
    )
    st.markdown(
    """
    - [YOLOv5s](https://docs.ultralytics.com/yolov5/quickstart_tutorial/#inference-with-pytorch-hub)
    """
    )
    st.markdown(
    """
    - [Matplotlib](https://matplotlib.org/stable/api/index)
    """
    )
    st.markdown(
    """
    - [Pillow](https://pillow.readthedocs.io/en/stable/)
    """
    )
    st.markdown(
    """
    - [BytesIO](https://docs.python.org/3/library/io.html)
    """
    )


if selected == "Aplication":
    
    uploaded_file = st.file_uploader("", type=["jpg",'jpeg','png'])
    if uploaded_file is None:
      st.text("Please upload an Image (jpg format)")
    else:
      image = Image.open(uploaded_file)
      results = detector(image)
      car_detections = [det for det in results[0].boxes if det.cls == 2]
      image_with_boxes = image.copy()
      draw = ImageDraw.Draw(image_with_boxes)
      for det in car_detections:
        x1, y1, x2, y2 = det.xyxy[0].tolist()
        confidence = float(det.conf)  # Convert tensor to float
        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
        draw.text((x1, y1 - 10), f"Car {confidence:.2f}", fill="red")
      st.image(image_with_boxes, caption="Detected Cars", use_column_width=True)
      st.header(f"Number of cars detected: {len(car_detections)}")

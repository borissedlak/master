import sys

import ModelParser
import Models
from VideoDetector import *

# privacy_model = ModelParser.parseModel("video:{'tag':'recording'}-->Gender_Trigger:{'prob':0.85}-->Blur_Area_Simple:{'blocks':5}")
privacy_model_1 = ModelParser.parseModel(Models.model_1)
privacy_model_2 = ModelParser.parseModel(Models.model_2)
privacy_model_3 = ModelParser.parseModel(Models.model_3)
privacy_model_4 = ModelParser.parseModel(Models.model_4)

chain_1 = privacy_model_1.getChainForSource("video", "webcam")
chain_2 = privacy_model_2.getChainForSource("video", "webcam")
chain_3 = privacy_model_3.getChainForSource("video", "webcam")
chain_4 = privacy_model_4.getChainForSource("video", "webcam")

detector_1 = VideoDetector(privacy_chain=chain_1, display_stats=True, write_stats=True)
detector_2 = VideoDetector(privacy_chain=chain_2, display_stats=True, write_stats=True)
detector_3 = VideoDetector(privacy_chain=chain_3, display_stats=True, write_stats=True)
detector_4 = VideoDetector(privacy_chain=chain_4, display_stats=True, write_stats=True)

# detector.processImage("../producer/demo_files/images/zoom_call.jpg", show_result=True)
# detector_1.processVideo(video_path="../producer/demo_files/videos/", video_name="video_1", model_name="model_1", show_result=False, )
# detector_2.processVideo(video_path="../producer/demo_files/videos/", video_name="video_1", model_name="model_2", show_result=False, )
# detector_3.processVideo(video_path="../producer/demo_files/videos/", video_name="video_1", model_name="model_3", show_result=False, )
# detector_4.processVideo(video_path="../producer/demo_files/videos/", video_name="video_1", model_name="model_4", show_result=False, )

detector_1.processVideo(video_path="../producer/demo_files/videos/", video_name="video_2", model_name="model_1", show_result=False, )
detector_2.processVideo(video_path="../producer/demo_files/videos/", video_name="video_2", model_name="model_2", show_result=False, )
detector_3.processVideo(video_path="../producer/demo_files/videos/", video_name="video_2", model_name="model_3", show_result=False, )
detector_4.processVideo(video_path="../producer/demo_files/videos/", video_name="video_2", model_name="model_4", show_result=False, )

sys.exit()

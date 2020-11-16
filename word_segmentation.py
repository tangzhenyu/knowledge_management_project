import thulac
from pyltp import Segmentor
from pyltp import CustomizedSegmentor
import os
 
sent = "韩国瑜此前就曾邀鸿海来高雄投资，而在16日直播时，韩更透露，17日要与郭台铭直接见面，邀他来高雄扩大投资创造更多工作机会。"
 
segment = thulac.thulac(user_dict='dict.txt',seg_only=True)
thu_out = segment.cut(sent, text=True)
print(thu_out)
 
LTP_DATA_DIR = 'D:\LTP\ltp_data_v3.4.0'
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
segmentor = Segmentor()
#segmentor.load_with_lexicon(cws_model_path, 'dict.txt')
segmentor.load(cws_model_path)
ltp_out = segmentor.segment(sent)
print(" ".join(w for w in ltp_out))
segmentor.release()

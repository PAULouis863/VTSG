#import spacy
#from spacy.matcher import Matcher
import os
import json
import glob
i=1
#ocr_files = [file for file in glob.glob(f"UIED/data/input/{i}/" + "*.json")]

text_segment={
    "span":"art"
}
pattern="patternmatcher"
segments={}
id=1
text_segment["span"] = "span.text"
segments[str(id)] = {}
segments[str(id)]["segment_info"] = text_segment
segments[str(id)]["text_analysis"] = {}
segments[str(id)]["text_analysis"][pattern] = {"doc": 1, "span": 2, "span_length": 2}
print(segments)

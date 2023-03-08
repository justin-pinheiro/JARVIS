import spacy
import random
from spacy.util import minibatch, compounding
from spacy.training import Example
from pathlib import Path
import time


start_time = time.time()

def train():
  nlp=spacy.load('en_core_web_sm')
  
  # Getting the pipeline component
  ner=nlp.get_pipe("ner")

  # training data
  TRAIN_DATA = [
              #Greetings
              ("hello there", {"entities": [(0, 5, "GREETING")]}),
              ("good morning", {"entities": [(0, 12, "GREETING")]}),
              ("good morning jarvis", {"entities": [(0, 12, "GREETING")]}),
              ("greetings", {"entities": [(0, 9, "GREETING")]}),
              ("greetings jarvis", {"entities": [(0, 9, "GREETING")]}),
              ("hiya", {"entities": [(0, 4, "GREETING")]}),
              ("hey", {"entities": [(0, 3, "GREETING")]}),
              ("hey jarvis", {"entities": [(0, 3, "GREETING")]}),
              ("hi everyone", {"entities": [(0, 2, "GREETING")]}),
              ("what's up", {"entities": [(0, 9, "GREETING")]}),
              ("good day", {"entities": [(0, 8, "GREETING")]}),
              ("hello", {"entities": [(0, 5, "GREETING")]}),
              ("hello jarvis", {"entities": [(0, 5, "GREETING")]}),
              ("hi there", {"entities": [(0, 8, "GREETING")]}),
              ("howdy", {"entities": [(0, 5, "GREETING")]}),
              ("yo", {"entities": [(0, 2, "GREETING")]}),
              ("hola", {"entities": [(0, 4, "GREETING")]}),
              ("salutations", {"entities": [(0, 11, "GREETING")]}),
              ("hi", {"entities": [(0, 2, "GREETING")]}),
              ("hi jarvis", {"entities": [(0, 2, "GREETING")]}),
              ("good evening", {"entities": [(0, 12, "GREETING")]}),
              ("good evening jarvis", {"entities": [(0, 12, "GREETING")]}),
              #Music
              ("Play Back in Black", {"entities": [(5, 18, "MUSIC_NAME")]}),
              ("Play the song Back in Black", {"entities": [(14, 27, "MUSIC_NAME")]}),
              ("Play the song Back in Black from AC/DC", {"entities": [(14, 27, "MUSIC_NAME")]}),
              ("Play Back in Black from AC/DC", {"entities": [(5, 18, "MUSIC_NAME")]}),
              ("Launch Back in Black", {"entities": [(7, 20, "MUSIC_NAME")]}),
              ("Launch Back in Black from AC/DC", {"entities": [(7, 20, "MUSIC_NAME")]}),
              ("Play Bad Romance", {"entities": [(5, 16, "MUSIC_NAME")]}),
              ("Play the song Bad Romance", {"entities": [(14, 25, "MUSIC_NAME")]}),
              ("Launch Bad Romance", {"entities": [(7, 18, "MUSIC_NAME")]}),
              ("Play Till I Collapse", {"entities": [(5, 20, "MUSIC_NAME")]}),
              ("Play the song Till I Collapse", {"entities": [(14, 29, "MUSIC_NAME")]}),
              ("Launch Till I Collapse", {"entities": [(7, 22, "MUSIC_NAME")]}),
              ("Play Merry Christmas", {"entities": [(5, 20, "MUSIC_NAME")]}),
              ("Play the song Merry Christmas", {"entities": [(14, 29, "MUSIC_NAME")]}),
              ("Launch Merry Christmas", {"entities": [(7, 22, "MUSIC_NAME")]}),
              ("Play Sweet Child o' Mine", {"entities": [(5, 24, "MUSIC_NAME")]}),
              ("Play the song Sweet Child o' Mine", {"entities": [(14, 33, "MUSIC_NAME")]}),
              ("Play Stairway to Heaven", {"entities": [(5, 23, "MUSIC_NAME")]}),
              ("Play the song Stairway to Heaven", {"entities": [(14, 32, "MUSIC_NAME")]}),
              ("Play Wonderwall", {"entities": [(5, 15, "MUSIC_NAME")]}),
              ("Play the song Wonderwall", {"entities": [(14, 24, "MUSIC_NAME")]}),
              ("Play Livin' on a Prayer", {"entities": [(5, 23, "MUSIC_NAME")]}),
              ("Play the song Livin' on a Prayer", {"entities": [(14, 32, "MUSIC_NAME")]}),
              ("Play Hotel California", {"entities": [(5, 21, "MUSIC_NAME")]}),
              ("Play the song Hotel California", {"entities": [(14, 30, "MUSIC_NAME")]}),
              #Weather
              ("what is the weather like", {"entities": [(0, 24, "WEATHER")]}),
              ("how's the weather today", {"entities": [(0, 23, "WEATHER")]}),
              ("what's the forecast like", {"entities": [(0, 24, "WEATHER")]}),
              ("is it sunny outside", {"entities": [(0, 19, "WEATHER")]}),
              ("are we expecting rain today", {"entities": [(0, 27, "WEATHER")]}),
              ("do i need an umbrella today", {"entities": [(0, 27, "WEATHER")]}),
              ("what kind of weather are we having", {"entities": [(0, 34, "WEATHER")]}),
              ("is it hot or cold outside", {"entities": [(0, 25, "WEATHER")]}),
              ("how's the weather looking", {"entities": [(0, 25, "WEATHER")]}),
              ("what's the temperature like outside", {"entities": [(0, 35, "WEATHER")]}),
              ("is it windy outside", {"entities": [(0, 19, "WEATHER")]}),
              ("is it snowing today", {"entities": [(0, 19, "WEATHER")]}),
              ("what's the weather forecast for today", {"entities": [(0, 37, "WEATHER")]}),
              ("is it humid outside today", {"entities": [(0, 25, "WEATHER")]}),
              ("what's the weather like in your area", {"entities": [(0, 36, "WEATHER")]}),
              ("is it foggy outside", {"entities": [(0, 19, "WEATHER")]}),
              ("what's the weather situation right now", {"entities": [(0, 38, "WEATHER")]}),
              ("is it a good day for outdoor activities", {"entities": [(0, 39, "WEATHER")]}),
              ("what's the weather like in the evening", {"entities": [(0, 38, "WEATHER")]}),
              ("are we expecting any storms today", {"entities": [(0, 33, "WEATHER")]}),
              #News
              ("what's the news today", {"entities": [(0, 21, "NEWS")]}),
              ("can you update me with the latest news", {"entities": [(0, 38, "NEWS")]}),
              ("tell me what's happening in the world", {"entities": [(0, 37, "NEWS")]}),
              ("do you have any news for me", {"entities": [(0, 27, "NEWS")]}),
              ("what's been going on lately", {"entities": [(0, 27, "NEWS")]}),
              ("what's new in the world today", {"entities": [(0, 29, "NEWS")]}),
              ("can you tell me the top news stories", {"entities": [(0, 36, "NEWS")]}),
              ("i need an update on current events", {"entities": [(0, 34, "NEWS")]}),
              ("anything interesting in the news today", {"entities": [(0, 38, "NEWS")]}),
              ("what are the headlines for today", {"entities": [(0, 32, "NEWS")]}),
              ("what's the latest news in the world", {"entities": [(0, 35, "NEWS")]}),
              ("what's the breaking news today", {"entities": [(0, 30, "NEWS")]}),
              ("can you give me a news update", {"entities": [(0, 29, "NEWS")]}),
              ("what are the current news stories", {"entities": [(0, 33, "NEWS")]}),
              ("i haven't been keeping up with the news, what's happening", {"entities": [(0, 57, "NEWS")]}),
              ("any important news to report", {"entities": [(0, 28, "NEWS")]}),
              ("what's happening around the world", {"entities": [(0, 33, "NEWS")]}),
              ("can you give me a rundown of the news", {"entities": [(0, 37, "NEWS")]}),
              ("tell me about the latest news development", {"entities": [(0, 41, "NEWS")]}),
              ]

  for _, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
      ner.add_label(ent[2])

  pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
  unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

  with nlp.disable_pipes(*unaffected_pipes):
    for _ in range(30):
      random.shuffle(TRAIN_DATA)
      batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
      for batch in batches:
          for text, annotations in batch:
              doc = nlp.make_doc(text)
              example = Example.from_dict(doc, annotations)
              test = spacy.training.offsets_to_biluo_tags(doc, annotations.get("entities"))
              if '-' in test:
                print(text, ' | ', text[annotations.get("entities")[0][0]:annotations.get("entities")[0][1]], " | ", test)
              texts, annotations = zip(*batch)
              nlp.update(
                          [example],
                          losses={},
                          drop=0.5,  # dropout - make it harder to memorise data
                      )
  
  nlp.to_disk("models/nlp_en")

def getEntitiesFromSentence(sentence : str) :
  nlp_updated = spacy.load("models/nlp_en")
  doc = nlp_updated(sentence)
  return [(ent.text, ent.label_) for ent in doc.ents]

print(getEntitiesFromSentence("hello jarvis what's the weather like"))
print("--- %s seconds ---" % (time.time() - start_time))
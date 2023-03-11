import spacy
from spacy.util import minibatch, compounding
from spacy.training import Example
from pathlib import Path
import time
import random


start_time = time.time()

def train_nlp_en():
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
              #Acknowledgment
              ("Thank you", {"entities" : [(0, 9, "ACKNOWLEDGMENT")]}),
              ("Thank you very much", {"entities" : [(0, 19, "ACKNOWLEDGMENT")]}),
              ("Thank you a lot", {"entities" : [(0, 15, "ACKNOWLEDGMENT")]}),
              ("Thanks", {"entities" : [(0, 6, "ACKNOWLEDGMENT")]}),
              ("Thanks Jarvis", {"entities" : [(0, 6, "ACKNOWLEDGMENT")]}),
              #Wellbeing
              ("how are you doing", {"entities" : [(0, 17, "WELLBEING")]}),
              ("how's it going", {"entities" : [(0, 14, "WELLBEING")]}),
              ("how have you been", {"entities" : [(0, 17, "WELLBEING")]}),
              ("what's up", {"entities": [(0, 9, "WELLBEING")]}),
              ("how's your day been so far", {"entities" : [(0, 26, "WELLBEING")]}),
              ("how are things", {"entities" : [(0, 14, "WELLBEING")]}),
              ("what's new", {"entities" : [(0, 10, "WELLBEING")]}),
              ("how are you feeling today", {"entities" : [(0, 25, "WELLBEING")]}),
              ("how's life treating you", {"entities" : [(0, 23, "WELLBEING")]}),
              ("how's your week been", {"entities" : [(0, 20, "WELLBEING")]}),
              ("how are you holding up", {"entities" : [(0, 22, "WELLBEING")]}),
              ("how's everything going with you", {"entities" : [(0, 31, "WELLBEING")]}),
              ("what's going on with you", {"entities" : [(0, 24, "WELLBEING")]}),
              ("how are you keeping", {"entities" : [(0, 19, "WELLBEING")]}),
              #Purpose
              ("what can you do for me", {"entities" : [(0, 22, "PURPOSE")]}),
              ("what is your function", {"entities" : [(0, 21, "PURPOSE")]}),
              ("how can you assist me", {"entities" : [(0, 21, "PURPOSE")]}),
              ("what is your purpose", {"entities" : [(0, 20, "PURPOSE")]}),
              ("what are you designed to do", {"entities" : [(0, 27, "PURPOSE")]}),
              ("what are your capabilities", {"entities" : [(0, 26, "PURPOSE")]}),
              ("can you tell me about your features", {"entities" : [(0, 35, "PURPOSE")]}),
              ("how can you help me accomplish my goals", {"entities" : [(0, 39, "PURPOSE")]}),
              ("what kind of tasks can you perform", {"entities" : [(0, 34, "PURPOSE")]}),
              ("what problems can you solve for me", {"entities" : [(0, 34, "PURPOSE")]}),
              ("can you explain how you work", {"entities" : [(0, 28, "PURPOSE")]}),
              ("what are the benefits of using you", {"entities" : [(0, 34, "PURPOSE")]}),
              ("how can you make my life easier", {"entities" : [(0, 31, "PURPOSE")]}),
              ("what are your strengths", {"entities" : [(0, 23, "PURPOSE")]}),
              ("what are some examples of things you can do", {"entities" : [(0, 43, "PURPOSE")]}),
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
              ("Play till i collapse", {"entities": [(5, 20, "MUSIC_NAME")]}),
              ("Play the song till i collapse", {"entities": [(14, 29, "MUSIC_NAME")]}),
              ("Launch till i collapse", {"entities": [(7, 22, "MUSIC_NAME")]}),
              ("Play merry christmas", {"entities": [(5, 20, "MUSIC_NAME")]}),
              ("Play the song merry christmas", {"entities": [(14, 29, "MUSIC_NAME")]}),
              ("Launch merry christmas", {"entities": [(7, 22, "MUSIC_NAME")]}),
              ("Play sweet child o' mine", {"entities": [(5, 24, "MUSIC_NAME")]}),
              ("Play the song sweet child o' mine", {"entities": [(14, 33, "MUSIC_NAME")]}),
              ("Play stairway to heaven", {"entities": [(5, 23, "MUSIC_NAME")]}),
              ("Play the song stairway to heaven", {"entities": [(14, 32, "MUSIC_NAME")]}),
              ("Play wonderwall", {"entities": [(5, 15, "MUSIC_NAME")]}),
              ("Play the song wonderwall", {"entities": [(14, 24, "MUSIC_NAME")]}),
              ("Play livin' on a prayer", {"entities": [(5, 23, "MUSIC_NAME")]}),
              ("Play the song livin' on a prayer", {"entities": [(14, 32, "MUSIC_NAME")]}),
              ("Play hotel california", {"entities": [(5, 21, "MUSIC_NAME")]}),
              ("Play the song hotel california", {"entities": [(14, 30, "MUSIC_NAME")]}),
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
              #Chess
              ("hey there, let's play a game of chess", {"entities": [(11, 37, "CHESS")]}),
              ("i'm in the mood for some chess shall we play", {"entities": [(20, 44, "CHESS")]}),
              ("jarvis, let's start a game of chess", {"entities": [(8, 35, "CHESS")]}),
              ("i challenge you to a game of chess, jarvis are you ready", {"entities": [(0, 35, "CHESS")]}),
              ("are you up for a game of chess, jarvis", {"entities": [(0, 30, "CHESS")]}),
              ("i've been practicing my chess skills want to play a game with me, jarvis", {"entities": [(0, 64, "CHESS")]}),
              # ("let's see who's better at chess, me or you, jarvis.", {"entities": [(25, 30, "CHESS")]}),
              # ("i'm looking for a good opponent for a chess match. will you play with me, ai", {"entities": [(52, 57, "CHESS")]}),
              # ("i'm excited to play a game of chess with you, jarvis.", {"entities": [(26, 31, "CHESS")]}),
              # ("jarvis, i want to test my skills against you in a game of chess.", {"entities": [(49, 54, "CHESS")]}),
              # ("shall we start a game of chess, ai. it's been a while since we last played.", {"entities": [(23, 28, "CHESS")]}),
              # ("i'm up for a challenge. how about a game of chess, jarvis", {"entities": [(36, 41, "CHESS")]}),
              # ("jarvis, i hope you're ready for a tough game of chess.", {"entities": [(42, 47, "CHESS")]}),
              # ("i'm in the mood for a strategic game. let's play chess, ai.", {"entities": [(40, 45, "CHESS")]}),
              # ("i think it's time for a friendly game of chess, jarvis. shall we begin", {"entities": [(43, 48, "CHESS")]}),
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
                          drop=0.4,  # dropout - make it harder to memorise data
                      )
  
  nlp.to_disk("models/nlp_en")

def train_nlp_fr():
  nlp=spacy.load('fr_core_news_sm')
  
  # Getting the pipeline component
  ner=nlp.get_pipe("ner")

  # training data
  TRAIN_DATA = [
              #Salutation
              ("salut", {"entities": [(0, 5, "GREETING")]}),
              ("bonjour", {"entities": [(0, 7, "GREETING")]}),
              ("bonjour jarvis", {"entities": [(0, 7, "GREETING")]}),
              ("salutations", {"entities": [(0, 11, "GREETING")]}),
              ("salutations jarvis", {"entities": [(0, 11, "GREETING")]}),
              ("coucou", {"entities": [(0, 6, "GREETING")]}),
              ("hey", {"entities": [(0, 3, "GREETING")]}),
              ("hey jarvis", {"entities": [(0, 3, "GREETING")]}),
              ("bonsoir", {"entities": [(0, 7, "GREETING")]}),
              ("bonsoir jarvis", {"entities": [(0, 7, "GREETING")]}),
              ("yo", {"entities": [(0, 2, "GREETING")]}),
              #Remerciement
              ("Merci", {"entities" : [(0, 5, "ACKNOWLEDGMENT")]}),
              ("Merci beaucoup", {"entities" : [(0, 14, "ACKNOWLEDGMENT")]}),
              ("Je te remercie", {"entities" : [(0, 14, "ACKNOWLEDGMENT")]}),
              ("Merci Jarvis", {"entities" : [(0, 5, "ACKNOWLEDGMENT")]}),
              ("Merci pour ton aide", {"entities" : [(0, 19, "ACKNOWLEDGMENT")]}),
              #Bien-etre
              ("comment vas tu", {"entities" : [(0, 14, "WELLBEING")]}),
              ("comment ça va", {"entities" : [(0, 13, "WELLBEING")]}),
              ("ça va", {"entities" : [(0, 5, "WELLBEING")]}),
              ("comment tu vas", {"entities": [(0, 14, "WELLBEING")]}),
              ("comment était ta journée", {"entities" : [(0, 24, "WELLBEING")]}),
              ("quoi de neuf", {"entities" : [(0, 12, "WELLBEING")]}),
              ("comment tu te sens", {"entities" : [(0, 18, "WELLBEING")]}),
              ("comment tu te sens aujourd'hui", {"entities" : [(0, 30, "WELLBEING")]}),
              ("comment était ta semaine", {"entities" : [(0, 24, "WELLBEING")]}),
              #Role
              ("que peux tu faire pour moi", {"entities" : [(0, 26, "PURPOSE")]}),
              ("quelle est ta fonction", {"entities" : [(0, 22, "PURPOSE")]}),
              ("comment peux tu m'aider", {"entities" : [(0, 23, "PURPOSE")]}),
              ("quel est ton rôle", {"entities" : [(0, 17, "PURPOSE")]}),
              ("dans quel but es tu conçu", {"entities" : [(0, 25, "PURPOSE")]}),
              ("quelles sont tes capacités", {"entities" : [(0, 26, "PURPOSE")]}),
              ("peux tu me dire quelles sont tes fonctionnalités", {"entities" : [(0, 48, "PURPOSE")]}),
              ("comment peux tu m'aider à accomplir mes objectifs", {"entities" : [(0, 49, "PURPOSE")]}),
              ("quel type de tâches peux tu effectuer", {"entities" : [(0, 37, "PURPOSE")]}),
              ("peux tu m'expliquer comment tu fonctionnes", {"entities" : [(0, 42, "PURPOSE")]}),
              ("quels sont les bénéfices de t'utiliser", {"entities" : [(0, 38, "PURPOSE")]}),
              ("donne moi des exemples de ce que tu peux faire", {"entities" : [(0, 46, "PURPOSE")]}),
              #Musique
              ("joue back in black", {"entities": [(5, 18, "MUSIC_NAME")]}),
              ("joue la musique back in black", {"entities": [(16, 29, "MUSIC_NAME")]}),
              ("joue la musique back in black de ac/dc", {"entities": [(16, 29, "MUSIC_NAME")]}),
              ("joue back in black from ac/dc", {"entities": [(5, 18, "MUSIC_NAME")]}),
              ("lance back in black", {"entities": [(6, 19, "MUSIC_NAME")]}),
              ("lance back in black de ac/dc", {"entities": [(6, 19, "MUSIC_NAME")]}),
              ("joue bad romance", {"entities": [(5, 16, "MUSIC_NAME")]}),
              ("joue la musique bad romance", {"entities": [(16, 27, "MUSIC_NAME")]}),
              ("lance bad romance", {"entities": [(6, 17, "MUSIC_NAME")]}),
              ("joue till i collapse", {"entities": [(5, 20, "MUSIC_NAME")]}),
              ("joue la musique till i collapse", {"entities": [(16, 31, "MUSIC_NAME")]}),
              ("lance till i collapse", {"entities": [(6, 21, "MUSIC_NAME")]}),
              ("joue merry christmas", {"entities": [(5, 20, "MUSIC_NAME")]}),
              ("joue la musique merry christmas", {"entities": [(16, 31, "MUSIC_NAME")]}),
              ("lance merry christmas", {"entities": [(6, 21, "MUSIC_NAME")]}),
              ("joue sweet child o' mine", {"entities": [(5, 24, "MUSIC_NAME")]}),
              ("joue la musique sweet child o' mine", {"entities": [(16, 35, "MUSIC_NAME")]}),
              ("joue stairway to heaven", {"entities": [(5, 23, "MUSIC_NAME")]}),
              ("joue la musique stairway to heaven", {"entities": [(16, 34, "MUSIC_NAME")]}),
              ("joue wonderwall", {"entities": [(5, 15, "MUSIC_NAME")]}),
              ("joue la musique wonderwall", {"entities": [(16, 26, "MUSIC_NAME")]}),
              ("joue livin' on a prayer", {"entities": [(5, 23, "MUSIC_NAME")]}),
              ("joue la musique livin' on a prayer", {"entities": [(16, 34, "MUSIC_NAME")]}),
              ("joue hotel california", {"entities": [(5, 21, "MUSIC_NAME")]}),
              ("joue la musique hotel california", {"entities": [(16, 32, "MUSIC_NAME")]}),
              #Meteo
              ("quelle est la météo", {"entities" : [(0, 19, "WEATHER")]}),
              ("quel temps fait il aujourd'hui", {"entities" : [(0, 30, "WEATHER")]}),
              ("attendons nous de la pluie aujourd'hui", {"entities" : [(0, 38, "WEATHER")]}),
              ("ai je besoin d'un parapluie aujourd'hui", {"entities" : [(0, 39, "WEATHER")]}),
              ("quel temps fait il", {"entities" : [(0, 18, "WEATHER")]}),
              ("est ce qu il neige aujourd'hui", {"entities" : [(0, 30, "WEATHER")]}),
              ("quelles sont les prévisions météorologiques pour aujourd'hui", {"entities" : [(0, 60, "WEATHER")]}), 
              ("quel est le temps prévu pour aujourd'hui", {"entities" : [(0, 40, "WEATHER")]}),
              ("fait il humide dehors aujourd'hui", {"entities" : [(0, 33, "WEATHER")]}),
              ("quel temps fait il dans la région", {"entities" : [(0, 33, "WEATHER")]}), 
              ("quelle est la situation météorologique en ce moment", {"entities" : [(0, 51, "WEATHER")]}),
              ("est ce une bonne journée pour les activités de plein air", {"entities" : [(0, 56, "WEATHER")]}),
              #Infos
              ("quelles sont les nouvelles du jours", {"entities" : [(0, 35, "NEWS")]}),
              ("quelles sont les news", {"entities" : [(0, 21, "NEWS")]}),
              ("peux-tu m'informer des dernières nouvelles", {"entities" : [(0, 42, "NEWS")]}),
              ("dis moi ce qu'il se passe dans le monde", {"entities" : [(0, 39, "NEWS")]}),
              ("que s'est-il passé dernièrement", {"entities" : [(0, 31, "NEWS")]}), 
              ("qu'est-ce qui s'est passé dernièrement", {"entities" : [(0, 38, "NEWS")]}),
              ("peux-tu me dire quelles sont les principales nouvelles", {"entities" : [(0, 54, "NEWS")]}),
              ("j'ai besoin d'une mise à jour sur les événements actuels", {"entities" : [(0, 56, "NEWS")]}),
              ("quelque chose d'intéressant dans les nouvelles aujourd'hui", {"entities" : [(0, 58, "NEWS")]}),
              ("quels sont les titres de la journée", {"entities" : [(0, 35, "NEWS")]}), 
              ("quoi de neuf dans l'actualité aujourd'hui", {"entities" :  [(0, 41, "NEWS")]}),
              ("quelles sont les actualités du moment", {"entities" : [(0, 37, "NEWS")]}), 
              ("peux-tu me donner une mise à jour des actualités", {"entities" :  [(0, 48, "NEWS")]}),
              ("je n'ai pas suivi l'actualité, que se passe-t-il", {"entities" : [(0, 48, "NEWS")]}),
              ("des nouvelles importantes à rapporter", {"entities" : [(0, 37, "NEWS")]}),
              ("ce qui se passe dans le monde", {"entities" : [(0, 29, "NEWS")]}),
              ("peux-tu me donner un aperçu des nouvelles", {"entities" : [(0, 41, "NEWS")]}), 
              ("que se passe-t-il dans le monde", {"entities" : [(0, 31, "NEWS")]}),
              #Echecs
              ("jouons aux échecs", {"entities" : [(0, 17, "CHESS")]}),
              ("faisons une partie d'échecs", {"entities" : [(0, 27, "CHESS")]}),
              ("je suis d'humeur à jouer aux échecs", {"entities" : [(0, 35, "CHESS")]}),
              ("commençons une partie d'échecs", {"entities" : [(0, 30, "CHESS")]}),
              ("je te défie de jouer aux échecs", {"entities" : [(0, 31, "chess")]}),
              ("je me suis entrainé aux échecs veux tu jouer une partie avec moi", {"entities" : [(0, 64, "CHESS")]})
              ]

  for _, annotations in TRAIN_DATA:
    print(annotations.get("entities"))
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
                          drop=0.6,  # dropout - make it harder to memorise data
                      )
  
  nlp.to_disk("models/nlp_fr")

def train_nlp_chess_en():
  nlp=spacy.load('en_core_web_sm')
  
  # Getting the pipeline component
  ner=nlp.get_pipe("ner")

  # training data
  TRAIN_DATA = [
              ("delta 2", {"entities": [(0, 5, "CHESS_COL_TO"),(6, 7, "CHESS_ROW_TO")]}),
              ("hotel 1", {"entities": [(0, 5, "CHESS_COL_TO"),(6, 7, "CHESS_ROW_TO")]}),
              ("alpha 3", {"entities": [(0, 5, "CHESS_COL_TO"),(6, 7, "CHESS_ROW_TO")]}),
              ("delta 8", {"entities": [(0, 5, "CHESS_COL_TO"),(6, 7, "CHESS_ROW_TO")]}),
              ("charlie two", {"entities": [(0, 7, "CHESS_COL_TO"),(8, 11, "CHESS_ROW_TO")]}),
              ("pawn delta 2", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("rook bravo 1", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("pawn alpha 6", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("rook hotel 1", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("pawn hotel 4", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("rook delta 8", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("rook hotel 6", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("rook alpha 4", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("pawn alpha 5", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("pawn hotel 1 promotes to queen", {"entities": [(25, 30, "CHESS_PROMOTION"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("pawn alpha 8 promotes to rook", {"entities": [(25, 29, "CHESS_PROMOTION"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("pawn alpha 8 promote to rook", {"entities": [(24, 28, "CHESS_PROMOTION"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("pawn charlie 8 promotes rook", {"entities": [(24, 28, "CHESS_PROMOTION"),(5, 12, "CHESS_COL_TO"),(13,14, "CHESS_ROW_TO")]}),
              ("pawn foxtrot 1 promote queen", {"entities": [(23, 28, "CHESS_PROMOTION"),(5, 12, "CHESS_COL_TO"),(13,14, "CHESS_ROW_TO")]}),
              ("pawn bravo 4 alpha 2 promotes to queen", {"entities": [(33, 38, "CHESS_PROMOTION"),(5, 10, "CHESS_COL_FROM"),(11, 12, "CHESS_ROW_FROM"),(13, 18, "CHESS_COL_TO"),(19, 20, "CHESS_ROW_TO")]}),
              ("pawn hotel 2", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("rook hotel 4", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("king alpha 4", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("king bravo 5", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("king delta 7", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("king hotel 2", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("king bravo 8", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("gone alpha 5", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("bean hotel 5", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("pawn bravo 4", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("rook alpha 7", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("cook hotel 6", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("book alpha 4", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("fawn hotel 2", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("lean bravo 8", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,12, "CHESS_ROW_TO")]}),
              ("rook hotel six", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,14, "CHESS_ROW_TO")]}),
              ("pawn hotel two", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,14, "CHESS_ROW_TO")]}),
              ("rook alpha four", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,15, "CHESS_ROW_TO")]}),
              ("pawn alpha five", {"entities": [(0, 4, "CHESS_PIECE"),(5, 10, "CHESS_COL_TO"),(11,15, "CHESS_ROW_TO")]}),
              ("pawn foxtrot 5", {"entities": [(0, 4, "CHESS_PIECE"),(5, 12, "CHESS_COL_TO"),(13,14, "CHESS_ROW_TO")]}),
              ("took charlie 2", {"entities": [(0, 4, "CHESS_PIECE"),(5, 12, "CHESS_COL_TO"),(13,14, "CHESS_ROW_TO")]}),
              ("pawn charlie 7", {"entities": [(0, 4, "CHESS_PIECE"),(5, 12, "CHESS_COL_TO"),(13,14, "CHESS_ROW_TO")]}),
              ("rook foxtrot 3", {"entities": [(0, 4, "CHESS_PIECE"),(5, 12, "CHESS_COL_TO"),(13,14, "CHESS_ROW_TO")]}),
              ("rook charlie 2", {"entities": [(0, 4, "CHESS_PIECE"),(5, 12, "CHESS_COL_TO"),(13,14, "CHESS_ROW_TO")]}),
              ("pawn foxtrot 3", {"entities": [(0, 4, "CHESS_PIECE"),(5, 12, "CHESS_COL_TO"),(13,14, "CHESS_ROW_TO")]}),
              ("look foxtrot 3", {"entities": [(0, 4, "CHESS_PIECE"),(5, 12, "CHESS_COL_TO"),(13,14, "CHESS_ROW_TO")]}),
              ("lawn charlie 7", {"entities": [(0, 4, "CHESS_PIECE"),(5, 12, "CHESS_COL_TO"),(13,14, "CHESS_ROW_TO")]}),
              ("dawn foxtrot 5", {"entities": [(0, 4, "CHESS_PIECE"),(5, 12, "CHESS_COL_TO"),(13,14, "CHESS_ROW_TO")]}),
              ("pawn charlie seven", {"entities": [(0, 4, "CHESS_PIECE"),(5, 12, "CHESS_COL_TO"),(13,18, "CHESS_ROW_TO")]}),
              ("rook foxtrot three", {"entities": [(0, 4, "CHESS_PIECE"),(5, 12, "CHESS_COL_TO"),(13,18, "CHESS_ROW_TO")]}),
              ("queen alpha 1", {"entities": [(0, 5, "CHESS_PIECE"),(6, 11, "CHESS_COL_TO"),(12, 13, "CHESS_ROW_TO")]}),
              ("queen delta 3", {"entities": [(0, 5, "CHESS_PIECE"),(6, 11, "CHESS_COL_TO"),(12, 13, "CHESS_ROW_TO")]}),
              ("queen bravo 8", {"entities": [(0, 5, "CHESS_PIECE"),(6, 11, "CHESS_COL_TO"),(12, 13, "CHESS_ROW_TO")]}),
              ("queen hotel 5", {"entities": [(0, 5, "CHESS_PIECE"),(6, 11, "CHESS_COL_TO"),(12, 13, "CHESS_ROW_TO")]}),
              ("queen delta 6", {"entities": [(0, 5, "CHESS_PIECE"),(6, 11, "CHESS_COL_TO"),(12, 13, "CHESS_ROW_TO")]}),
              ("scene alpha 1", {"entities": [(0, 5, "CHESS_PIECE"),(6, 11, "CHESS_COL_TO"),(12, 13, "CHESS_ROW_TO")]}),
              ("sight hotel 3", {"entities": [(0, 5, "CHESS_PIECE"),(6, 11, "CHESS_COL_TO"),(12, 13, "CHESS_ROW_TO")]}),
              ("might delta 7", {"entities": [(0, 5, "CHESS_PIECE"),(6, 11, "CHESS_COL_TO"),(12, 13, "CHESS_ROW_TO")]}),
              ("light hotel 7", {"entities": [(0, 5, "CHESS_PIECE"),(6, 11, "CHESS_COL_TO"),(12, 13, "CHESS_ROW_TO")]}),
              ("queen bravo eight", {"entities": [(0, 5, "CHESS_PIECE"),(6, 11, "CHESS_COL_TO"),(12, 17, "CHESS_ROW_TO")]}),
              ("queen hotel five", {"entities": [(0, 5, "CHESS_PIECE"),(6, 11, "CHESS_COL_TO"),(12, 16, "CHESS_ROW_TO")]}),
              ("queen foxtrot 4", {"entities": [(0, 5, "CHESS_PIECE"),(6, 13, "CHESS_COL_TO"),(14, 15, "CHESS_ROW_TO")]}),
              ("queen foxtrot 1", {"entities": [(0, 5, "CHESS_PIECE"),(6, 13, "CHESS_COL_TO"),(14, 15, "CHESS_ROW_TO")]}),
              ("queen charlie 6", {"entities": [(0, 5, "CHESS_PIECE"),(6, 13, "CHESS_COL_TO"),(14, 15, "CHESS_ROW_TO")]}),
              ("green foxtrot 1", {"entities": [(0, 5, "CHESS_PIECE"),(6, 13, "CHESS_COL_TO"),(14, 15, "CHESS_ROW_TO")]}),
              ("queen charlie 4", {"entities": [(0, 5, "CHESS_PIECE"),(6, 13, "CHESS_COL_TO"),(14, 15, "CHESS_ROW_TO")]}),
              ("queen foxtrot one", {"entities": [(0, 5, "CHESS_PIECE"),(6, 13, "CHESS_COL_TO"),(14, 17, "CHESS_ROW_TO")]}),
              ("knight echo 5", {"entities": [(0, 6, "CHESS_PIECE"),(7, 11, "CHESS_COL_TO"),(12, 13, "CHESS_ROW_TO")]}),
              ("knight bravo 3", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("bishop delta 4", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("knight hotel 3", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("bishop bravo 5", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("knight delta 7", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("bishop alpha 3", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("knight alpha 2", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("knight bravo 4 alpha 2", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_FROM"),(13, 14, "CHESS_ROW_FROM"),(15, 20, "CHESS_COL_TO"),(21, 22, "CHESS_ROW_TO")]}),
              ("bishop alpha 4 bravo 2", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_FROM"),(13, 14, "CHESS_ROW_FROM"),(15, 20, "CHESS_COL_TO"),(21, 22, "CHESS_ROW_TO")]}),
              ("knight delta 5 alpha 3", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_FROM"),(13, 14, "CHESS_ROW_FROM"),(15, 20, "CHESS_COL_TO"),(21, 22, "CHESS_ROW_TO")]}),
              ("pieces delta 8 bravo 6", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_FROM"),(13, 14, "CHESS_ROW_FROM"),(15, 20, "CHESS_COL_TO"),(21, 22, "CHESS_ROW_TO")]}),
              ("bishop hotel 8", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("bishop delta 5", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("knight hotel 7", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("bishop hotel 6", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("bishop bravo 8", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("knight delta 1", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("bishop delta 5", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("bishop delta 4", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("bishop bravo 5", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 14, "CHESS_ROW_TO")]}),
              ("bishop bravo five", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 17, "CHESS_ROW_TO")]}),
              ("bishop delta five", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 17, "CHESS_ROW_TO")]}),
              ("bishop delta four", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 17, "CHESS_ROW_TO")]}),
              ("knight hotel three", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 18, "CHESS_ROW_TO")]}),
              ("knight delta seven", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 18, "CHESS_ROW_TO")]}),
              ("knight hotel seven", {"entities": [(0, 6, "CHESS_PIECE"),(7, 12, "CHESS_COL_TO"),(13, 18, "CHESS_ROW_TO")]}),
              ("knight foxtrot 7", {"entities": [(0, 6, "CHESS_PIECE"),(7, 14, "CHESS_COL_TO"),(15, 16, "CHESS_ROW_TO")]}),
              ("bishop foxtrot 6", {"entities": [(0, 6, "CHESS_PIECE"),(7, 14, "CHESS_COL_TO"),(15, 16, "CHESS_ROW_TO")]}),
              ("bishop charlie 1", {"entities": [(0, 6, "CHESS_PIECE"),(7, 14, "CHESS_COL_TO"),(15, 16, "CHESS_ROW_TO")]}),
              ("knight foxtrot 2", {"entities": [(0, 6, "CHESS_PIECE"),(7, 14, "CHESS_COL_TO"),(15, 16, "CHESS_ROW_TO")]}),
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
                          drop=0.4,  # dropout - make it harder to memorise data
                      )
  
  nlp.to_disk("models/nlp_chess_en")

def train_nlp_chess_fr():
  nlp=spacy.load('fr_core_news_sm')
  
  # Getting the pipeline component
  ner=nlp.get_pipe("ner")

  # training data
  TRAIN_DATA = [
              ("pion delta 4", {"entities": [(5, 7, "PAWN_MOVEMENT")]}),
              ("pion hotel 5", {"entities": [(5, 7, "PAWN_MOVEMENT")]}),
              ("pion echo 4", {"entities": [(5, 7, "PAWN_MOVEMENT")]}),
              ("pion delta 5", {"entities": [(5, 7, "PAWN_MOVEMENT")]}),
              ("pion echo 5", {"entities": [(5, 7, "PAWN_MOVEMENT")]}),
              ("pion prend delta 4", {"entities": [(11, 13, "PAWN_CAPTURE")]}),
              ("pion prend hotel 1", {"entities": [(11, 13, "PAWN_CAPTURE")]}),
              ("pion prend bravo 6", {"entities": [(11, 13, "PAWN_CAPTURE")]}),
              ("pion prend foxtrot 4", {"entities": [(11, 13, "PAWN_CAPTURE")]}),
              ("pion prend golf 2", {"entities": [(11, 13, "PAWN_CAPTURE")]}),
              ("cavalier delta 4", {"entities": [(9, 11, "KNIGHT_MOVEMENT")]}),
              ("cavalier delta 4", {"entities": [(9, 11, "KNIGHT_MOVEMENT")]}),
              ("cavalier hotel 2", {"entities": [(9, 11, "KNIGHT_MOVEMENT")]}),
              ("cavalier alpha 5", {"entities": [(9, 11, "KNIGHT_MOVEMENT")]}),
              ("cavalier echo 3", {"entities": [(9, 11, "KNIGHT_MOVEMENT")]}),
              ("fou alpha 3", {"entities": [(4, 6, "BISHOP_MOVEMENT")]}),
              ("fou golf 8", {"entities": [(4, 6, "BISHOP_MOVEMENT")]}),
              ("fou hotel 8", {"entities": [(4, 6, "BISHOP_MOVEMENT")]}),
              ("fou bravo 3", {"entities": [(4, 6, "BISHOP_MOVEMENT")]}),
              ("fou foxtrot 5", {"entities": [(4, 6, "BISHOP_MOVEMENT")]}),
              ("tour hotel 8", {"entities": [(5, 7, "ROOK_MOVEMENT")]}),
              ("tour hotel 1", {"entities": [(5, 7, "ROOK_MOVEMENT")]}),
              ("tour golf 1", {"entities": [(5, 7, "ROOK_MOVEMENT")]}),
              ("tour alpha 2", {"entities": [(5, 7, "ROOK_MOVEMENT")]}),
              ("tour alpha 8", {"entities": [(5, 7, "ROOK_MOVEMENT")]}),
              ("dame delta 4", {"entities": [(5, 7, "QUEEN_MOVEMENT")]}),
              ("dame echo 3", {"entities": [(5, 7, "QUEEN_MOVEMENT")]}),
              ("dame alpha 2", {"entities": [(5, 7, "QUEEN_MOVEMENT")]}),
              ("dame foxtrot 4", {"entities": [(5, 7, "QUEEN_MOVEMENT")]}),
              ("dame hotel 1", {"entities": [(5, 7, "QUEEN_MOVEMENT")]}),
              ("roi golf 8", {"entities": [(4, 6, "KING_MOVEMENT")]}),
              ("roi bravo 1", {"entities": [(4, 6, "KING_MOVEMENT")]}),
              ("roi golf 1", {"entities": [(4, 6, "KING_MOVEMENT")]}),
              ("roi bravo 8", {"entities": [(4, 6, "KING_MOVEMENT")]}),
              ("roi charlie 3", {"entities": [(4, 6, "KING_MOVEMENT")]}),
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
                          drop=0.4,  # dropout - make it harder to memorise data
                      )
  
  nlp.to_disk("models/nlp_chess_fr")

def getEntitiesFromSentence(sentence : str, model : str) :
  nlp_updated = spacy.load(model)
  doc = nlp_updated(sentence)
  return [(ent.text, ent.label_) for ent in doc.ents]

def getChessMove(sentence : str, model : str) :
  nlp_updated = spacy.load(model)
  doc = nlp_updated(sentence)
  return [(ent.text, ent.label_) for ent in doc.ents]

# train_nlp_chess_en()

# print(getChessMove("phone bravo eight remote to queen", "models/nlp_chess_en"))
# print(getChessMove("pawn alpha 8 bravo 7 promote queen", "models/nlp_chess_en"))
# print(getChessMove("pawn alpha 5 bravo 6", "models/nlp_chess_en"))
# print("--- %s seconds ---" % (time.time() - start_time))  
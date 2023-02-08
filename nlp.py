import spacy
import random
from spacy.util import minibatch, compounding
from spacy.training import Example
from pathlib import Path

nlp=spacy.load('en_core_web_sm')

# Getting the pipeline component
ner=nlp.get_pipe("ner")

# training data
TRAIN_DATA = [
              # ("Hello there", {"entities": [(0, 4, "GREETING")]}),
              # ("Good morning", {"entities": [(0, 10, "GREETING")]}),
              # ("Good morning Jarvis", {"entities": [(0, 10, "GREETING")]}),
              # ("Greetings", {"entities": [(0, 8, "GREETING")]}),
              # ("Greetings Jarvis", {"entities": [(0, 8, "GREETING")]}),
              # ("Hiya", {"entities": [(0, 3, "GREETING")]}),
              # ("Hey", {"entities": [(0, 2, "GREETING")]}),
              # ("Hey Jarvis", {"entities": [(0, 2, "GREETING")]}),
              # ("Hi everyone", {"entities": [(0, 10, "GREETING")]}),
              # ("What's up", {"entities": [(0, 7, "GREETING")]}),
              # ("Good day", {"entities": [(0, 8, "GREETING")]}),
              # ("Hello", {"entities": [(0, 5, "GREETING")]}),
              # ("Hello Jarvis", {"entities": [(0, 5, "GREETING")]}),
              # ("Hi there", {"entities": [(0, 8, "GREETING")]}),
              # ("Howdy", {"entities": [(0, 5, "GREETING")]}),
              # ("Yo", {"entities": [(0, 2, "GREETING")]}),
              # ("Hola", {"entities": [(0, 4, "GREETING")]}),
              # ("Salutations", {"entities": [(0, 11, "GREETING")]}),
              # ("Hi", {"entities": [(0, 2, "GREETING")]}),
              # ("Hi Jarvis", {"entities": [(0, 2, "GREETING")]}),
              # ("Good evening", {"entities": [(0, 12, "GREETING")]}),
              # ("Good evening Jarvis", {"entities": [(0, 12, "GREETING")]}),
              ("Play Back in Black", {"entities": [(5, 17, "MUSIC_NAME")]}),
              ("Play the song Back in Black", {"entities": [(14, 26, "MUSIC_NAME")]}),
              ("Play the song Back in Black from AC/DC", {"entities": [(14, 26, "MUSIC_NAME")]}),
              ("Play Back in Black from AC/DC", {"entities": [(5, 17, "MUSIC_NAME")]}),
              ("Launch Back in Black", {"entities": [(7, 19, "MUSIC_NAME")]}),
              ("Launch Back in Black from AC/DC", {"entities": [(7, 19, "MUSIC_NAME")]}),
              ("Play Bad Romance", {"entities": [(5, 15, "MUSIC_NAME")]}),
              ("Play the song Bad Romance", {"entities": [(14, 24, "MUSIC_NAME")]}),
              ("Launch Bad Romance", {"entities": [(7, 17, "MUSIC_NAME")]}),
              ("Play Till I Collapse", {"entities": [(5, 19, "MUSIC_NAME")]}),
              ("Play the song Till I Collapse", {"entities": [(14, 28, "MUSIC_NAME")]}),
              ("Launch Till I Collapse", {"entities": [(7, 21, "MUSIC_NAME")]}),
              ("Play Merry Christmas", {"entities": [(5, 19, "MUSIC_NAME")]}),
              ("Play the song Merry Christmas", {"entities": [(14, 28, "MUSIC_NAME")]}),
              ("Launch Merry Christmas", {"entities": [(7, 21, "MUSIC_NAME")]}),
              ]

# Adding labels to the `ner`
for _, annotations in TRAIN_DATA:
  for ent in annotations.get("entities"):
      ner.add_label(ent[2])

# Disable pipeline components you dont need to change
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

# TRAINING THE MODEL
with nlp.disable_pipes(*unaffected_pipes):

  # Training for 30 iterations
  for iteration in range(30):

    # shuufling examples  before every iteration
    random.shuffle(TRAIN_DATA)
    # batch up the examples using spaCy's minibatch
    batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        for text, annotations in batch:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            texts, annotations = zip(*batch)
            nlp.update(
                        [example],
                        losses={},
                        drop=0.7,  # dropout - make it harder to memorise data
                    )

doc = nlp("Play Bad Romance")
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
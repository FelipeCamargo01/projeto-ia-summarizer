from transformers import PegasusForConditionalGeneration
from transformers import PegasusTokenizer
from transformers import pipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import AutoTokenizer, AutoModelForMaskedLM

en_model_name = "google/pegasus-large"
pt_model_name = 'phpaiola/ptt5-base-summ-xlsum'
pt_token_name = 'unicamp-dl/ptt5-base-portuguese-vocab'

import re 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))
pegasus_tokenizer_en = PegasusTokenizer.from_pretrained(en_model_name)
tokenizer_pt = T5Tokenizer.from_pretrained(pt_token_name)
model_pt = T5ForConditionalGeneration.from_pretrained(pt_model_name)

def doSummarize(text, algorithm):
    if algorithm == 'AutoTokenizer':
      model_name = "csebuetnlp/mT5_multilingual_XLSum"
      tokenizer = AutoTokenizer.from_pretrained(model_name)
      model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

      input_ids = tokenizer(
          [WHITESPACE_HANDLER(text)],
          return_tensors="pt",
          padding="max_length",
          truncation=True,
          max_length=512
      )["input_ids"]

      output_ids = model.generate(
          input_ids=input_ids,
          max_length=1000,
          no_repeat_ngram_size=2,
          num_beams=4
      )[0]

      summary = tokenizer.decode(
          output_ids,
          skip_special_tokens=True,
          clean_up_tokenization_spaces=False
      )

      return summary

    else:
      inputs = tokenizer_pt.encode(text, max_length=10000, truncation=True, return_tensors='pt')
      summary_ids = model_pt.generate(inputs, max_length=10000, min_length=32, num_beams=5, no_repeat_ngram_size=3, early_stopping=True)
      summary = tokenizer_pt.decode(summary_ids[0])

      return summary
  

   
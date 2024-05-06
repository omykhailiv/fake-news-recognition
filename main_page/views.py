import re
import string
import spacy
from nltk.corpus import stopwords
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from transformers import pipeline


@csrf_exempt
def render_main_page(request):
    if request.method == 'POST':
        text = request.POST.get('news-input-area')
        return redirect('render_predictions', text=text)
    return render(request, 'main_page/index.html')

def render_predictions(request, text):
    pipe = pipeline("text-classification", model="omykhailiv/bert-fake-news-recognition")
    prediction = pipe.predict(title_preprocess(text))
    output =create_output(prediction)
    return render(request, 'main_page/prediction_results.html',
                  {'label': output[0], 'score': output[1], 'news_title': text})

def create_output(prediction):
    p = prediction[0].get('label')
    if p=='LABEL_0':
        label = 'Fake'
    else:
        label = 'True'
    score = prediction[0].get('score')
    print(score)
    return [label, round(score, 3)*100]

def title_preprocess(text):
    lem = spacy.load('en_core_web_sm')
    stop_words = set('../stopwords/stopwords/english')
    # Convert text to lowercase for case-insensitive processing
    text = str(text).lower()

    # Remove HTML tags and their contents (e.g., "<tag>text</tag>")
    text = re.sub('<.*?>+\w+<.*?>', '', text)

    # Remove punctuation using regular expressions and string escaping
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)

    # Remove words containing alphanumeric characters followed by digits
    # (e.g., "model2023", "data10")
    text = re.sub('\w*\d\w*', '', text)

    # Remove newline characters
    text = re.sub('\n', '', text)

    # Replace multiple whitespace characters with a single space
    text = re.sub('\\s+', ' ', text)

    # Lemmatize words (convert them to their base form)
    text = lem(text)
    words = [word.lemma_ for word in text]

    # Removing stopwords, such as do, not, as, etc. (https://gist.github.com/sebleier/554280)
    new_filtered_words = [
        word for word in words if word not in stopwords.words('english')]
    return ' '.join(new_filtered_words)
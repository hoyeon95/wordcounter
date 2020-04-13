from django.shortcuts import render

# Create your views here.

# render는 3개의 인자까지 받을 수 있다.
# render(request객체, template이름, (optional)사전형자료형)

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def result(request):
    text = request.GET['fulltext'] # home.html에서 form에 입력한 값 전체를 fulltext로 이름 지었었음.
    words = text.split()
    word_dictionary = {}
    

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word] += 1
        else:
            #add to dictionary
            word_dictionary[word] = 1

    return render(request, 'wordcount/result.html', {'full': text, 'total': len(words), 'dictionary' : word_dictionary.items()})
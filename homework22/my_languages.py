def my_languages(results):
    return [k for k, v in (
        filter(lambda i: i[1] >= 60, sorted(results.items(), key=lambda item: item[1], reverse=True)))]


print(my_languages({"C++": 90, "Python": 147, "Java": 60}))

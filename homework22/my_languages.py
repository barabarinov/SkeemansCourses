def my_languages(results):
    return [k for k, v in (
        filter(lambda i: i[1] >= 60, sorted(results.items(), key=lambda item: item[1], reverse=True)))]


print(my_languages({"Dracenko": 90, "Syniuk": 147, "Miher_drumpex": 6000}))

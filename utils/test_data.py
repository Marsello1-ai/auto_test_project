pozitiv_authorize = ["Mars", "Marsello", "Shrek"]
negative_authorize = [None, 123, [], True]
pozitiv_payload_post_mem = [
    {
        "text": "fsdfsdf",
        "url": "https://upload.wikimedia.org/wikipedia/ru/a/a3/%D0%A3%D0%BF%D0%BE%D1%80%D0%BE%D1%82%D1%8B%D0%B9_%D0%BB%D0%B8%D1%81.jpeg",
        "tags": ["eqwewq", "adasdad"],
        "info": {"color": "white", "age": 25}
    },

    {
        "text": "fsdfsdf",
        "url": "%B9_%D0%BB%D0%B8%D1%81.jpeg",
        "tags": ["eqwewq", "adasdad"],
        "info": {"color": "white", "age": 25}
    }

]
negative_payload_post_mem = [
    {
        "text": 123,
        "url": "https://upload.wikimedia.org/wikipedia/ru/a/a3/%D0%A3%D0%BF%D0%BE%D1%80%D0%BE%D1%82%D1%8B%D0%B9_%D0%BB%D0%B8%D1%81.jpeg",
        "tags": ["eqwewq", "adasdad"],
        "info": {"color": "white", "age": 25}
    },

    {
        "text": "fsdfsdf",
        "url": "%B9_%D0%BB%D0%B8%D1%81.jpeg",
        "tags": "eqwewq",
        "info": {"color": "white", "age": 25}
    },

    {
        "text": "fsdfsdf",
        "url": "https://upload.wikimedia.org/wikipedia/ru/a/a3/%D0%A3%D0%BF%D0%BE%D1%80%D0%BE%D1%82%D1%8B%D0%B9_%D0%BB%D0%B8%D1%81.jpeg",
        "tags": ["eqwewq", "adasdad"],
        "info": ["color", "white", "age", 25]
    }

]

negative_payload_put_mem = [
    {
        "id": None,
        "text": 123,
        "url": "https://upload.wikimedia.org/wikipedia/ru/a/a3/%D0%A3%D0%BF%D0%BE%D1%80%D0%BE%D1%82%D1%8B%D0%B9_%D0%BB%D0%B8%D1%81.jpeg",
        "tags": ["eqwewq", "adasdad"],
        "info": {"color": "white", "age": 25}
    },

    {
        "id": None,
        "text": "fsdfsdf",
        "url": "%B9_%D0%BB%D0%B8%D1%81.jpeg",
        "tags": "eqwewq",
        "info": {"color": "white", "age": 25}
    },

    {
        "id": None,
        "text": "fsdfsdf",
        "url": "https://upload.wikimedia.org/wikipedia/ru/a/a3/%D0%A3%D0%BF%D0%BE%D1%80%D0%BE%D1%82%D1%8B%D0%B9_%D0%BB%D0%B8%D1%81.jpeg",
        "tags": ["eqwewq", "adasdad"],
        "info": ["color", "white", "age", 25]
    }

]

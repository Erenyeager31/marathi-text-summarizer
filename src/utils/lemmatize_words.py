lemmatization_dict = {
    # Verbs
    "लिखले": "लिखणे",  # "लिखले" is the past tense form of "लिखणे" (to write)
    "वाचले": "वाचणे",  # "वाचले" is the past tense form of "वाचणे" (to read)
    "सुरू": "सुरू",    # "सुरू" is already in its base form
    "हसत": "हसणे",    # "हसत" is the present continuous form of "हसणे" (to laugh)
    "सपळले": "सपळणे",  # "सपळले" is the past tense form of "सपळणे" (to succeed)
    "खाल्ले": "खाणे",  # "खाल्ले" is the past tense form of "खाणे" (to eat)
    "दिसले": "दिसणे",  # "दिसले" is the past tense form of "दिसणे" (to see)
    "आयले": "आयणे",   # "आयले" is the past tense form of "आयणे" (to come)
    "उचलले": "उचलणे", # "उचलले" is the past tense form of "उचलणे" (to lift)
    "धोपटले": "धोपटणे", # "धोपटले" is the past tense form of "धोपटणे" (to hit)
    "शेअर केले": "शेअर करणे", # "शेअर केले" is the past tense form of "शेअर करणे" (to share)
    "गेला": "जाणे",   # "गेला" is the past tense form of "जाणे" (to go)
    "फसवले": "फसवणे", # "फसवले" is the past tense form of "फसवणे" (to deceive)
    "आढळले": "आढळणे", # "आढळले" is the past tense form of "आढळणे" (to find)
    "सांगितले": "सांगणे", # "सांगितले" is the past tense form of "सांगणे" (to tell)
    "उतरणे": "उतरणे",  # "उतरणे" is the present tense form of "उतरणे" (to descend)
    "उठले": "उठणे",   # "उठले" is the past tense form of "उठणे" (to rise)
    "प्रेरित": "प्रेरित करणे", # "प्रेरित" is the past participle of "प्रेरित करणे" (to inspire)

    # Nouns
    "मुलं": "मुलगा",  # "मुलं" is the plural form of "मुलगा" (child)
    "पुस्तक": "पुस्तक",  # "पुस्तक" is already in its base form (book)
    "घर": "घर",      # "घर" is already in its base form (house)
    "काम": "काम",    # "काम" is already in its base form (work)
    "शाळा": "शाळा",  # "शाळा" is already in its base form (school)
    "आदमी": "आदमी",  # "आदमी" is already in its base form (man/person)
    "कुटुंब": "कुटुंब",  # "कुटुंब" is already in its base form (family)
    "कुत्रा": "कुत्रा",  # "कुत्रा" is already in its base form (dog)
    "फूल": "फूल",    # "फूल" is already in its base form (flower)
    "पाणी": "पाणी",   # "पाणी" is already in its base form (water)
    "आयुष्य": "आयुष्य", # "आयुष्य" is already in its base form (life)
    "काळ": "काळ",    # "काळ" is already in its base form (time/period)
    "तास": "तास",    # "तास" is already in its base form (hour)
    "कागद": "कागद",  # "कागद" is already in its base form (paper)
    "पेटी": "पेटी",   # "पेटी" is already in its base form (box)
    "संगणक": "संगणक", # "संगणक" is already in its base form (computer)
    "मायबोली": "मायबोली", # "मायबोली" is already in its base form (mother tongue)
    "विज्ञान": "विज्ञान", # "विज्ञान" is already in its base form (science)
    "समाज": "समाज",   # "समाज" is already in its base form (society)
    "फुटबॉल": "फुटबॉल", # "फुटबॉल" is already in its base form (football)

    # Adjectives
    "सुंदर": "सुंदर",  # "सुंदर" is already in its base form (beautiful)
    "आनंदी": "आनंदी",  # "आनंदी" is already in its base form (happy)
    "जाड": "जाड",      # "जाड" is already in its base form (thick)
    "कडक": "कडक",      # "कडक" is already in its base form (hard)
    "कसले": "कसले",    # "कसले" is already in its base form (good)
    "रात्री": "रात्री", # "रात्री" is already in its base form (nightly)
    "गोड": "गोड",      # "गोड" is already in its base form (sweet)
    "आळशी": "आळशी",   # "आळशी" is already in its base form (lazy)
    "शानदार": "शानदार",# "शानदार" is already in its base form (splendid)
    "आकर्षक": "आकर्षक",# "आकर्षक" is already in its base form (attractive)
    "मुलींचा": "मुली", # "मुलींचा" is the possessive form of "मुली" (girl's)
    "नवीन": "नवीन",   # "नवीन" is already in its base form (new)
    "ताज्या": "ताजे",  # "ताज्या" is the plural form of "ताजे" (fresh)

    # Pronouns
    "तुम्ही": "तुम्ही",  # "तुम्ही" is already in its base form (you - plural/formal)
    "तो": "तो",        # "तो" is already in its base form (he)
    "ती": "ती",        # "ती" is already in its base form (she)
    "आम्ही": "आम्ही",  # "आम्ही" is already in its base form (we)
    "ते": "ते",        # "ते" is already in its base form (they - neutral/plural)
    "हे": "हे",        # "हे" is already in its base form (this - neutral)
    "तीच": "तीच",     # "तीच" is already in its base form (she - emphatic)
    "आपण": "आपण",    # "आपण" is already in its base form (we - formal)
    "हे": "हे",        # "हे" is already in its base form (it - neutral)
    "त्यांना": "त्यांना", # "त्यांना" is already in its base form (to them)

    # Adverbs
    "आता": "आता",     # "आता" is already in its base form (now)
    "केल्याने": "केल्याने",  # "केल्याने" is already in its base form (after doing)
    "शिवाय": "शिवाय",  # "शिवाय" is already in its base form (without)
    "सर्व": "सर्व",    # "सर्व" is already in its base form (all)
    "फार": "फार",     # "फार" is already in its base form (very)
    "म्हणजे": "म्हणजे",# "म्हणजे" is already in its base form (i.e.)
    "नक्की": "नक्की",  # "नक्की" is already in its base form (surely)
    "सुट्टी": "सुट्टी", # "सुट्टी" is already in its base form (holiday)
    "आणखी": "आणखी",  # "आणखी" is already in its base form (more)
    "कधीच": "कधीच",  # "कधीच" is already in its

    "कृपया": "कृपया",
    "मजकूर": "मजकूर",
    "प्रविष्ट": "प्रविष्ट करणे",
    "करा": "करणे",
}

def lemmatize_word(word: str) -> str:
    return lemmatization_dict.get(word, word)  # Return the lemma or the word itself if not found

def lemmatize_tokenized_words(tokenized_words_list: list) -> list:
    lemmatized_list = []
    for sentence in tokenized_words_list:
        lemmatized_sentence = [lemmatize_word(word) for word in sentence]
        lemmatized_list.append(lemmatized_sentence)
    return lemmatized_list

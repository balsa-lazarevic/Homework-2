def getTagContent(haystack, needle):
    openTag = '<' + needle + '>'
    closeTag = '</' + needle + '>'
    openLen = len(openTag)
    closeLen = len(closeTag)

    lastBeginIndex = 0
    lastCloseIndex = 0

    occurences = []

    continueSearch = True
    while continueSearch:
        begin = haystack.find(openTag, lastBeginIndex)
        close = haystack.find(closeTag, lastCloseIndex)

        if(begin < 0):
            continueSearch = False
        else:
            lastBeginIndex = begin + openLen
            lastCloseIndex = close + closeLen  

            occurence = haystack[lastBeginIndex:close]
            occurences.append(occurence)
    return(occurences)

htmlString1 = '<h2>balsa</h2><h1>stefan</h1><h1>marko</h1>'
allOccurences = getTagContent(htmlString1, 'h2')
print(allOccurences)
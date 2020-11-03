# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common.

def match_mismatch(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()
    different = set(words1 + words2)
    # different = set(words1) ^ set(words2)
    common = set(words1) & set(words2)
    return list(different), list(common)

def test_input():
    sentence1 = 'We are really pleased to meet you in our city'
    sentence2 = 'The city was hit by a really heavy storm'

    different, common = match_mismatch(sentence1, sentence2)

    assert different.sort() == ['The','We','a','are','by','heavy','hit','in','meet','our', 'pleased','storm','to','was','you'].sort()
    assert common.sort() == ['city', 'really'].sort()

def palindrome(word):
    if len[word]==0: #we checked if the length of the word is 0 or not if it is simply return false
        return 'false'
    if word[0] != word[-1]: # here we are simply checking the main step of the function if the satrting and ending letter are same or not
        return 'False'#if not return false
    return palindrome[1:-1] #most crucial step, here we are outside the if loop that means both the if statement are false 
#and then returning to the function by removing both the letters 

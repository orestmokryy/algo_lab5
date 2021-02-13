def preprocess(string, size): 
    bad_character = [-1]*256
    for i in range(size): 
        bad_character[ord(string[i])] = i; 
    return bad_character 

def search(text, pattern): 
    matches = []
    pattern_length = len(pattern) 
    text_length = len(text) 
    bad_character = preprocess(pattern, pattern_length)  
    shift = 0
    while(shift <= text_length-pattern_length): 
        j = pattern_length-1

        while j>=0 and pattern[j] == text[shift+j]: 
            j -= 1
        if j<0: 
            
            matches.append(shift)
            shift += (pattern_length-bad_character[ord(text[shift+pattern_length])] if shift+pattern_length<text_length else 1) 
        else: 
            print(ord(text[shift+j]))
            shift += max(1, j-bad_character[ord(text[shift+j])]) 
    return matches

def main(): 
    text = "preprocessing"
    pattern = "cess"
    print(search(text, pattern)) 
  
if __name__ == '__main__': 
    main() 
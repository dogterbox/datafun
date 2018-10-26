def tokenize(text):
    tokens_by_slash = str(text.encode('utf-8')).split('/')	#get tokens after splitting by slash
    all_tokens = []
    for i in tokens_by_slash:
        tokens = str(i).split('-')	#get tokens after splitting by dash
        tokens_by_dot = []
        for j in range(0, len(tokens)):
            temp_tokens = str(tokens[j]).split('.')	#get tokens after splitting by dot
            tokens_by_dot = tokens_by_dot + temp_tokens
        all_tokens = all_tokens + tokens + tokens_by_dot
    all_tokens = list(set(all_tokens))	#remove redundant tokens

    return all_tokens
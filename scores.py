import configparser

config = configparser.ConfigParser()

#on écrit les scores dans un fichier
def write_score(name, score):
    config.read('scores.ini')
    if name in config:
        if int(config[name]['score']) < score:
            config[name]['score'] = str(score)
    else:
        config[name] = {'score': str(score)}
    with open('scores.ini', 'w') as configfile:
        config.write(configfile)

#on teste
#write_score('test', 100)
#write_score('test', 200)
#write_score('test2', 300)


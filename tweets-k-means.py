# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 08:13:31 2018
K-means algorithm to cluster Twiter data
"""
import json
import argparse

def read_list_from_txt_file(init_seed_file):
    '''
    input = open(init_seed_file, "r")
    content = input.read()
    list = content.split(',\n')
    '''
    list = []
    with open(init_seed_file)as file:
        for entry in file:
            list.append(int(entry.split(',')[0]))     
    return list

def read_json_texts(tweets_json_file):
    tweet_dict= dict()
    with open(tweets_json_file) as file:
        for entry in file:
            tweet_dict[json.loads(entry)['id']] = (json.loads(entry)['text'])
    file.close()
    return tweet_dict

def jaccard_distance(tweet1, tweet2):
    dist = 0
    tweet1_words = set(tweet1.split(' '))
    tweet2_words = set(tweet2.split(' '))
    union_set = set(tweet1.split(' ') + tweet2.split(' '))
    union_len = len(union_set)
    intersection_len = len(tweet1_words) + len(tweet2_words) - union_len
    if union_len != 0:
        dist = 1 - (intersection_len/float(union_len))
    return dist

def kmeans(k, seeds, tweets, output_file):
    if len(seeds) > k:
        print("The initial seed file has some extra see values. We will consider the first " + str(k) + " values.")
        val = 1
        for seed in seeds:
            if val > k:
                seeds.remove(seed)
            val = val+1
        
    if len(seeds) < k:
       print("The initial seed file does not have " + str(k) + " values.") 
       print("We will update k to the length of the initial seed lists.")
       k = len(seeds)
    
    # First we select the centroids with the initial seeds
    tweet_dict = dict()
    finished =  False
    while finished == False:
        finished = True
        tweet_dict.clear()
        for id_val, tweet in tweets.items():
            min_val = 1
            centroid = 0
            for seed in seeds:
                jac_dist = jaccard_distance(tweet, tweets[seed])
                if jac_dist < min_val:
                    min_val = jac_dist
                    centroid = seed
            if tweet_dict.get(centroid, "None") != "None":
                tweet_dict[centroid].append({id_val:tweet})
            else:
                tweet_dict[centroid] = [{id_val:tweet}] 
        for id_val, dicts in tweet_dict.items():
            #print("Start")
            centroid = 0
            min_val = len(tweets)
            for dict_elm in dicts:
                #print(dict_elm)
                for id, tweet in dict_elm.items():
                    sum_val = 0
                    for id_val_1, dicts_1 in tweet_dict.items():
                        for dict_elm_1 in dicts_1:
                            for id_1, tweet_1 in dict_elm_1.items():
                                if id_1 != id:
                                    '''
                                    jac_dist = jaccard_distance(tweet, tweet_1)
                                    if jac_dist < min_val:
                                           min_val = jac_dist
                                           centroid = id
                                    '''
                                    sum_val = sum_val + jaccard_distance(tweet, tweet_1)
                    if sum_val < min_val:
                        centroid = id
                        min_val = jac_dist
            #print("End")
            if id_val != centroid:
                #print(id_val)
                seeds.remove(id_val)
                seeds.append(centroid)
                finished= False
    fh = open(output_file, "w")
    #fh.write("<cluster-id>" + "\t\t" + "<List of tweet ids separated by comma>\n")
    i = 1
    sse = 0
    for id_val, dt in tweet_dict.items():
        id_list = []
        for dict_elm in dt:
            for key, val in dict_elm.items():
                id_list.append(key)
                jac_dist = jaccard_distance(val, tweets[id_val])
                sse = sse + (jac_dist*jac_dist)
        #print(str(i),"\t",dt)
        fh.write(str(i)+"\t"+str(id_list)[1:-1]+"\n")
        i = i + 1
    fh.write("\n"+str("SSE: ")+str(sse)+"\n")
    #print(str("Squared sum error: ")+str(sse)+"\n")

    
if __name__ == "__main__":
    default_k = 25
    default_init_seed_file = 'InitialSeeds.txt'
    default_tweets_json_file = 'Tweets.json'
    default_output_file = 'tweets-k-means-output.txt'
    parser = argparse.ArgumentParser()
    parser.add_argument("numberOfClusters", type=int, help="Number of Clusters.", nargs='?',
                        default=default_k, const=default_k)
    parser.add_argument("initialSeedsFile", type=str, help="File containing initial seeds.", nargs='?',
                        default=default_init_seed_file, const=default_init_seed_file)
    parser.add_argument("tweetsDataFile", type=str, help="File containing initial tweets in json format.", nargs='?',
                        default=default_tweets_json_file, const=default_tweets_json_file)
    parser.add_argument("outputFile", type=str, help="Output file to be created.", nargs='?',
                        default=default_output_file, const=default_output_file)
    args = parser.parse_args()

    k = args.numberOfClusters
    init_seed_file = args.initialSeedsFile
    tweets_json_file = args.tweetsDataFile
    output_file = args.outputFile
    seeds = read_list_from_txt_file(init_seed_file)
    '''
    print (k)
    print(init_seed_file)
    print(tweets_json_file)
    print(output_file)
    '''
    tweets = read_json_texts(tweets_json_file)
    kmeans(k, seeds, tweets, output_file)
    